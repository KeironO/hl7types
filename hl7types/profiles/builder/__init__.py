import importlib
from collections.abc import Callable
from typing import Any, Union, get_args, get_origin, get_type_hints

from pydantic import create_model
from pydantic.fields import Field, FieldInfo
from pydantic_core import PydanticUndefined

from hl7types import HL7Model, HL7Registry
from hl7types._utils import version_to_module
from hl7types.profiles.parser import (
    ProfileConstraints,
    SegGroupConstraint,
    SegmentConstraint,
    Usage,
)


def _import_segment(version: str, seg_name: str) -> type[HL7Model] | None:
    mod_name = version_to_module(version)
    try:
        mod = importlib.import_module(f"hl7types.hl7.{mod_name}.segments.{seg_name}")
        cls = getattr(mod, seg_name, None)
        if isinstance(cls, type) and issubclass(cls, HL7Model):
            return cls
        else:
            raise ValueError(f"segment {seg_name!r} is not a valid hl7 segment")
    except ModuleNotFoundError:
        raise ValueError(f"segment {seg_name!r} is not a valid hl7 segment")


def _copy_field_info(field: FieldInfo, **overrides: Any) -> FieldInfo:
    return Field(
        overrides.get("default", field.default),
        title=field.title,
        description=field.description,
        validation_alias=field.validation_alias,
        serialization_alias=field.serialization_alias,
    )


def _unwrap_optional(annotation: Any) -> tuple[Any, bool]:
    if get_origin(annotation) is Union and type(None) in get_args(annotation):
        inner_args = [a for a in get_args(annotation) if a is not type(None)]
        if len(inner_args) == 1:
            return inner_args[0], False
    return annotation, False


def _generate_table_checkerer(table_id: str, codes: set[str]) -> Callable[[str], str]:
    def _check(v: str) -> str:
        if v not in codes:
            raise ValueError(f"value {v!r} not in table {table_id}")
        return v

    return _check


def make_constrained_segment(
    base_cls: type[HL7Model],
    constraint: SegmentConstraint,
    tables: dict[str, set[str]] | None = None,
) -> type[HL7Model]:
    """Return a pydantic subclass of base_cls that enforces constraint."""

    seg_name = constraint.name
    print(seg_name)

    resolved_tables: dict[str, set[str]] = tables or {}

    field_overrides: dict[str, Any] = {}

    hints = get_type_hints(base_cls)

    for i, field_constraint in enumerate(constraint.fields, start=1):
        field_name = field_constraint.name
        if field_name not in base_cls.model_fields:
            print(f"{field_name} is not a valid field, skipping")

        # Need to get hints to compare and constrain
        hint = hints.get(field_name)

        if hint is None:
            continue

        has_usage_rules = field_constraint.usage in (Usage.REQUIRED, Usage.NOT_USED)
        has_length_rule = field_constraint.length is not None
        has_table_rule = bool(field_constraint.table and field_constraint.table in resolved_tables)

        if not (has_usage_rules, has_length_rule, has_table_rule):
            continue

        base_field = base_cls.model_fields[field_name]
        annotation = hint
        default = base_field.default

        if field_constraint.usage == Usage.NOT_USED:
            field_overrides[field_name] = (
                type(None),
                _copy_field_info(base_field, default=default),
            )
            continue

        if field_constraint.usage == Usage.REQUIRED:
            inner, was_optional = _unwrap_optional(annotation)
            if was_optional:
                annotation = inner
            default = PydanticUndefined

        if has_length_rule or has_table_rule:
            inner, was_optional = _unwrap_optional(annotation)
            if inner is str:
                metadata: list[Any] = [str]
                if has_length_rule:
                    metadata.append(Field(max_length=field_constraint.length))
                if has_table_rule:
                    checkerer = _generate_table_checkerer(
                        field_constraint, resolved_tables[field_constraint.table]
                    )
                    metadata.append(checkerer)
                    annotation = inner | None if was_optional else inner

            field_overrides[field_name] = (
                annotation,
                _copy_field_info(base_field, default=default),
            )

        if not field_overrides:
            return base_cls

        constrained_cls = create_model(seg_name, __base__=base_cls, **field_overrides)
        constrained_cls.__module__ = base_cls.__module__
        constrained_cls.__qualname__ = f"Profile{seg_name}"
        return constrained_cls


def build_registry_from_pofile(
    profile: ProfileConstraints,
    registry: HL7Registry,
    *,
    version: str | None = None,
    tables: dict[str, set[str]] | None = None,
) -> None:
    hl7_version = version or profile.hl7_version

    seen: set[str] = set()

    def _register(constraint: SegmentConstraint) -> None:
        name = constraint.name
        if name in seen:
            return
        seen.add(name)

        base_cls = _import_segment(hl7_version, name)

        if base_cls is None:
            return

        constrained = make_constrained_segment(base_cls, constraint, tables)
        if constrained is not base_cls:
            try:
                registry.register_segment(name, constrained)
            except ValueError as e:
                # TODO: Override this as it's likely going to be impacted by blocks to MSH/FHS/BHS protection
                raise e

        def _walk(children: list[SegmentConstraint | SegGroupConstraint]) -> None:
            for child in children:
                if isinstance(child, SegmentConstraint):
                    _register(child)
                elif isinstance(child, SegGroupConstraint):
                    _walk(child.children)

        _walk(profile.segments)

from typing import Any, get_type_hints

from hl7types import HL7Model
from hl7types.profiles.parser import SegmentConstraint, Usage


def make_constrained_segment(
    base_clas: type[HL7Model],
    constraint: SegmentConstraint,
    tables: dict[str, set[str]] | None = None,
) -> type[HL7Model]:
    """Return a pydantic subclass of base_cls that enforces constraint."""

    seg_name = constraint.name
    print(seg_name)

    resolved_tables: dict[str, set[str]] = tables or {}

    field_overrides: dict[str, Any] = {}

    hints = get_type_hints(base_clas)

    for i, field_constraint in enumerate(constraint.fields, start=1):
        field_name = field_constraint.name
        if field_name not in base_clas.model_fields:
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

        base_field = base_clas.model_fields[field_name]
        annotation = hint
        default = base_field.default

        print(annotation, default)

        if field_constraint.usage == Usage.NOT_USED:
            # NEED TO COPY FIELD, PROBABLY NEED A UTIL
            field_overrides[field_name] = (type(None),)
            continue


def build_registry_from_pofile():
    pass

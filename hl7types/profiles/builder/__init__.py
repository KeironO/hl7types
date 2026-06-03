from typing import Any

from hl7types import HL7Model
from hl7types.profiles.parser import SegmentConstraint


def make_constrained_segment(
    base_clas: type[HL7Model],
    constraint: SegmentConstraint,
    tables: dict[str, set[str]] | None = None,
) -> type[HL7Model]:
    """Return a pydantic subclass of base_cls that enforces constraint."""

    seg_name = constraint.name
    resolved_tables: dict[str, set[str]] = tables or {}

    field_overrides: dict[str, Any] = {}

    print(seg_name, resolved_tables, field_overrides)

    for i, field_constraint in enumerate(constraint.fields, start=1):
        field_name = field_constraint.name
        if field_name not in base_clas.model_fields:
            print(f"{field_name} is not a valid field, skipping")

        # Need to get hints to compare and constrain


def build_registry_from_pofile():
    pass

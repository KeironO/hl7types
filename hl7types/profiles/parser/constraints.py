from dataclasses import dataclass, field
from enum import Enum


class Usage(str, Enum):
    REQUIRED = "R"
    OPTIONAL = "O"
    CONDITIONAL = "C"
    BACKWARD_COMPAT = "B"
    NOT_USED = "X"
    REQUIRED_BUT_MAY_BE_EMPTY = "RE"


@dataclass
class SubComponentConstraint:
    name: str
    usage: Usage
    datatype: str
    length: int | None = None
    table: str | None = None


@dataclass
class ComponentConstraint:
    name: str
    usage: Usage
    datatype: str
    length: int | None = None
    table: str | None = None
    predicate: str | None = None
    sub_components: list[SubComponentConstraint] | None = None


@dataclass
class FieldConstraint:
    name: str
    usage: Usage
    min: int
    datatype: str
    max: int | None = None
    length: int | None = None
    item_no: str | None = None
    table: str | None = None
    components: list[ComponentConstraint] | None = field(default_factory=list)


@dataclass
class SegmentConstraint:
    name: str
    long_name: str
    usage: Usage
    min: int
    max: int | None = None
    fields: list[FieldConstraint] | None = field(default_factory=list)


@dataclass
class SegGroupConstraint:
    name: str
    long_name: str
    usage: Usage
    min: int
    max: int | None
    children: list[SegmentConstraint] | None = field(default_factory=list)


@dataclass
class ProfileConstraints:
    hl7_version: str
    msg_type: str
    event_type: str
    msg_struct_id: str
    name: str
    segments: list[SegmentConstraint | SegGroupConstraint] | None = field(default_factory=list)

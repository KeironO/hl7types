import xml.etree.ElementTree as ET
from pathlib import Path

from hl7types.profiles.parser.constraints import (
    ComponentConstraint,
    FieldConstraint,
    ProfileConstraints,
    SegGroupConstraint,
    SegmentConstraint,
    SubComponentConstraint,
    Usage,
)


def _parse_usage(value: str | None, default: str = "O") -> Usage:
    value = value or default

    try:
        return Usage(value)
    except ValueError:
        try:
            return Usage[value]
        except KeyError as exc:
            raise ValueError(f"Unknown usage value: {value!r}") from exc


def _parse_sub_component(elem: ET.Element) -> SubComponentConstraint:
    return SubComponentConstraint(
        name=elem.get("Name", ""),
        usage=_parse_usage(elem.get("Usage")),
        datatype=elem.get("Datatype", ""),
        length=int(elem.get("Length")) if elem.get("Length") else None,
        table=elem.get("Table"),
    )


def _parse_component(elem: ET.Element) -> ComponentConstraint:
    predicate = elem.find("Predicate")
    return ComponentConstraint(
        name=elem.get("Name", ""),
        usage=_parse_usage(elem.get("Usage")),
        datatype=elem.get("Datatype", ""),
        length=int(elem.get("Length")) if elem.get("Length") else None,
        table=elem.get("Table"),
        predicate=predicate.text.strip() if predicate is not None and predicate.text else None,
        sub_components=[_parse_sub_component(sc) for sc in elem.findall("SubComponent")],
    )


def _max(value: str | None) -> int | None:
    if value in (None, "*"):
        return None
    return int(value)


def _parse_field(elem: ET.Element) -> FieldConstraint:
    return FieldConstraint(
        name=elem.get("Name", ""),
        datatype=elem.get("Datatype", ""),
        min=int(elem.get("Min", "0")),
        max=_max(elem.get("Max", "*")),
        usage=_parse_usage(elem.get("Usage")),
        item_no=elem.get("ItemNo"),
        length=int(elem.get("Length")) if elem.get("Length") else None,
        table=elem.get("Table"),
        components=[_parse_component(c) for c in elem.findall("Component")],
    )


def _parse_segment(elem: ET.Element) -> SegmentConstraint:
    return SegmentConstraint(
        name=elem.get("Name", ""),
        long_name=elem.get("LongName", ""),
        usage=_parse_usage(elem.get("Usage")),
        min=int(elem.get("Min", "0")),
        max=_max(elem.get("Max", "*")),
        fields=[_parse_field(f) for f in elem.findall("Field")],
    )


def _parse_seg_group(elem: ET.Element) -> SegGroupConstraint:
    # This is an assumption and needs testing against more than the stuff we've seen so far.
    children: list[SegmentConstraint | SegGroupConstraint] = []
    for child in elem:
        if child.tag == "Segment":
            children.append(_parse_segment(child))
        elif child.tag == "SegGroup":
            children.append(_parse_seg_group(child))
    return SegGroupConstraint(
        name=elem.get("Name", ""),
        long_name=elem.get("LongName", ""),
        usage=_parse_usage(elem.get("Usage")),
        min=int(elem.get("Min", "0")),
        max=_max(elem.get("Max", "*")),
        children=children,
    )


def parse_tables(path: str | Path) -> dict[str, set[str]]:
    """Parse a table file into a mapping of table ID to allowed codes."""
    root = ET.parse(path).getroot()
    tables: dict[str, set[str]] = {}

    for hl7table in root.iter("hl7table"):
        table_id = hl7table.get("id")
        codes: set[str] = {
            elem.get("code") for elem in hl7table.findall("tableElement") if elem.get("code")
        }

        if table_id and codes:
            tables[table_id] = codes

    return tables


def parse_profile(path: str | Path) -> ProfileConstraints:
    """Parse an HL7 v2 conformance profile XML file into a ``ProfileConstraints`` object.

    Parameters
    ----------
    path : str or Path
        Path to the conformance profile XML file.

    Returns
    -------
    ProfileConstraints
        The full tree of segment and field constraints defined in the profile,
        along with metadata such as HL7 version, message type, and event type.

    Raises
    ------
    ValueError
        If the file does not contain a valid ``HL7v2xStaticDef`` element.
    """
    root = ET.parse(path).getroot()
    static_def = root.find("HL7v2xStaticDef")
    if static_def is None:
        raise ValueError(
            f"Could not parse profile {path}. No HL7v2StaticDEf element found in profile"
        )

    meta = root.find("MetaData")

    # Strip all of the metadata from the root, static def and meta.
    hl7_version = root.get("HL7Version")
    msg_type = static_def.get("MsgType")
    event_type = static_def.get("EventType")
    msg_struct_id = static_def.get("MsgStructID")
    name = meta.get("Name") if meta is not None else None

    children: list[SegmentConstraint | SegGroupConstraint] = []

    for child in static_def:
        if child.tag == "Segment":
            children.append(_parse_segment(child))
        elif child.tag == "SegGroup":
            children.append(_parse_seg_group(child))

    return ProfileConstraints(
        hl7_version=hl7_version,
        msg_type=msg_type,
        event_type=event_type,
        msg_struct_id=msg_struct_id,
        name=name,
        segments=children,
    )

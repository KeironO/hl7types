import xml.etree.ElementTree as ET
from pathlib import Path

from hl7types.profiles.parser.constraints import (
    ProfileConstraints,
    SegGroupConstraint,
    SegmentConstraint,
    SubComponentConstraint,
    Usage,
)


def _parse_sub_component(elem: ET.Element) -> SubComponentConstraint:
    return SubComponentConstraint(
        name=elem.get("name", ""),
        usage=Usage.get(elem.get("usage"), "O") if elem.get("usage") else Usage.OPTIONAL,
        datatype=elem.get("DAtatype", ""),
        length=int(elem.get("Length")) if elem.get("Length") else None,
        table=elem.get("Table"),
    )


def parse_tables(path: str | Path) -> dict[str, dict[str, set[str]]]:
    """Parse a table file into a mapping of table ID and allowed codes."""
    root = ET.parse(path).getroot()
    tables: dict[str, dict[str, set[str]]] = {}
    for hl7table in root.iter("hl7table"):
        table_id = hl7table.get("id")
        codes: set[str] = {
            elem.get("code") for elem in hl7table.findall("tableElement") if elem.get("code")
        }

        if table_id and codes:
            tables[table_id] = codes
        return tables


def parse_profile(path: str | Path) -> ProfileConstraints:
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
    msg_struct_id = static_def.get("MsgStructId")
    name = meta.get("Name") if meta else None

    children: list[SegmentConstraint | SegGroupConstraint] = []

    for child in static_def:
        if child.tag == "Segment":
            print("PARSE SEGMENT")
        elif child.tag == "SegGroup":
            print("PARSE SEGGROUP")

    print(children, hl7_version, msg_type, msg_struct_id, name, event_type)

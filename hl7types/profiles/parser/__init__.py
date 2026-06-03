import xml.etree.ElementTree as ET
from pathlib import Path

from hl7types.profiles.parser.constraints import ProfileConstraints


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
    pass

"""Release contract tests for required PID fields during XML decoding."""
from __future__ import annotations

from xml.etree import ElementTree as ET

import pytest
from pydantic import ValidationError

from hl7types import decode_er7, decode_xml, encode_xml
from hl7types.hl7.v2_5_1.messages.ADT_A01 import ADT_A01


ADT_A01_WIRE = (
    "MSH|^~\\&|SENDING|FACILITY|RECEIVING|DEST|20240101120000||ADT^A01^ADT_A01|MSG001|P|2.5.1\r"
    "EVN|A01|20240101120000\r"
    "PID|1||123456^^^MRN^MR||Doe^John^A||19800101|M\r"
    "PV1|1|I|WARD^BED1\r"
)


def _strip_elements_by_local_name(xml: str, local_name: str) -> str:
    root = ET.fromstring(xml)

    for parent in root.iter():
        for child in list(parent):
            if child.tag.split("}", 1)[-1] == local_name:
                parent.remove(child)

    return ET.tostring(root, encoding="unicode")


@pytest.mark.parametrize("removed_tag, expected_error", [("PID.3", "pid_3"), ("PID.5", "pid_5")])
def test_strict_xml_decode_rejects_missing_pid_required_fields(
    removed_tag: str,
    expected_error: str,
) -> None:
    msg = decode_er7(ADT_A01_WIRE, msg_cls=ADT_A01, strict=True)
    xml = encode_xml(msg)
    xml = _strip_elements_by_local_name(xml, removed_tag)

    with pytest.raises(ValidationError, match=expected_error):
        decode_xml(xml, msg_cls=ADT_A01, strict=True)

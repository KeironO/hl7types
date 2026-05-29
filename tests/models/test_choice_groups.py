"""
Tests for HL7 choice group validation.

Choice groups (like ORM_O01_CHOICE) require exactly one of their child elements
to be present, not all of them like sequence groups do.

Reference: https://github.com/crs4/hl7apy/issues/151
hl7apy.validation.Validator does not differentiate between sequence and choice group types.
Both fall into the same branch in _check_known_element, which iterates all child references
and calls _check_repetitions on each individually. For choice groups, this is incorrect
because only one child needs to be present, not all of them.
"""
from __future__ import annotations

from hl7types import decode_er7
from hl7types.hl7.v2_3.messages.ORM_O01 import ORM_O01


def test_orm_o01_choice_with_obr() -> None:
    """ORM_O01 message with OBR in choice group (valid case).

    Based on the hl7apy issue #151 example. OBR satisfies ORM_O01_CHOICE,
    so this message should parse without issues.
    """
    msg_text = (
        "MSH|^~\\&|SND|SND|RCV|RCV|20260101120000||ORM^O01|MSG001|P|2.3\r"
        "PID|1||12345||DOE^JOHN|||19800101|M\r"
        "ORC|NW||||||1^^^20260101120000|20260101120000\r"
        "OBR|1|||SPEC-001|PANEL|||20260101090000|||||||CSF||||||||||||1^^^20260101120000\r"
    )

    msg = decode_er7(msg_text, strict=True)
    assert isinstance(msg, ORM_O01)

"""
Tests emulating ca.uhn.hl7v2.model.AbstractMessageTest.
Source: https://github.com/hapifhir/hapi-hl7v2/blob/master/hapi-core/src/test/java/ca/uhn/hl7v2/model/AbstractMessageTest.java

Notes:
- testParseAndEncode adapted to test round-trip parsing and encoding.
- testGetVersion, testGenerateAck, testCopy and other Java-specific tests are
  not applicable to hl7types, which uses immutable Pydantic models.
"""
from __future__ import annotations

from hl7types import decode_er7


def test_parse_and_encode_roundtrip_v22() -> None:
    """Parse a v2.2 ADT^A01 message and verify roundtrip encoding.

    When a v2.2 message is parsed from ER7 and re-encoded, the structure
    should be preserved.
    """
    msg_text = (
        "MSH|^~\\&|LABGL1||DMCRES||19951002185200||ADT^A01|LABGL1199510021852632|P|2.2\r"
        "EVN|A01|19951002185200\r"
        "PID|||T12345||TEST^PATIENT^P||19601002|M||||||||||123456\r"
        "PV1||I|NER|||||||GSU||||||||E||||||||||||||||||||||||||19951002174900|19951006\r"
    )

    msg = decode_er7(msg_text)

    # Verify key fields are accessible
    assert msg.MSH.msh_10 == "LABGL1199510021852632"
    assert msg.MSH.msh_11 == "P"

    # Verify roundtrip encoding includes original data
    encoded = msg.model_dump_er7()
    assert "LABGL1199510021852632" in encoded
    assert "PID|" in encoded


def test_parse_sets_message_fields_v22() -> None:
    """Parsing a v2.2 message populates fields correctly.

    In v2.2, some fields that are repeating in later versions are single.
    For example, pid_5 is a single PN field, not a list.
    """
    msg_text = (
        "MSH|^~\\&|LABGL1||DMCRES||19951002185200||ADT^A01|LABGL1199510021852632|P|2.2\r"
        "EVN|A01|19951002185200\r"
        "PID|||T12345||TEST^PATIENT^P||19601002|M||||||||||123456\r"
        "PV1||I|NER|||||||GSU||||||||E||||||||||||||||||||||||||19951002174900|19951006\r"
    )

    msg = decode_er7(msg_text)

    # MSH fields (v2.2 parses these as strings, not objects)
    assert msg.MSH.msh_3 == "LABGL1"
    assert msg.MSH.msh_10 == "LABGL1199510021852632"
    assert msg.MSH.msh_11 == "P"

    # PID fields - pid_5 is a PN object in v2.2 (not a list)
    assert msg.PID.pid_3[0] == "T12345"
    assert msg.PID.pid_5.pn_1 == "TEST"
    assert msg.PID.pid_5.pn_2 == "PATIENT"
    assert msg.PID.pid_8 == "M"


def test_parse_sets_message_fields_v24() -> None:
    """Parsing a v2.4 message populates fields correctly.

    In v2.4, repeating fields like pid_5 are stored as lists.
    """
    msg_text = (
        "MSH|^~\\&|LABGL1||DMCRES||20010602185200||ADT^A01|LABGL1200106021852632|P|2.4\r"
        "EVN|A01|20010602185200\r"
        "PID|||T12345||TEST^PATIENT^P||19601002|M||||||||||123456\r"
        "PV1||I|NER|||||||GSU||||||||E||||||||||||||||||||||||||20010602174900|20010606\r"
    )

    msg = decode_er7(msg_text)

    # MSH fields (v2.4 parses these as objects)
    assert msg.MSH.msh_3.hd_1 == "LABGL1"
    assert msg.MSH.msh_10 == "LABGL1200106021852632"
    assert msg.MSH.msh_11.pt_1 == "P"

    # PID fields - pid_5 is a list of XPN objects in v2.4
    assert msg.PID.pid_3[0].cx_1 == "T12345"
    assert msg.PID.pid_5[0].xpn_2 == "PATIENT"
    assert msg.PID.pid_8 == "M"

    # PV1 fields
    assert msg.PV1.pv1_2 == "I"
    assert msg.PV1.pv1_3.pl_1 == "NER"


def test_message_version_v22() -> None:
    """ADT_A01 v2.2 messages should decode with version field.

    The version field should be accessible and contain the HL7 version.
    """
    msg_text = (
        "MSH|^~\\&|LABGL1||DMCRES||19951002185200||ADT^A01|LABGL1199510021852632|P|2.2\r"
        "EVN|A01|19951002185200\r"
        "PID|||T12345||TEST^PATIENT^P||19601002|M||||||||||123456\r"
        "PV1||I|NER|||||||GSU||||||||E||||||||||||||||||||||||||19951002174900|19951006\r"
    )

    msg = decode_er7(msg_text)
    assert msg.MSH.msh_12 == "2.2"


def test_message_version_v24() -> None:
    """ADT_A01 v2.4 messages should decode with version field.

    The version field should be accessible as a VID object in v2.4.
    """
    msg_text = (
        "MSH|^~\\&|LABGL1||DMCRES||20010602185200||ADT^A01|LABGL1200106021852632|P|2.4\r"
        "EVN|A01|20010602185200\r"
        "PID|||T12345||TEST^PATIENT^P||19601002|M||||||||||123456\r"
        "PV1||I|NER|||||||GSU||||||||E||||||||||||||||||||||||||20010602174900|20010606\r"
    )

    msg = decode_er7(msg_text)
    assert msg.MSH.msh_12.vid_1 == "2.4"

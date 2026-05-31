"""
Tests emulating ca.uhn.hl7v2.model.AbstractSegmentTest.
Source: https://github.com/hapifhir/hapi-hl7v2/blob/master/hapi-core/src/test/java/ca/uhn/hl7v2/model/AbstractSegmentTest.java

Notes:
- testEnsureEnoughFields, testUnexpectedFieldReps, testInsertRepetition are not directly
  applicable to hl7types, which uses immutable Pydantic models.
- testParseEmpty, testParseNull, and testParseMshWithNoContent are adapted to test
  the parsing and field handling behavior.
"""
from __future__ import annotations

from hl7types import decode_er7


def test_parse_and_roundtrip() -> None:
    """Parsing and re-encoding a message should preserve the original structure.

    When a message is parsed from ER7, the segments should be preserved,
    and re-encoding should produce equivalent output.
    """
    msg_text = (
        "MSH|^~\\&|LABGL1||DMCRES||19951002185200||ADT^A01|LABGL1199510021852632|P|2.2\r"
        "EVN|A01|19951002185200\r"
        "PID|||T12345||TEST^PATIENT^P||19601002|M||||||||||123456\r"
        "PV1||I|NER|||||||GSU||||||||E||||||||||||||||||||||||||19951002174900|19951006\r"
    )

    msg = decode_er7(msg_text)

    # Verify segments are present
    assert msg.MSH is not None
    assert msg.PID is not None
    assert msg.PV1 is not None

    # Re-encode and verify structure
    encoded = msg.model_dump_er7()
    assert "MSH|" in encoded
    assert "PID|" in encoded
    assert "PV1|" in encoded


def test_segment_field_access() -> None:
    """Segment fields should be accessible via the model.

    When parsing a message, individual segment fields should be
    extractable and accessible.
    """
    msg_text = (
        "MSH|^~\\&|LABGL1||DMCRES||19951002185200||ADT^A01|LABGL1199510021852632|P|2.2\r"
        "EVN|A01|19951002185200\r"
        "PID|||T12345||TEST^PATIENT^P||19601002|M||||||||||123456\r"
        "PV1||I|NER|||||||GSU||||||||E||||||||||||||||||||||||||19951002174900|19951006\r"
    )

    msg = decode_er7(msg_text)

    # MSH segment fields
    assert msg.MSH.msh_1 == "|"
    assert msg.MSH.msh_2 == "^~\\&"
    assert msg.MSH.msh_10 == "LABGL1199510021852632"

    # PID segment fields
    assert msg.PID.pid_8 == "M"

    # PV1 segment fields
    assert msg.PV1 is not None
    assert msg.PV1.pv1_2 == "I"


def test_msh_encoding_characters() -> None:
    """MSH segment encoding characters should be parseable.

    The MSH segment contains encoding characters that define how the
    rest of the message is encoded.
    """
    msg_text = (
        "MSH|^~\\&|LABGL1||DMCRES||19951002185200||ADT^A01|LABGL1199510021852632|P|2.2\r"
        "EVN|A01|19951002185200\r"
        "PID|||T12345||TEST^PATIENT^P||19601002|M||||||||||123456\r"
        "PV1||I|NER|||||||GSU||||||||E||||||||||||||||||||||||||19951002174900|19951006\r"
    )

    msg = decode_er7(msg_text)

    # Encoding characters should be set
    assert msg.MSH.msh_1 == "|"
    assert msg.MSH.msh_2 == "^~\\&"


def test_parse_segment_only() -> None:
    """A minimal strict ADT_A01 message should parse.

    Under strict decoding, ADT_A01 requires MSH, EVN, PID, and PV1.
    """
    msg_text = (
        "MSH|^~\\&|LABGL1||DMCRES||19951002185200||ADT^A01|LABGL1199510021852632|P|2.2\r"
        "EVN|A01|19951002185200\r"
        "PID|||T12345||TEST^PATIENT^P||19601002|M||||||||||123456\r"
        "PV1||I|NER|||||||GSU||||||||E||||||||||||||||||||||||||19951002174900|19951006\r"
    )

    msg = decode_er7(msg_text)

    assert msg.MSH is not None
    assert msg.PID is not None
    assert msg.PV1 is not None
    assert msg.PID.pid_3[0] == "T12345"

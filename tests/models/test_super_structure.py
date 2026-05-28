"""
Tests emulating ca.uhn.hl7v2.model.SuperStructureTest.
Source: https://github.com/hapifhir/hapi-hl7v2/blob/master/hapi-core/src/test/java/ca/uhn/hl7v2/model/SuperStructureTest.java

Tests for handling messages with repeating segments and various message structures.
"""
from __future__ import annotations

from hl7types import decode_er7


def test_parse_adt_a01_message() -> None:
    """ADT^A01 messages should parse correctly.

    A typical ADT^A01 (patient admission) message should parse and
    be accessible.
    """
    msg_text = (
        "MSH|^~\\&|NES|NINTENDO|AGNEW|CORNERCUBICLE|20010101000000||ADT^A01|Q123456789T123456789X123456|P|2.3\r"
        "PID|1||123456789|0123456789^AA^^JP|BROS^MARIO^^^^||19850101000000|M|||123 FAKE STREET^MARIO^^TOADSTOOL KINGDOM^NES^A1B2C3^JP^HOME^^1234|1234|(555)555-0123^HOME^JP:1234567|||S|MSH|12345678|||||||0|||||N\r"
    )

    msg = decode_er7(msg_text)

    # Message should parse successfully
    assert msg.MSH is not None
    assert msg.PID is not None
    assert msg.MSH.msh_9 == "ADT^A01" or "ADT" in str(msg.MSH.msh_9)


def test_parse_adu_a01_message_with_multiple_segments() -> None:
    """Messages with multiple standard segments should parse.

    When a message contains multiple segments in sequence, all should
    be parsed and accessible.
    """
    msg_text = (
        "MSH|^~\\&|NES|NINTENDO|AGNEW|CORNERCUBICLE|20010101000000||ADT^A01|Q123456789T123456789X123456|P|2.3\r"
        "EVN|A01|20010101000000|||^KOOPA^BOWSER^^^^^^^CURRENT\r"
        "PID|1||123456789|0123456789^AA^^JP|BROS^MARIO^^^^||19850101000000|M|||123 FAKE STREET^MARIO^^TOADSTOOL KINGDOM^NES^A1B2C3^JP^HOME^^1234|1234|(555)555-0123^HOME^JP:1234567|||S|MSH|12345678|||||||0|||||N\r"
    )

    msg = decode_er7(msg_text)

    # All segments should be accessible
    assert msg.MSH is not None
    assert msg.EVN is not None
    assert msg.PID is not None


def test_roundtrip_message_encoding() -> None:
    """Messages should survive roundtrip parsing and encoding.

    When a message is parsed from ER7 and re-encoded, the structure
    should be preserved with key segments and fields intact.
    """
    msg_text = (
        "MSH|^~\\&|NES|NINTENDO|AGNEW|CORNERCUBICLE|20010101000000||ADT^A01|Q123456789T123456789X123456|P|2.3\r"
        "PID|1||123456789|0123456789^AA^^JP|BROS^MARIO^^^^||19850101000000|M|||123 FAKE STREET^MARIO^^TOADSTOOL KINGDOM^NES^A1B2C3^JP^HOME^^1234|1234|(555)555-0123^HOME^JP:1234567|||S|MSH|12345678|||||||0|||||N\r"
    )

    msg = decode_er7(msg_text)

    # Re-encode the message
    encoded = msg.model_dump_er7()

    # Should contain key segments
    assert "MSH|" in encoded
    assert "PID|" in encoded


def test_message_field_preservation() -> None:
    """Re-encoding a parsed message should preserve field values.

    When a message is parsed and re-encoded, the essential fields
    should maintain their values through the round-trip.
    """
    msg_text = (
        "MSH|^~\\&|NES|NINTENDO|AGNEW|CORNERCUBICLE|20010101000000||ADT^A01|Q123456789T123456789X123456|P|2.3\r"
        "PID|1||123456789|0123456789^AA^^JP|BROS^MARIO^^^^||19850101000000|M||||||||||||||||||N\r"
    )

    msg = decode_er7(msg_text)
    encoded = msg.model_dump_er7()

    # Re-parse the encoded message
    msg2 = decode_er7(encoded)

    # Verify key fields are preserved
    assert msg.MSH.msh_10 == msg2.MSH.msh_10

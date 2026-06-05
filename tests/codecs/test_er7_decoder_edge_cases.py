"""Behavioural tests for ER7 decoding edge cases."""

from __future__ import annotations

import pytest

from hl7types import decode_er7
from hl7types.codecs.er7.decoder import _unescape, decode_er7_segment
from hl7types.codecs.er7.encoder import DEFAULT_ENCODING, EncodingChars


def test_decode_rejects_message_without_msh_segment() -> None:
    with pytest.raises(ValueError, match="No MSH segment"):
        decode_er7("PID|1||123456\r")


def test_decode_rejects_empty_message_type() -> None:
    with pytest.raises(ValueError, match="MSH.9 is empty"):
        decode_er7("MSH|^~\\&|A|B|C|D|20010101||" + "|" * 3 + "2.3\r")


def test_decode_rejects_empty_version_id() -> None:
    with pytest.raises(ValueError, match="MSH.12 is empty"):
        decode_er7("MSH|^~\\&|A|B|C|D|20010101||ADT^A01|CTRL|P\r")


def test_decode_rejects_unknown_message_structure() -> None:
    with pytest.raises(ValueError, match="Unknown message structure 'UNKNOWN'"):
        decode_er7("MSH|^~\\&|A|B|C|D|20010101||UNKNOWN|CTRL|P|2.3\r")


def test_decode_segment_accepts_non_standard_field_separator() -> None:
    from hl7types.hl7.v2_3.segments.MSH import MSH

    segment = "MSH!^~\\&!SEND!RECV!REC!DEST!20010101000000!!ADT^A01!CTRL!P!2.3"

    result = decode_er7_segment(
        segment,
        MSH,
        EncodingChars(field="!"),
    )

    assert result.msh_1 == "!"
    assert result.msh_2 == "^~\\&"
    assert result.msh_3.hd_1 == "SEND"  # type: ignore[union-attr]
    assert result.msh_9 == "ADT^A01"
    assert result.msh_10 == "CTRL"
    assert result.msh_12 == "2.3"


def test_decode_drops_empty_trailing_repetition() -> None:
    msg = decode_er7(
        "MSH|^~\\&|NES|NINTENDO|AGNEW|CC|20010101000000||ADT^A01|Q1|P|2.3\r"
        "EVN|A01|20010101000000\r"
        "PID|1||123~456~||DOE^JOHN\r"
        "PV1|1|I\r"
    )

    assert msg.PID is not None

    identifiers = msg.PID.pid_3
    assert identifiers is not None
    assert [identifier.cx_1 for identifier in identifiers] == ["123", "456"]


def test_decode_preserves_subcomponent_separator_inside_scalar_component() -> None:
    msg = decode_er7(
        "MSH|^~\\&|APP^FACILITY&NAMESPACE^ISO|B|C|D|20010101||ADT^A01|Q1|P|2.3\r"
        "EVN|A01|20010101\r"
        "PID|1||123456||DOE^JOHN\r"
        "PV1|1|I\r"
    )

    assert msg.MSH.msh_3.hd_1 == "APP"  # type: ignore[union-attr]
    assert msg.MSH.msh_3.hd_2 == "FACILITY&NAMESPACE"  # type: ignore[union-attr]
    assert msg.MSH.msh_3.hd_3 == "ISO"  # type: ignore[union-attr]


def test_decode_composite_datatype_inside_segment() -> None:
    from hl7types.hl7.v2_3.segments.PID import PID

    # PID.15 is CE in HL7 v2.3: identifier^text^coding-system.
    # Fields 1 and 5 (required name) are supplied; 2-4 and 6-14 are empty.
    segment = "PID|1||||DOE^JOHN||||||||||ENG^English^ISO639"

    result = decode_er7_segment(segment, PID)
    language = result.pid_15  # type: ignore[union-attr]

    assert language is not None
    assert language.ce_1 == "ENG"
    assert language.ce_2 == "English"
    assert language.ce_3 == "ISO639"


@pytest.mark.parametrize(
    ("segment_separator", "wire"),
    [
        (
            "\r",
            "MSH|^~\\&|NES|NINTENDO|AGNEW|CC|20010101000000||ADT^A01|Q1|P|2.3\r"
            "EVN|A01|20010101000000\r"
            "PID|1||123456789||DOE^JOHN\r"
            "PV1|1|I",
        ),
        (
            "\n",
            "MSH|^~\\&|NES|NINTENDO|AGNEW|CC|20010101000000||ADT^A01|Q1|P|2.3\n"
            "EVN|A01|20010101000000\n"
            "PID|1||123456789||DOE^JOHN\n"
            "PV1|1|I",
        ),
        (
            "\r\n",
            "MSH|^~\\&|NES|NINTENDO|AGNEW|CC|20010101000000||ADT^A01|Q1|P|2.3\r\n"
            "EVN|A01|20010101000000\r\n"
            "PID|1||123456789||DOE^JOHN\r\n"
            "PV1|1|I",
        ),
        (
            "\x1c",
            "MSH|^~\\&|NES|NINTENDO|AGNEW|CC|20010101000000||ADT^A01|Q1|P|2.3\x1c"
            "EVN|A01|20010101000000\x1c"
            "PID|1||123456789||DOE^JOHN\x1c"
            "PV1|1|I",
        ),
    ],
)
def test_decode_accepts_configured_segment_separator(
    segment_separator: str,
    wire: str,
) -> None:
    from hl7types.hl7.v2_3.messages.ADT_A01 import ADT_A01

    msg = decode_er7(wire, msg_cls=ADT_A01, segment_separator=segment_separator)

    assert isinstance(msg, ADT_A01)
    assert msg.MSH.msh_10 == "Q1"  # type: ignore[union-attr]
    assert msg.PID.pid_3[0].cx_1 == "123456789"  # type: ignore[index, union-attr]
    assert msg.PID.pid_5.xpn_1 == "DOE"  # type: ignore[union-attr]
    assert msg.PID.pid_5.xpn_2 == "JOHN"  # type: ignore[union-attr]
    assert msg.PV1.pv1_2 == "I"  # type: ignore[union-attr]


def test_decode_uses_custom_segment_separator_when_resolving_message_class() -> None:
    from hl7types.hl7.v2_1.messages.ADR_A19 import ADR_A19

    wire = (
        "MSH|^~\\&|||||202001010000||ADR^A19|1|P|2.1\x1c"
        "MSA|AA|1\x1c"
        "QRD|20200101000000|R|I|1^^^|1|1^RD|DEM|123456789|RES|ALL\x1c"
        "PID|1||123456789||DOE^JOHN\x1c"
        "PV1|1|I|WARD^ROOM^BED"
    )

    msg = decode_er7(wire, segment_separator="\x1c")

    assert isinstance(msg, ADR_A19)
    assert msg.MSH.msh_10 == "1"  # type: ignore[union-attr]


def test_decode_accepts_explicit_message_class() -> None:
    from hl7types.hl7.v2_3.messages.ADT_A01 import ADT_A01

    wire = (
        "MSH|^~\\&|NES|NINTENDO|AGNEW|CC|20010101000000||ADT^A01|Q1|P|2.3\r"
        "EVN|A01|20010101000000\r"
        "PID|1||123456789||DOE^JOHN\r"
        "PV1|1|I\r"
    )

    msg = decode_er7(wire, msg_cls=ADT_A01)

    assert isinstance(msg, ADT_A01)
    assert msg.MSH.msh_10 == "Q1"  # type: ignore[union-attr]


def test_unescape_replaces_hl7_delimiter_escape_sequences() -> None:
    raw = r"a\F\b\S\c\T\d\R\e\E\f"

    assert _unescape(raw, DEFAULT_ENCODING) == "a|b^c&d~e\\f"

"""Tests for HL7 v2.7+ truncation character support."""
from __future__ import annotations

import pytest

from hl7types import decode_er7
from hl7types.codecs.er7.encoder import EncodingChars


# v2.7 wire with ^~\&# in MSH.2 and a truncated value in PID.5
TRUNCATION_WIRE = (
    r"MSH|^~\&#|SendApp|SendFac|RecApp|RecFac|20240101120000||ADT^A01^ADT_A01|MSG001|P|2.7" + "\r"
    "EVN|A01|20240101120000\r"
    "PID|1||MRN001^^^HospA^MR||Smith#\r"
    "PV1|1|I\r"
)

# Same structure but declared as v2.5 - truncation char must be rejected
TRUNCATION_WIRE_PRE_27 = (
    r"MSH|^~\&#|SendApp|SendFac|RecApp|RecFac|20240101120000||ADT^A01^ADT_A01|MSG001|P|2.5" + "\r"
    "EVN|A01|20240101120000\r"
    "PID|1||MRN001^^^HospA^MR||Smith#\r"
    "PV1|1|I\r"
)


class TestEncodingCharsFromMsh2:
    def test_five_char_msh2_accepted_for_v27(self) -> None:
        enc = EncodingChars.from_msh2("^~\\&#", "2.7")
        assert enc.truncation == "#"

    def test_five_char_msh2_accepted_for_v28(self) -> None:
        enc = EncodingChars.from_msh2("^~\\&#", "2.8.2")
        assert enc.truncation == "#"

    def test_five_char_msh2_rejected_below_v27(self) -> None:
        with pytest.raises(ValueError, match="v2.7"):
            EncodingChars.from_msh2("^~\\&#", "2.5")

    def test_five_char_msh2_rejected_for_v26(self) -> None:
        with pytest.raises(ValueError, match="v2.7"):
            EncodingChars.from_msh2("^~\\&#", "2.6")

    def test_five_char_msh2_rejected_with_no_version(self) -> None:
        with pytest.raises(ValueError, match="v2.7"):
            EncodingChars.from_msh2("^~\\&#")

    def test_four_char_msh2_has_no_truncation(self) -> None:
        enc = EncodingChars.from_msh2("^~\\&", "2.7")
        assert enc.truncation == ""

    def test_six_char_msh2_raises(self) -> None:
        with pytest.raises(ValueError):
            EncodingChars.from_msh2("^~\\&##", "2.7")


class TestTruncationDecoding:
    def test_truncation_char_stripped_from_field_value(self) -> None:
        msg = decode_er7(TRUNCATION_WIRE)
        # PID.5 family name should have trailing # stripped
        pid = msg.PID  # type: ignore[union-attr]
        assert pid.pid_5[0].xpn_1.fn_1 == "Smith"

    def test_truncation_wire_below_v27_raises(self) -> None:
        with pytest.raises(ValueError, match="v2.7"):
            decode_er7(TRUNCATION_WIRE_PRE_27)


class TestTruncationEncoding:
    def test_truncation_char_included_in_msh2_on_roundtrip(self) -> None:
        msg = decode_er7(TRUNCATION_WIRE)
        wire = msg.model_dump_er7()
        msh_line = wire.split("\r")[0]
        # MSH.2 is the second field - should contain the truncation char
        msh2 = msh_line.split("|")[1]
        assert msh2 == "^~\\&#"

    def test_truncation_char_escaped_in_field_values(self) -> None:
        enc = EncodingChars(truncation="#")
        from hl7types.codecs.er7.encoder import _escape
        assert _escape("foo#bar", enc) == "foo\\Z\\bar"

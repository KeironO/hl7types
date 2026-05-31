"""Tests targeting uncovered branches in the ER7 decoder."""
from __future__ import annotations

import pytest

from hl7types import decode_er7
from hl7types.codecs.er7.decoder import (
    _split_segments,
    _unescape,
    decode_er7_segment,
    is_segment_cls,
)
from hl7types.codecs.er7.encoder import DEFAULT_ENCODING, EncodingChars


# _resolve_msg_cls error paths


def test_decode_er7_raises_when_no_msh() -> None:
    with pytest.raises(ValueError, match="No MSH segment"):
        decode_er7("PID|1||123456\r")


def test_decode_er7_raises_when_msh9_empty() -> None:
    with pytest.raises(ValueError, match="MSH.9 is empty"):
        decode_er7("MSH|^~\\&|A|B|C|D|20010101||" + "|" * 3 + "2.3\r")


def test_decode_er7_raises_when_msh12_empty() -> None:
    with pytest.raises(ValueError, match="MSH.12 is empty"):
        decode_er7("MSH|^~\\&|A|B|C|D|20010101||ADT^A01|CTRL|P\r")


def test_decode_er7_msh9_unknown_structure_raises() -> None:
    with pytest.raises((ModuleNotFoundError, ValueError)):
        decode_er7("MSH|^~\\&|A|B|C|D|20010101||UNKNOWN|CTRL|P|2.3\r")


# Non-standard field separator


def test_decode_er7_segment_non_standard_field_sep() -> None:
    from hl7types.hl7.v2_3.segments.MSH import MSH

    seg_str = "MSH!^~\\&!SEND!RECV!REC!DEST!20010101000000!!ADT^A01!CTRL!P!2.3"
    enc = EncodingChars(field="!")
    result = decode_er7_segment(seg_str, MSH, enc)
    assert result.msh_3.hd_1 == "SEND"  # type: ignore[union-attr]


# _parse_rep / _parse_field edge cases


def test_empty_repetition_skipped() -> None:
    # Trailing repetition separator the empty rep should be dropped
    msg = decode_er7(
        "MSH|^~\\&|NES|NINTENDO|AGNEW|CC|20010101000000||ADT^A01|Q1|P|2.3\r"
        "EVN|A01|20010101000000\r"
        "PID|1||123~||\r"
    )
    assert msg.PID is not None
    pid3 = msg.PID.pid_3
    assert pid3 is not None
    assert all(cx.cx_1 for cx in pid3)


# Subcomponent parsing


def test_scalar_component_preserves_subcomponent_separator() -> None:
    # hd_2 is a scalar string, so the & inside FACILITY&NAMESPACE is not split —
    # the whole value is preserved verbatim, including the subcomponent character.
    msg = decode_er7(
        "MSH|^~\\&|APP^FACILITY&NAMESPACE^ISO|B|C|D|20010101||ADT^A01|Q1|P|2.3\r"
        "EVN|A01|20010101\r"
        "PID|1\r"
    )
    assert msg.MSH.msh_3.hd_1 == "APP"  # type: ignore[union-attr]
    assert msg.MSH.msh_3.hd_2 == "FACILITY&NAMESPACE"  # type: ignore[union-attr]


# is_segment_cls correctly classifies segments and datatypes


def test_datatype_is_not_segment() -> None:
    from hl7types.hl7.v2_3.datatypes.CE import CE

    assert not is_segment_cls(CE)


def test_segment_is_segment() -> None:
    from hl7types.hl7.v2_3.segments.BTS import BTS

    assert is_segment_cls(BTS)


def test_ce_datatype_decodes_correctly_inside_segment() -> None:
    # Regression: is_segment_cls(CE) returning True would break composite parsing
    # because _parse_rep dispatches on _is_model, not is_segment_cls, but a future
    # helper using is_segment_cls as a general classifier must not misfire on datatypes.
    # This test confirms CE fields round-trip through decode_er7_segment correctly.
    from hl7types.hl7.v2_3.segments.PID import PID

    # PID.15 is CE (primary language): identifier^text^coding-system
    # PID|field1(1)|...|field14(14)|CE-field(15)
    seg_str = "PID|1" + "|" * 13 + "|ENG^English^ISO639"
    result = decode_er7_segment(seg_str, PID)
    lang = result.pid_15  # type: ignore[union-attr]
    assert lang is not None
    assert lang.ce_1 == "ENG"
    assert lang.ce_2 == "English"
    assert lang.ce_3 == "ISO639"


# _split_segments: standard CR/LF variants and custom separators


def test_split_segments_cr() -> None:
    assert _split_segments("MSH|^~\\&\rMSA|AA|1", "\r") == ["MSH|^~\\&", "MSA|AA|1"]


def test_split_segments_lf() -> None:
    assert _split_segments("MSH|^~\\&\nMSA|AA|1", "\n") == ["MSH|^~\\&", "MSA|AA|1"]


def test_split_segments_crlf() -> None:
    assert _split_segments("MSH|^~\\&\r\nMSA|AA|1", "\r\n") == ["MSH|^~\\&", "MSA|AA|1"]


def test_split_segments_custom() -> None:
    assert _split_segments("MSH|^~\\&\x1cMSA|AA|1", "\x1c") == ["MSH|^~\\&", "MSA|AA|1"]


# Custom separator used consistently for both segmentation and auto-resolution


def test_auto_resolve_uses_custom_segment_separator() -> None:
    from hl7types.hl7.v2_1.messages.ADR_A19 import ADR_A19

    wire = (
        "MSH|^~\\&|||||202001010000||ADR^A19|1|P|2.1\x1c"
        "MSA|AA|1\x1c"
        "QRD|20200101000000|R|I|1^^^|1|1^RD|PID\x1c"
        "PID|1\x1c"
        "PV1|1|I"
    )
    msg = decode_er7(wire, segment_separator="\x1c")
    assert isinstance(msg, ADR_A19)


# Custom segment separator is honoured consistently (explicit msg_cls)


def test_custom_segment_separator_is_honoured() -> None:
    from hl7types.hl7.v2_3.messages.ADT_A01 import ADT_A01

    wire = (
        "MSH|^~\\&|NES|NINTENDO|AGNEW|CC|20010101000000||ADT^A01|Q1|P|2.3\x1c"
        "EVN|A01|20010101000000\x1c"
        "PID|1||123456789"
    )
    msg = decode_er7(wire, msg_cls=ADT_A01, segment_separator="\x1c")
    assert msg.MSH.msh_10 == "Q1"  # type: ignore[union-attr]


# _unescape handles all five delimiter escape sequences


def test_unescape_all_delimiter_escapes() -> None:
    raw = r"a\F\b\S\c\T\d\R\e\E\f"
    assert _unescape(raw, DEFAULT_ENCODING) == "a|b^c&d~e\\f"


# decode_er7 with explicit msg_cls

def test_decode_er7_explicit_msg_cls() -> None:
    from hl7types.hl7.v2_3.messages.ADT_A01 import ADT_A01

    msg_text = (
        "MSH|^~\\&|NES|NINTENDO|AGNEW|CC|20010101000000||ADT^A01|Q1|P|2.3\r"
        "EVN|A01|20010101000000\r"
        "PID|1||123456789\r"
    )
    msg = decode_er7(msg_text, msg_cls=ADT_A01)
    assert isinstance(msg, ADT_A01)
    assert msg.MSH.msh_10 == "Q1"

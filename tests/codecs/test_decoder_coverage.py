"""Tests targeting uncovered branches in the ER7 decoder."""
from __future__ import annotations

import pytest

from hl7types import decode_er7
from hl7types.codecs.er7.decoder import decode_er7_segment
from hl7types.codecs.er7.encoder import EncodingChars


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


def test_decode_er7_msh9_single_component_fallback() -> None:
    # MSH.9 with no caret single-component path, no matching module exists
    with pytest.raises((ModuleNotFoundError, AttributeError)):
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


def test_subcomponent_field_parsed() -> None:
    # HD.2 is a plain string but sits next to a subcomponent-bearing field
    msg = decode_er7(
        "MSH|^~\\&|APP^FACILITY&NAMESPACE^ISO|B|C|D|20010101||ADT^A01|Q1|P|2.3\r"
        "EVN|A01|20010101\r"
        "PID|1\r"
    )
    assert msg.MSH.msh_3.hd_1 == "APP"  # type: ignore[union-attr]
    assert msg.MSH.msh_3.hd_2 == "FACILITY&NAMESPACE"  # type: ignore[union-attr]


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

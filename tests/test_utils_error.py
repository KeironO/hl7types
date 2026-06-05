"""Tests for hl7types.utils.error ; ERR segment generation from ValidationErrors."""
from __future__ import annotations

import pytest
from pydantic import ValidationError

from hl7types.utils.error import (
    _error_code_from_pydantic_error,
    _segment_and_field_from_loc,
    err_from_pydantic_error,
    errs_from_exception,
)


def _missing_msh_error() -> dict:
    """Return a single 'missing' ValidationError dict with loc ('msh_7',)."""
    from hl7types.hl7.v2_5_1.segments.MSH import MSH
    try:
        MSH.model_validate({"msh_1": "|"})
    except ValidationError as e:
        return e.errors()[0]
    raise AssertionError("expected ValidationError")


def _missing_msh_exc() -> ValidationError:
    from hl7types.hl7.v2_5_1.segments.MSH import MSH
    try:
        MSH.model_validate({"msh_1": "|"})
    except ValidationError as e:
        return e
    raise AssertionError("expected ValidationError")


@pytest.mark.parametrize("error_type,expected", [
    ("missing", "101"),
    ("string_too_long", "104"),
    ("too_long", "104"),
    ("int_parsing", "102"),
    ("float_parsing", "102"),
    ("bool_parsing", "102"),
    ("date_parsing", "102"),
    ("datetime_parsing", "102"),
    ("time_parsing", "102"),
    ("string_type", "102"),
    ("int_type", "102"),
    ("float_type", "102"),
    ("bool_type", "102"),
    ("date_type", "102"),
    ("datetime_type", "102"),
    ("time_type", "102"),
    ("unknown_type", "199"),
])
def test_error_code_from_type(error_type: str, expected: str):
    assert _error_code_from_pydantic_error({"type": error_type, "msg": ""}) == expected


@pytest.mark.parametrize("msg,expected", [
    ("Not in table XYZ", "103"),
    ("valid HL7 datetime required", "102"),
    ("valid HL7 date required", "102"),
    ("valid HL7 time required", "102"),
    ("wrong data type supplied", "102"),
])
def test_error_code_from_message_text(msg: str, expected: str):
    assert _error_code_from_pydantic_error({"type": "value_error", "msg": msg}) == expected


def test_loc_empty_returns_none():
    assert _segment_and_field_from_loc(()) == (None, None)


def test_loc_segment_field_parsed():
    seg, field = _segment_and_field_from_loc(("msh_9",))
    assert seg == "MSH"
    assert field == 9


def test_loc_segment_uppercased():
    seg, _ = _segment_and_field_from_loc(("pid_3",))
    assert seg == "PID"


def test_loc_multi_digit_field():
    _, field = _segment_and_field_from_loc(("msh_12",))
    assert field == 12


def test_loc_non_matching_returns_none():
    assert _segment_and_field_from_loc(("MSA",)) == (None, None)


@pytest.mark.parametrize("version", ["2.1", "2.2"])
def test_err_v2_1_v2_2_err1_contains_code_and_field(version: str):
    error = _missing_msh_error()
    seg = err_from_pydantic_error(error, version)
    assert seg.err_1[0] == "101"
    assert seg.err_1[1] == "7"


@pytest.mark.parametrize("version", ["2.3.1", "2.4"])
def test_err_v2_3_1_v2_4_eld_structure(version: str):
    error = _missing_msh_error()
    seg = err_from_pydantic_error(error, version)
    eld = seg.err_1[0]
    assert eld.eld_1 == "MSH"
    assert eld.eld_2 == "1"
    assert eld.eld_3 == "7"
    assert eld.eld_4.ce_1 == "101"
    assert eld.eld_4.ce_2 == "Required field missing"
    assert eld.eld_4.ce_3 == "HL70060"

@pytest.mark.parametrize("version", ["2.5.1", "2.6", "2.7", "2.8", "2.8.2"])
def test_err_v2_5_1_plus_structure(version: str):
    error = _missing_msh_error()
    seg = err_from_pydantic_error(error, version)

    assert seg.err_4 == "E"

    assert seg.err_3.cwe_1 == "101"
    assert seg.err_3.cwe_2 == "Required field missing"
    assert seg.err_3.cwe_3 == "HL70357"

    erl = seg.err_2[0]
    assert erl.erl_1 == "MSH"
    assert erl.erl_2 == "1"
    assert erl.erl_3 == "7"

def test_errs_from_exception_returns_one_err_per_violated_field():
    errs = errs_from_exception(_missing_msh_exc(), "2.5.1")
    assert len(errs) >= 1


def test_errs_from_exception_non_validation_error_returns_empty():
    assert errs_from_exception(ValueError("bad"), "2.5.1") == []
    assert errs_from_exception(RuntimeError("boom"), "2.5.1") == []


def test_errs_from_exception_all_have_severity_e():
    errs = errs_from_exception(_missing_msh_exc(), "2.8.2")
    assert all(e.err_4 == "E" for e in errs)


def test_err_from_pydantic_error_unknown_version_raises():
    with pytest.raises(ValueError, match="ERR segment not found"):
        err_from_pydantic_error({"type": "missing", "msg": "", "loc": ("msh_9",)}, "9.9.9")



def test_nak_construction_from_decode_error():
    from hl7types import decode_er7
    from hl7types.hl7.v2_8_2.messages.ACK import ACK
    from hl7types.hl7.v2_8_2.segments.MSA import MSA
    from hl7types.hl7.v2_8_2.segments.MSH import MSH
    from hl7types.hl7.v2_8_2.datatypes.HD import HD
    from hl7types.hl7.v2_8_2.datatypes.MSG import MSG
    from hl7types.hl7.v2_8_2.datatypes.PT import PT
    from hl7types.hl7.v2_8_2.datatypes.VID import VID

    # ACK wire deliberately missing MSA to trigger a ValidationError
    wire = "MSH|^~\\&|SEND|FAC|RECV|FAC|20240101120000||ACK|MSG001|P|2.8.2\r"

    try:
        decode_er7(wire, msg_cls=ACK, strict=True)
        pytest.fail("expected ValidationError")
    except Exception as exc:
        errs = errs_from_exception(exc, "2.8.2")

    assert len(errs) >= 1

    msh = MSH(
        msh_3=HD(hd_1="RECV"),
        msh_5=HD(hd_1="SEND"),
        msh_7="20240101120000",
        msh_9=MSG(msg_1="ACK", msg_2="A01", msg_3="ACK"),
        msh_10="MSG002",
        msh_11=PT(pt_1="P"),
        msh_12=VID(vid_1="2.8.2"),
    )
    msa = MSA(msa_1="AE", msa_2="MSG001")
    nak = ACK(MSH=msh, MSA=msa, ERR=errs)

    er7 = nak.model_dump_er7()
    assert "AE" in er7
    assert "ERR|" in er7

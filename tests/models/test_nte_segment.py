"""Tests for the generated NTE segment model (hl7types.hl7.v2_1.segments.NTE).

Covers runtime behaviour: nte_3 as an optional list of plain strings, population
by Python field name / HL7 dot-notation alias, serialisation with aliases, and
ER7 decoding.
"""
from __future__ import annotations

import pytest
import pydantic

from hl7types import decode_er7
from hl7types.hl7.v2_1.segments.NTE import NTE

# OBR with all required v2.1 fields present (positions 4, 7, 8, 9, 14, 22).
_OBR = "|".join([
    "OBR", "1", "", "", "CBC^CBC", "", "",
    "19950101090000", "19950101090000", "19950101090000",
    "", "", "", "", "19950101100000",
    "", "", "", "", "", "", "",
    "19950101110000",
])
assert _OBR.split("|")[0] == "OBR"
assert len(_OBR.split("|")) >= 23

_ORU_R01_WITH_NTE = (
    "MSH|^~\\&|APP|FAC|APP2|FAC2|19950101120000||ORU^R01|MSG001|P|2.1\r"
    "PID|1||P001||DOE^JOHN||19800101|M\r"
    + _OBR + "\r"
    "NTE|1||Fasting sample\r"
    "OBX|1|ST|WBC^White Blood Cell||5.0|10*3/uL|4.0-11.0|N|||F\r"
)


def _decoded_nte() -> NTE:
    """Return the first NTE segment from a decoded ORU^R01 message."""
    msg = decode_er7(_ORU_R01_WITH_NTE)
    nte_list = msg.PATIENT_RESULT[0].ORDER_OBSERVATION[0].NTE
    assert isinstance(nte_list, list)
    assert nte_list
    assert isinstance(nte_list[0], NTE)
    return nte_list[0]


def test_direct_construction_single_comment_succeeds() -> None:
    """NTE(nte_3=['Fasting sample']) constructs successfully."""
    nte = NTE(nte_3=["Fasting sample"])
    assert nte.nte_3 == ["Fasting sample"]


def test_direct_construction_multiple_comments_succeeds() -> None:
    """NTE(nte_3=[...]) accepts more than one string."""
    nte = NTE(nte_3=["First comment", "Second comment"])
    assert nte.nte_3 == ["First comment", "Second comment"]


def test_nte_3_is_a_list() -> None:
    """nte_3 is a list when supplied."""
    nte = NTE(nte_3=["Fasting sample"])
    assert isinstance(nte.nte_3, list)


def test_nte_3_items_are_plain_strings() -> None:
    """Every item in nte_3 is a plain str, not a generated datatype object."""
    nte = NTE(nte_3=["Fasting sample", "Second note"])
    for item in nte.nte_3:
        assert type(item) is str


def test_direct_construction_without_nte_3_succeeds() -> None:
    """Omitting nte_3 succeeds; the field defaults to None."""
    nte = NTE()
    assert nte.nte_3 is None


def test_direct_construction_with_empty_nte_3_succeeds() -> None:
    """Supplying nte_3=[] succeeds; the field is optional in the generated model."""
    nte = NTE(nte_3=[])
    assert nte.nte_3 == []


def test_direct_construction_by_hl7_dot_notation() -> None:
    """nte_3 can be set via the 'NTE.3' HL7 dot-notation key in a dict unpack."""
    nte = NTE(**{"NTE.3": ["Fasting sample"]})
    assert nte.nte_3 == ["Fasting sample"]


def test_model_dump_by_alias_contains_nte_3_key() -> None:
    """model_dump(by_alias=True) serialises nte_3 under the key 'NTE.3'."""
    nte = NTE(nte_3=["Fasting sample"])
    dump = nte.model_dump(by_alias=True)
    assert "NTE.3" in dump


def test_model_dump_by_alias_nte_3_value() -> None:
    """model_dump(by_alias=True) preserves the nte_3 value under key 'NTE.3'."""
    nte = NTE(nte_3=["Fasting sample"])
    assert nte.model_dump(by_alias=True)["NTE.3"] == ["Fasting sample"]


def test_decoded_nte_3_is_populated_list() -> None:
    """Decoding a message with NTE produces a populated nte_3 list."""
    nte = _decoded_nte()
    assert isinstance(nte.nte_3, list)
    assert len(nte.nte_3) >= 1


def test_decoded_nte_3_items_are_plain_strings() -> None:
    """Items in a decoded nte_3 list are plain str instances."""
    nte = _decoded_nte()
    for item in nte.nte_3:
        assert type(item) is str


def test_decoded_nte_3_contains_expected_text() -> None:
    """The decoded nte_3 list contains the comment text from the ER7 message."""
    nte = _decoded_nte()
    assert "Fasting sample" in nte.nte_3

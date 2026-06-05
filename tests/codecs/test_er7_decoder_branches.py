"""ER7 decoder: type-unwrapping rules, position-map filtering, empty-field handling,
lenient-mode placeholder injection, and non-standard delimiter auto-detection.
Private helpers are tested where the equivalent behaviour cannot easily be driven
through the public decode_er7 / decode_er7_segment APIs."""
from __future__ import annotations

import typing
from typing import List

import pytest
from pydantic import AliasChoices, BaseModel, Field, ValidationError

from hl7types import decode_er7
from hl7types.codecs.er7.decoder import (
    _build_pos_map,
    _is_model,
    _parse_field,
    _parse_rep,
    _unwrap,
    decode_er7_segment,
    is_segment_cls,
)
from hl7types.codecs.er7.encoder import DEFAULT_ENCODING
from hl7types.hl7 import HL7Model
from hl7types.hl7.v2_5_1.segments.MSA import MSA
from hl7types.hl7.v2_5_1.segments.MSH import MSH

# Field name MSH/MSA would shadow the imported type under PEP 649 lazy annotations;
# aliasing avoids that.  Models must live at module scope for get_type_hints.
_MSH = MSH
_MSA = MSA


class _MsgWithScalar(BaseModel):
    MSH: _MSH
    MSA: _MSA
    tag: str = "default"


class _MsgWithRequiredScalar(BaseModel):
    MSH: _MSH
    required_tag: str  # required, no default ; decoder cannot fill scalar fields


class _SegWithRequiredList(HL7Model):
    sl_1: str = Field(
        default=...,
        validation_alias=AliasChoices("sl_1", "SL.1"),
        serialization_alias="SL.1",
    )
    sl_2: List[str] = Field(
        default=...,
        validation_alias=AliasChoices("sl_2", "SL.2"),
        serialization_alias="SL.2",
    )
    model_config = {"populate_by_name": True}


def test_unwrap_union_with_multiple_non_none_types_returns_original():
    ann = typing.Union[str, int]
    result, is_list = _unwrap(ann)
    assert is_list is False
    assert result is ann


def test_unwrap_list_of_optional_unwraps_to_inner_type():
    inner, is_list = _unwrap(typing.List[typing.Optional[str]])
    assert inner is str
    assert is_list is True


def test_is_model_returns_false_for_non_class():
    assert _is_model("not a class") is False


def test_is_segment_cls_returns_false_for_non_model_types():
    assert is_segment_cls(str) is False
    assert is_segment_cls(42) is False


def test_build_pos_map_skips_fields_with_no_serialization_alias():
    # Group models store segment references without dotted numeric aliases,
    # so the pos map should be empty.
    from hl7types.hl7.v2_5_1.groups.ADT_A01_PROCEDURE import ADT_A01_PROCEDURE

    result = _build_pos_map(ADT_A01_PROCEDURE)
    assert result == {}


def test_build_pos_map_skips_non_dotted_string_alias():
    class WeirdAliasModel(BaseModel):
        x: str = Field(default="", serialization_alias="NODOT")

    result = _build_pos_map(WeirdAliasModel)
    assert result == {}


def test_parse_rep_returns_none_for_empty_raw():
    assert _parse_rep("", str, DEFAULT_ENCODING) is None


def test_parse_rep_returns_none_for_model_with_empty_pos_map():
    from hl7types.hl7.v2_5_1.groups.ADT_A01_PROCEDURE import ADT_A01_PROCEDURE

    assert _parse_rep("PID^1^3", ADT_A01_PROCEDURE, DEFAULT_ENCODING) is None


def test_parse_field_returns_none_for_empty_raw():
    assert _parse_field("", str, False, DEFAULT_ENCODING) is None


def test_decode_er7_segment_auto_detects_non_standard_field_sep_from_wire():
    # When decode_er7_segment is called with DEFAULT_ENCODING (field="|") but the
    # wire uses "!", the segment detects the actual separator from MSH[3] and
    # switches enc automatically ; no explicit EncodingChars required.
    from hl7types.hl7.v2_3.segments.MSH import MSH as MSH23

    seg_str = "MSH!^~\\&!SEND!FAC!RECV!DEST!20010101000000!!ADT^A01!CTRL!P!2.3"
    result = decode_er7_segment(seg_str, MSH23)

    assert result.msh_1 == "!"  # type: ignore[union-attr]
    assert result.msh_2 == "^~\\&"  # type: ignore[union-attr]
    assert result.msh_3.hd_1 == "SEND"  # type: ignore[union-attr]
    assert result.msh_9 == "ADT^A01"  # type: ignore[union-attr]
    assert result.msh_10 == "CTRL"  # type: ignore[union-attr]
    assert result.msh_12 == "2.3"  # type: ignore[union-attr]


def test_decode_er7_segment_extra_fields_beyond_schema_are_ignored():
    from hl7types.hl7.v2_3.segments.MSH import MSH as MSH23

    extra = "MSH|^~\\&|A|B|C|D|20010101||ADT^A01|CTRL|P|2.3" + "|" * 10 + "EXTRA22"
    result = decode_er7_segment(extra, MSH23, strict=False)
    assert result.msh_3.hd_1 == "A"  # type: ignore[union-attr]


def test_decode_er7_segment_lenient_fills_required_list_field_with_empty():
    with pytest.warns(UserWarning, match="sl_2.*strict=False"):
        seg = decode_er7_segment("_SegWithRequiredList|value", _SegWithRequiredList, strict=False)

    assert seg.sl_1 == "value"
    assert seg.sl_2 == []


_ACK_WIRE = (
    "MSH|^~\\&|SEND|FAC|RECV|FAC|20240101||ACK|MSG001|P|2.5.1\r"
    "MSA|AA|MSG001\r"
)


def test_decode_er7_message_with_non_model_scalar_field_decodes_segments_and_keeps_default():
    # Non-model scalar fields on a message wrapper (e.g. tag: str = "default") are
    # silently skipped by the decoder; segments around them decode normally.
    msg = decode_er7(_ACK_WIRE, msg_cls=_MsgWithScalar)
    assert msg.MSH.msh_10 == "MSG001"  # type: ignore[union-attr]
    assert msg.MSA.msa_1 == "AA"  # type: ignore[union-attr]
    assert msg.tag == "default"  # type: ignore[union-attr]


def test_decode_er7_message_with_required_scalar_field_raises_validation_error():
    # Lenient mode only injects placeholders for model-type fields. A required
    # scalar field with no default cannot be filled and causes ValidationError.
    wire = "MSH|^~\\&|SEND|FAC|RECV|FAC|20240101||ACK|MSG001|P|2.5.1\r"
    with pytest.raises(ValidationError):
        decode_er7(wire, msg_cls=_MsgWithRequiredScalar, strict=False)


def test_decode_er7_raises_when_msg_cls_has_no_matching_segments():
    class EmptyMsg(BaseModel):
        pass

    wire = "MSH|^~\\&|A|B|C|D|20010101||ACK|001|P|2.3\rMSA|AA|001\r"
    with pytest.raises(ValueError, match="Could not decode"):
        decode_er7(wire, msg_cls=EmptyMsg)

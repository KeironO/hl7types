"""ER7 encoder: encoding-character inference, composite/subcomposite serialisation,
and segment-collection logic. Private helpers are tested where the equivalent
behaviour cannot easily be driven through the public encode_er7 / encode_er7_segment
APIs."""

from __future__ import annotations

from pydantic import BaseModel

from hl7types.codecs.er7.encoder import (
    DEFAULT_ENCODING,
    EncodingChars,
    _collect_segments,
    _encode_composite,
    _encode_subcomposite,
    _encode_value,
    _pos,
    encode_er7,
    encode_er7_segment,
)
from hl7types.hl7.v2_5_1.segments.MSA import MSA


def test_pos_returns_none_when_alias_has_no_dot() -> None:
    assert _pos("NODOT") is None


def test_pos_returns_none_when_alias_suffix_is_not_numeric() -> None:
    assert _pos("FOO.bar") is None


def test_encode_subcomposite_returns_empty_string_for_empty_dict() -> None:
    assert _encode_subcomposite({}, DEFAULT_ENCODING) == ""


def test_encode_composite_returns_empty_string_for_empty_dict() -> None:
    assert _encode_composite({}, DEFAULT_ENCODING) == ""


def test_encode_composite_treats_numeric_component_as_empty() -> None:
    # _encode_composite only handles str and dict values; non-string scalars
    # (which model_dump never emits for composite types) are treated as absent.
    result = _encode_composite({"FOO.1": 42}, DEFAULT_ENCODING)

    assert result == ""


def test_encode_value_returns_empty_string_for_none() -> None:
    assert _encode_value(None, DEFAULT_ENCODING) == ""


def test_encode_value_converts_integer_to_string() -> None:
    assert _encode_value(42, DEFAULT_ENCODING) == "42"


def test_encode_value_converts_float_to_string() -> None:
    assert _encode_value(3.14, DEFAULT_ENCODING) == "3.14"


def test_encode_segment_with_no_hl7_fields_returns_class_name() -> None:
    class EmptyModel(BaseModel):
        pass

    result = encode_er7_segment(EmptyModel())

    assert result == "EmptyModel"


def test_encode_msh_reconstructs_encoding_characters_when_msh2_is_missing() -> None:
    from hl7types.hl7.v2_5_1.segments.MSH import MSH

    msh = MSH.model_construct(msh_1="|", msh_2=None)

    result = encode_er7_segment(msh)

    assert result == "MSH|^~\\&"


def test_encode_msh_includes_truncation_character_in_msh2_position() -> None:
    from hl7types.hl7.v2_5_1.segments.MSH import MSH

    msh = MSH.model_construct(msh_1="|", msh_2=None)
    encoding = EncodingChars(truncation="#")

    result = encode_er7_segment(msh, encoding)

    assert result == "MSH|^~\\&#"


def test_encode_msh_with_null_message_type_does_not_render_none_literal() -> None:
    from hl7types.hl7.v2_5_1.segments.MSH import MSH

    msh = MSH.model_construct(msh_1="|", msh_2="^~\\&", msh_9=None)

    result = encode_er7_segment(msh)

    assert result.startswith("MSH|")
    assert "None" not in result


def test_encode_single_segment_returns_encoded_segment() -> None:
    result = encode_er7(MSA(msa_1="AA", msa_2="MSG001"))

    assert result == "MSA|AA|MSG001"


def test_encode_message_with_no_segments_returns_empty_string() -> None:
    class NoSegments(BaseModel):
        note: str = "hello"

    result = encode_er7(NoSegments())

    assert result == ""


def test_collect_segments_ignores_non_segment_model_fields() -> None:
    class MsgWithString(BaseModel):
        MSA: MSA
        tag: str = "ignored"

    result = _collect_segments(MsgWithString(MSA=MSA(msa_1="AA", msa_2="001")))

    assert len(result) == 1
    assert isinstance(result[0], MSA)


def test_encode_message_without_version_still_includes_known_segments() -> None:
    from hl7types.hl7.v2_5_1.messages.ACK import ACK
    from hl7types.hl7.v2_5_1.segments.MSH import MSH

    msh = MSH.model_construct(msh_1="|", msh_2="^~\\&")
    msa = MSA(msa_1="AA", msa_2="MSG001")
    message = ACK.model_construct(MSH=msh, MSA=msa)

    result = encode_er7(message)

    assert result == "MSH|^~\\&\rMSA|AA|MSG001"

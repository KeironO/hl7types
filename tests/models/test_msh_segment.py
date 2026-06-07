"""Tests for the generated MSH segment model (hl7types.hl7.v2_1.segments.MSH).

Covers runtime behaviour: hardcoded defaults for msh_1 and msh_2, required
field validation, population by Python name/human-readable alias/HL7
dot-notation alias, and serialisation with aliases.
"""
from __future__ import annotations

import pytest
import pydantic

from hl7types import decode_er7
from hl7types.hl7.v2_1.segments.MSH import MSH

_ADT_A17 = (
    "MSH|^~\\&|APP|FAC|APP2|FAC2|19950101120000||ADT^A17|MSG001|P|2.1\r"
    "EVN|A17|19950101120000\r"
    "PID|1||P001||DOE^JOHN||\r"
    "PV1|1|I|WARD1\r"
    "PID|2||P002||SMITH^JANE||\r"
    "PV1|1|I|WARD2\r"
)


def _decoded_msh() -> MSH:
    """Return the MSH segment from a decoded ADT^A17 v2.1 message."""
    msh = decode_er7(_ADT_A17).MSH
    assert isinstance(msh, MSH)
    return msh


def _required_fields() -> dict:
    """Return a dict of the required non-default MSH fields sourced from a decoded message."""
    src = _decoded_msh()
    return {
        "msh_9": src.msh_9,
        "msh_10": src.msh_10,
        "msh_11": src.msh_11,
        "msh_12": src.msh_12,
    }


def test_decoded_msh_field_separator_is_pipe() -> None:
    """A decoded MSH has msh_1 equal to the HL7 field separator '|'."""
    msh = _decoded_msh()
    assert msh.msh_1 == "|"


def test_decoded_msh_encoding_characters() -> None:
    """A decoded MSH has msh_2 equal to the standard HL7 encoding characters."""
    msh = _decoded_msh()
    assert msh.msh_2 == "^~\\&"


def test_direct_construction_msh_1_default() -> None:
    """msh_1 defaults to '|' when not supplied during direct construction."""
    msh = MSH(**_required_fields())
    assert msh.msh_1 == "|"


def test_direct_construction_msh_2_default() -> None:
    """msh_2 defaults to '^~\\&' when not supplied during direct construction."""
    msh = MSH(**_required_fields())
    assert msh.msh_2 == "^~\\&"


def test_direct_construction_override_msh_1_by_name() -> None:
    """msh_1 can be overridden by Python field name."""
    msh = MSH(msh_1="!", **_required_fields())
    assert msh.msh_1 == "!"


def test_direct_construction_override_msh_2_by_name() -> None:
    """msh_2 can be overridden by Python field name."""
    msh = MSH(msh_2="@#$%", **_required_fields())
    assert msh.msh_2 == "@#$%"


def test_direct_construction_by_field_separator_alias() -> None:
    """msh_1 can be set via the 'field_separator' human-readable alias."""
    msh = MSH(field_separator="!", **_required_fields())
    assert msh.msh_1 == "!"


def test_direct_construction_by_encoding_characters_alias() -> None:
    """msh_2 can be set via the 'encoding_characters' human-readable alias."""
    msh = MSH(encoding_characters="@#$%", **_required_fields())
    assert msh.msh_2 == "@#$%"


def test_direct_construction_by_hl7_dot_notation() -> None:
    """msh_1 and msh_2 can be set via HL7 dot-notation keys in a dict unpack."""
    src = _decoded_msh()
    msh = MSH(**{
        "MSH.1": "!",
        "MSH.2": "@#$%",
        "MSH.9": src.msh_9,
        "MSH.10": src.msh_10,
        "MSH.11": src.msh_11,
        "MSH.12": src.msh_12,
    })
    assert msh.msh_1 == "!"
    assert msh.msh_2 == "@#$%"


def test_model_dump_by_alias_contains_hl7_dot_notation_keys() -> None:
    """model_dump(by_alias=True) uses HL7 dot-notation keys for MSH.1 and MSH.2."""
    msh = MSH(**_required_fields())
    dump = msh.model_dump(by_alias=True)
    assert "MSH.1" in dump
    assert "MSH.2" in dump


def test_model_dump_by_alias_msh_1_value() -> None:
    """model_dump(by_alias=True) preserves the msh_1 value under key 'MSH.1'."""
    msh = MSH(**_required_fields())
    assert msh.model_dump(by_alias=True)["MSH.1"] == "|"


def test_model_dump_by_alias_msh_2_value() -> None:
    """model_dump(by_alias=True) preserves the msh_2 value under key 'MSH.2'."""
    msh = MSH(**_required_fields())
    assert msh.model_dump(by_alias=True)["MSH.2"] == "^~\\&"


def test_direct_construction_without_required_field_raises() -> None:
    """Omitting a required non-default field such as msh_12 raises a ValidationError."""
    src = _decoded_msh()
    with pytest.raises(pydantic.ValidationError) as exc_info:
        MSH(msh_9=src.msh_9, msh_10=src.msh_10, msh_11=src.msh_11)
    missing = {e["loc"] for e in exc_info.value.errors() if e["type"] == "missing"}
    assert ("msh_12",) in missing

"""Tests for the generated ACK message model (hl7types.hl7.v2_4.messages.ACK).

Covers runtime behaviour of the Pydantic model: required/optional fields,
ER7 decoding, and direct construction by field name.
"""
from __future__ import annotations

import pytest
import pydantic

from hl7types import decode_er7
from hl7types.hl7.v2_4.messages.ACK import ACK
from hl7types.hl7.v2_4.segments.ERR import ERR

_ACK_NO_ERR = (
    "MSH|^~\\&|APP|FAC|APP2|FAC2|20240101120000||ACK|MSG001|P|2.4\r"
    "MSA|AA|MSG001\r"
)

_ACK_WITH_ERR = (
    "MSH|^~\\&|APP|FAC|APP2|FAC2|20240101120000||ACK|MSG001|P|2.4\r"
    "MSA|AA|MSG001\r"
    "ERR|207\r"
)


def test_decode_er7_msh_and_msa_populated() -> None:
    """ACK decoded from ER7 has MSH and MSA populated."""
    msg = decode_er7(_ACK_NO_ERR)
    assert msg.MSH is not None
    assert msg.MSA is not None


def test_decode_er7_err_absent_is_none() -> None:
    """ERR is None when no ERR segment is present in the ER7 message."""
    msg = decode_er7(_ACK_NO_ERR)
    assert msg.ERR is None


def test_decode_er7_err_present_populates_field() -> None:
    """ERR is populated when an ERR segment appears in the ER7 message."""
    msg = decode_er7(_ACK_WITH_ERR)
    assert msg.ERR is not None
    assert isinstance(msg.ERR, ERR)


def test_direct_construction_without_msh_raises() -> None:
    """Omitting MSH from direct construction raises a Pydantic ValidationError."""
    msg = decode_er7(_ACK_NO_ERR)
    with pytest.raises(pydantic.ValidationError) as exc_info:
        ACK(MSA=msg.MSA)
    missing = {e["loc"] for e in exc_info.value.errors() if e["type"] == "missing"}
    assert ("MSH",) in missing


def test_direct_construction_without_msa_raises() -> None:
    """Omitting MSA from direct construction raises a Pydantic ValidationError."""
    msg = decode_er7(_ACK_NO_ERR)
    with pytest.raises(pydantic.ValidationError) as exc_info:
        ACK(MSH=msg.MSH)
    missing = {e["loc"] for e in exc_info.value.errors() if e["type"] == "missing"}
    assert ("MSA",) in missing


def test_direct_construction_with_required_only_succeeds() -> None:
    """ACK can be constructed with only the required MSH and MSA fields."""
    msg = decode_er7(_ACK_NO_ERR)
    ack = ACK(MSH=msg.MSH, MSA=msg.MSA)
    assert ack.MSH is not None
    assert ack.MSA is not None
    assert ack.ERR is None


def test_populate_by_name_msh_and_msa() -> None:
    """Field-name population works for MSH and MSA."""
    msg = decode_er7(_ACK_NO_ERR)
    ack = ACK(MSH=msg.MSH, MSA=msg.MSA)
    assert ack.MSH is msg.MSH
    assert ack.MSA is msg.MSA


def test_populate_by_name_err() -> None:
    """Field-name population works for the optional ERR field."""
    msg = decode_er7(_ACK_WITH_ERR)
    ack = ACK(MSH=msg.MSH, MSA=msg.MSA, ERR=msg.ERR)
    assert ack.ERR is not None
    assert isinstance(ack.ERR, ERR)

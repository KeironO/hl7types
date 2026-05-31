"""
Tests for strict=True decoding, which enforces required segments/fields
instead of silently injecting empty placeholders.
"""
from __future__ import annotations

import pytest
from pydantic import ValidationError

import hl7types  # noqa: F401
from hl7types import decode_er7
from hl7types.hl7.v2_5_1.messages.ACK import ACK

ACK_WIRE = (
    r"MSH|^~\&|SEND|FAC|RECV|FAC|20240101120000||ACK|MSG001|P|2.5.1" + "\r"
    "MSA|AA|MSG001\r"
)

ACK_MISSING_MSA_WIRE = (
    r"MSH|^~\&|SEND|FAC|RECV|FAC|20240101120000||ACK|MSG001|P|2.5.1" + "\r"
)


def test_lenient_decode_complete_ack() -> None:
    """A complete ACK wire decodes correctly in lenient mode."""
    msg = decode_er7(ACK_WIRE, msg_cls=ACK)
    assert isinstance(msg, ACK)
    assert msg.MSA.msa_1 == "AA"
    assert msg.MSA.msa_2 == "MSG001"


def test_lenient_decode_missing_msa_succeeds() -> None:
    """ACK without MSA decodes without error in lenient mode (default)."""
    msg = decode_er7(ACK_MISSING_MSA_WIRE, strict=False)
    assert isinstance(msg, ACK)
    assert msg.MSA.model_fields_set == set()


def test_strict_decode_complete_ack() -> None:
    """A complete ACK wire decodes correctly in strict mode."""
    msg = decode_er7(ACK_WIRE, msg_cls=ACK, strict=True)
    assert isinstance(msg, ACK)
    assert msg.MSA.msa_1 == "AA"
    assert msg.MSA.msa_2 == "MSG001"


def test_strict_decode_missing_msa_raises() -> None:
    """ACK without MSA raises ValidationError in strict mode."""
    with pytest.raises(ValidationError):
        decode_er7(ACK_MISSING_MSA_WIRE, msg_cls=ACK, strict=True)


def test_lenient_model_validate_er7_missing_msa_succeeds() -> None:
    """model_validate_er7 without MSA succeeds in lenient mode."""
    msg = ACK.model_validate_er7(ACK_MISSING_MSA_WIRE)
    assert isinstance(msg, ACK)
    assert msg.MSA.model_fields_set == set()


def test_strict_model_validate_er7_missing_msa_raises() -> None:
    """model_validate_er7 without MSA raises ValidationError in strict mode."""
    with pytest.raises(ValidationError):
        ACK.model_validate_er7(ACK_MISSING_MSA_WIRE, strict=True)

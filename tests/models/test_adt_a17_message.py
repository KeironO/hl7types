"""Tests for the generated ADT_A17 message model (hl7types.hl7.v2_1.messages.ADT_A17).

Covers runtime behaviour of the Pydantic message model: required fields,
the repeating PATIENT group constraint, ER7 decoding, and direct construction
by field name.
"""
from __future__ import annotations

import pytest
import pydantic

from hl7types import decode_er7
from hl7types.hl7.v2_1.messages.ADT_A17 import ADT_A17
from hl7types.hl7.v2_1.groups.ADT_A17_PATIENT import ADT_A17_PATIENT

_ADT_A17 = (
    "MSH|^~\\&|APP|FAC|APP2|FAC2|19950101120000||ADT^A17|MSG001|P|2.1\r"
    "EVN|A17|19950101120000\r"
    "PID|1||P001||DOE^JOHN||\r"
    "PV1|1|I|WARD1\r"
    "PID|2||P002||SMITH^JANE||\r"
    "PV1|1|I|WARD2\r"
)


def test_decoded_adt_a17_has_msh() -> None:
    """A decoded ADT^A17 message has a populated MSH segment."""
    msg = decode_er7(_ADT_A17)
    assert msg.MSH is not None


def test_decoded_adt_a17_has_evn() -> None:
    """A decoded ADT^A17 message has a populated EVN segment."""
    msg = decode_er7(_ADT_A17)
    assert msg.EVN is not None


def test_decoded_adt_a17_patient_is_nonempty_list() -> None:
    """PATIENT is a non-empty list after decoding."""
    msg = decode_er7(_ADT_A17)
    assert isinstance(msg.PATIENT, list)
    assert len(msg.PATIENT) >= 1


def test_decoded_adt_a17_patient_items_are_correct_type() -> None:
    """Each item in the decoded PATIENT list is an ADT_A17_PATIENT group."""
    msg = decode_er7(_ADT_A17)
    for patient in msg.PATIENT:
        assert isinstance(patient, ADT_A17_PATIENT)


def test_direct_construction_with_all_fields_succeeds() -> None:
    """ADT_A17 can be constructed directly from valid decoded fields."""
    msg = decode_er7(_ADT_A17)
    adt = ADT_A17(MSH=msg.MSH, EVN=msg.EVN, PATIENT=msg.PATIENT)
    assert adt.MSH is not None
    assert adt.EVN is not None
    assert len(adt.PATIENT) >= 1


def test_direct_construction_without_msh_raises() -> None:
    """Omitting MSH from direct construction raises a Pydantic ValidationError."""
    msg = decode_er7(_ADT_A17)
    with pytest.raises(pydantic.ValidationError) as exc_info:
        ADT_A17(EVN=msg.EVN, PATIENT=msg.PATIENT)
    missing = {e["loc"] for e in exc_info.value.errors() if e["type"] == "missing"}
    assert ("MSH",) in missing


def test_direct_construction_without_evn_raises() -> None:
    """Omitting EVN from direct construction raises a Pydantic ValidationError."""
    msg = decode_er7(_ADT_A17)
    with pytest.raises(pydantic.ValidationError) as exc_info:
        ADT_A17(MSH=msg.MSH, PATIENT=msg.PATIENT)
    missing = {e["loc"] for e in exc_info.value.errors() if e["type"] == "missing"}
    assert ("EVN",) in missing


def test_direct_construction_without_patient_raises() -> None:
    """Omitting PATIENT from direct construction raises a Pydantic ValidationError."""
    msg = decode_er7(_ADT_A17)
    with pytest.raises(pydantic.ValidationError) as exc_info:
        ADT_A17(MSH=msg.MSH, EVN=msg.EVN)
    missing = {e["loc"] for e in exc_info.value.errors() if e["type"] == "missing"}
    assert ("PATIENT",) in missing


def test_direct_construction_with_empty_patient_raises() -> None:
    """Supplying PATIENT=[] raises a Pydantic ValidationError (min_length=1)."""
    msg = decode_er7(_ADT_A17)
    with pytest.raises(pydantic.ValidationError) as exc_info:
        ADT_A17(MSH=msg.MSH, EVN=msg.EVN, PATIENT=[])
    errors = exc_info.value.errors()
    assert any(e["loc"] == ("PATIENT",) and "length" in str(e).lower() for e in errors)


def test_direct_construction_preserves_patient_list() -> None:
    """The supplied PATIENT list is preserved on the constructed model."""
    msg = decode_er7(_ADT_A17)
    adt = ADT_A17(MSH=msg.MSH, EVN=msg.EVN, PATIENT=msg.PATIENT)
    assert adt.PATIENT == msg.PATIENT

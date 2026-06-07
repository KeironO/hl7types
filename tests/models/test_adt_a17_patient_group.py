"""Tests for the generated ADT_A17_PATIENT group model.

Covers runtime behaviour of the Pydantic group model: required fields,
construction from decoded segments, and field-name population.

Note: the ADT_A17_PATIENT group lives in v2_1. In that version the ADT_A17
message wraps two PATIENT groups (one per patient being swapped), so segments
are sourced by decoding an ADT^A17 v2.1 message and extracting the first group.
"""
from __future__ import annotations

import pytest
import pydantic

from hl7types import decode_er7
from hl7types.hl7.v2_1.groups.ADT_A17_PATIENT import ADT_A17_PATIENT

_ADT_A17 = (
    "MSH|^~\\&|APP|FAC|APP2|FAC2|19950101120000||ADT^A17|MSG001|P|2.1\r"
    "EVN|A17|19950101120000\r"
    "PID|1||P001||DOE^JOHN||\r"
    "PV1|1|I|WARD1\r"
    "PID|2||P002||SMITH^JANE||\r"
    "PV1|1|I|WARD2\r"
)


def _decoded_patient() -> ADT_A17_PATIENT:
    """Return the first PATIENT group from a decoded ADT^A17 message."""
    return decode_er7(_ADT_A17).PATIENT[0]


def test_decoded_message_exposes_patient_group() -> None:
    """A decoded ADT^A17 message exposes a list of ADT_A17_PATIENT groups."""
    msg = decode_er7(_ADT_A17)
    assert isinstance(msg.PATIENT, list)
    assert len(msg.PATIENT) >= 1
    assert isinstance(msg.PATIENT[0], ADT_A17_PATIENT)


def test_decoded_patient_group_has_pid() -> None:
    """The PATIENT group decoded from ER7 has a populated PID segment."""
    patient = _decoded_patient()
    assert patient.PID is not None


def test_decoded_patient_group_has_pv1() -> None:
    """The PATIENT group decoded from ER7 has a populated PV1 segment."""
    patient = _decoded_patient()
    assert patient.PV1 is not None


def test_direct_construction_with_pid_and_pv1_succeeds() -> None:
    """ADT_A17_PATIENT can be constructed directly from valid PID and PV1 objects."""
    patient = _decoded_patient()
    grp = ADT_A17_PATIENT(PID=patient.PID, PV1=patient.PV1)
    assert grp.PID is not None
    assert grp.PV1 is not None


def test_direct_construction_without_pid_raises() -> None:
    """Omitting PID from direct construction raises a Pydantic ValidationError."""
    patient = _decoded_patient()
    with pytest.raises(pydantic.ValidationError) as exc_info:
        ADT_A17_PATIENT(PV1=patient.PV1)
    missing = {e["loc"] for e in exc_info.value.errors() if e["type"] == "missing"}
    assert ("PID",) in missing


def test_direct_construction_without_pv1_raises() -> None:
    """Omitting PV1 from direct construction raises a Pydantic ValidationError."""
    patient = _decoded_patient()
    with pytest.raises(pydantic.ValidationError) as exc_info:
        ADT_A17_PATIENT(PID=patient.PID)
    missing = {e["loc"] for e in exc_info.value.errors() if e["type"] == "missing"}
    assert ("PV1",) in missing


def test_populate_by_name_preserves_pid_and_pv1() -> None:
    """Field-name population preserves the supplied PID and PV1 objects."""
    patient = _decoded_patient()
    grp = ADT_A17_PATIENT(PID=patient.PID, PV1=patient.PV1)
    assert grp.PID is patient.PID
    assert grp.PV1 is patient.PV1

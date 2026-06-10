"""Contract tests confirming PID.3 and PID.5 are enforced as required (minOccurs=1).

The XSD marks both fields as required and repeating; the generated model must
reject construction without them and reject an empty list for either.
"""
from __future__ import annotations

import pytest
from pydantic import ValidationError

from hl7types.hl7.v2_5_1.datatypes.CX import CX
from hl7types.hl7.v2_5_1.datatypes.XPN import XPN
from hl7types.hl7.v2_5_1.segments.PID import PID


def test_pid_without_pid_3_raises() -> None:
    with pytest.raises(ValidationError, match="pid_3"):
        PID(pid_5=[XPN.model_construct()])


def test_pid_without_pid_5_raises() -> None:
    with pytest.raises(ValidationError, match="pid_5"):
        PID(pid_3=[CX.model_construct()])


def test_pid_with_empty_pid_3_raises() -> None:
    with pytest.raises(ValidationError, match="pid_3"):
        PID(pid_3=[], pid_5=[XPN.model_construct()])


def test_pid_with_empty_pid_5_raises() -> None:
    with pytest.raises(ValidationError, match="pid_5"):
        PID(pid_3=[CX.model_construct()], pid_5=[])


def test_pid_with_required_fields_succeeds() -> None:
    pid = PID(pid_3=[CX.model_construct()], pid_5=[XPN.model_construct()])
    assert len(pid.pid_3) == 1
    assert len(pid.pid_5) == 1

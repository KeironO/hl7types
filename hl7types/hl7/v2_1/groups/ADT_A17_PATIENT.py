"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.1
Class: ADT_A17.PATIENT
Type: Group
"""
from __future__ import annotations

from typing import Optional
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.PID import PID
from ..segments.PV1 import PV1

_PID = PID
_PV1 = PV1


class ADT_A17_PATIENT(HL7Model):
    """HL7 v2 ADT_A17.PATIENT group.

    Attributes:
        PID (PID): required
        PV1 (PV1): required
    """

    PID: _PID = Field(
        default=...,
        title="PID",
        description="Required",
    )

    PV1: _PV1 = Field(
        default=...,
        title="PV1",
        description="Required",
    )

    model_config = {"populate_by_name": True}

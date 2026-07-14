"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.1
Class: ADT_A17.PATIENT
Type: Group
"""
from __future__ import annotations

from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.PID import PID
from ..segments.PV1 import PV1

_PID = PID
_PV1 = PV1


class ADT_A17_PATIENT(HL7Model):
    """HL7 v2 ADT_A17.PATIENT group.

    Attributes:
        PID (PID): PATIENT IDENTIFICATION, required
        PV1 (PV1): PATIENT VISIT, required
    """

    PID: _PID = Field(
        title="PID",
        description="PATIENT IDENTIFICATION",
    )

    PV1: _PV1 = Field(
        title="PV1",
        description="PATIENT VISIT",
    )

    model_config = {"populate_by_name": True}

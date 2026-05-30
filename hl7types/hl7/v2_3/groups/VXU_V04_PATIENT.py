"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3
Class: VXU_V04.PATIENT
Type: Group
"""
from __future__ import annotations

from typing import Optional
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.PV1 import PV1
from ..segments.PV2 import PV2

_PV1 = PV1
_PV2 = PV2


class VXU_V04_PATIENT(HL7Model):
    """HL7 v2 VXU_V04.PATIENT group.

    Attributes:
        PV1 (PV1): required
        PV2 (Optional[PV2]): optional
    """

    PV1: _PV1 = Field(
        default=...,
        title="PV1",
        description="Required",
    )

    PV2: Optional[_PV2] = Field(
        default=None,
        title="PV2",
        description="Optional",
    )

    model_config = {"populate_by_name": True}

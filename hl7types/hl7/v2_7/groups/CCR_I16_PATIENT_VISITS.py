"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7
Class: CCR_I16.PATIENT_VISITS
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


class CCR_I16_PATIENT_VISITS(HL7Model):
    """HL7 v2 CCR_I16.PATIENT_VISITS group.

    Attributes:
        PV1 (PV1): Patient Visit, required
        PV2 (Optional[PV2]): Patient Visit - Additional Information, optional
    """

    PV1: _PV1 = Field(
        title="PV1",
        description="Patient Visit",
    )

    PV2: Optional[_PV2] = Field(
        default=None,
        title="PV2",
        description="Patient Visit - Additional Information",
    )

    model_config = {"populate_by_name": True}

"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.4
Class: OMG_O19.PATIENT_VISIT_PRIOR
Type: Group
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..segments.PV1 import PV1
from ..segments.PV2 import PV2

_PV1 = PV1
_PV2 = PV2


class OMG_O19_PATIENT_VISIT_PRIOR(BaseModel):
    """HL7 v2 OMG_O19.PATIENT_VISIT_PRIOR group.

    Attributes:
        PV1 (PV1): required
        PV2 (Optional[PV2]): optional
    """

    PV1: _PV1 = Field(
        default=...,
        title="PV1",
        description="Required",
    )

    PV2: _PV2 | None = Field(
        default=None,
        title="PV2",
        description="Optional",
    )

    model_config = {"populate_by_name": True}

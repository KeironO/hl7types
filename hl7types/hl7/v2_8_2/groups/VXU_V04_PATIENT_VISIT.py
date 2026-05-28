"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.2
Class: VXU_V04.PATIENT_VISIT
Type: Group
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..segments.ARV import ARV
from ..segments.PV1 import PV1
from ..segments.PV2 import PV2

_ARV = ARV
_PV1 = PV1
_PV2 = PV2


class VXU_V04_PATIENT_VISIT(BaseModel):
    """HL7 v2 VXU_V04.PATIENT_VISIT group.

    Attributes:
        PV1 (PV1): required
        PV2 (Optional[PV2]): optional
        ARV (Optional[List[ARV]]): optional
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

    ARV: list[_ARV] | None = Field(
        default=None,
        title="ARV",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}

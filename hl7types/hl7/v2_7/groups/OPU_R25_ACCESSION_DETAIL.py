"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7
Class: OPU_R25.ACCESSION_DETAIL
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import BaseModel, Field

from ..segments.NK1 import NK1

from .OPU_R25_PATIENT import OPU_R25_PATIENT
from .OPU_R25_SPECIMEN import OPU_R25_SPECIMEN

_NK1 = NK1
_OPU_R25_PATIENT = OPU_R25_PATIENT
_OPU_R25_SPECIMEN = OPU_R25_SPECIMEN


class OPU_R25_ACCESSION_DETAIL(BaseModel):
    """HL7 v2 OPU_R25.ACCESSION_DETAIL group.

    Attributes:
        NK1 (List[NK1]): required
        PATIENT (Optional[OPU_R25_PATIENT]): optional
        SPECIMEN (List[OPU_R25_SPECIMEN]): required
    """

    NK1: List[_NK1] = Field(
        default=...,
        title="NK1",
        description="Required, repeating",
    )

    PATIENT: Optional[_OPU_R25_PATIENT] = Field(
        default=None,
        title="PATIENT",
        description="Optional",
    )

    SPECIMEN: List[_OPU_R25_SPECIMEN] = Field(
        default=...,
        title="SPECIMEN",
        description="Required, repeating",
    )

    model_config = {"populate_by_name": True}

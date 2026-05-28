"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.1
Class: CRM_C01.PATIENT_VISIT
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import BaseModel, Field

from ..segments.PRT import PRT
from ..segments.PV1 import PV1

_PRT = PRT
_PV1 = PV1


class CRM_C01_PATIENT_VISIT(BaseModel):
    """HL7 v2 CRM_C01.PATIENT_VISIT group.

    Attributes:
        PV1 (PV1): required
        PRT (Optional[List[PRT]]): optional
    """

    PV1: _PV1 = Field(
        default=...,
        title="PV1",
        description="Required",
    )

    PRT: Optional[List[_PRT]] = Field(
        default=None,
        title="PRT",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}

"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3
Class: CRM_C01
Type: Message
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import BaseModel, Field

from ..segments.MSH import MSH

from ..groups.CRM_C01_PATIENT import CRM_C01_PATIENT

_CRM_C01_PATIENT = CRM_C01_PATIENT
_MSH = MSH


class CRM_C01(BaseModel):
    """HL7 v2 CRM_C01 message.

    Attributes:
        MSH (MSH): required
        PATIENT (List[CRM_C01_PATIENT]): required
    """

    MSH: _MSH = Field(
        default=...,
        title="MSH",
        description="Required",
    )

    PATIENT: List[_CRM_C01_PATIENT] = Field(
        default=...,
        title="PATIENT",
        description="Required, repeating",
    )

    model_config = {"populate_by_name": True}

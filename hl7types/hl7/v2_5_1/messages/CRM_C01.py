"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5.1
Class: CRM_C01
Type: Message
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..groups.CRM_C01_PATIENT import CRM_C01_PATIENT
from ..segments.MSH import MSH
from ..segments.SFT import SFT

_CRM_C01_PATIENT = CRM_C01_PATIENT
_MSH = MSH
_SFT = SFT


class CRM_C01(BaseModel):
    """HL7 v2 CRM_C01 message.

    Attributes:
        MSH (MSH): required
        SFT (Optional[List[SFT]]): optional
        PATIENT (List[CRM_C01_PATIENT]): required
    """

    MSH: _MSH = Field(
        default=...,
        title="MSH",
        description="Required",
    )

    SFT: list[_SFT] | None = Field(
        default=None,
        title="SFT",
        description="Optional, repeating",
    )

    PATIENT: list[_CRM_C01_PATIENT] = Field(
        default=...,
        title="PATIENT",
        description="Required, repeating",
    )

    model_config = {"populate_by_name": True}

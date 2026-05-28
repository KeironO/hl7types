"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.2
Class: EHC_E01
Type: Message
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import BaseModel, Field

from ..segments.MSH import MSH
from ..segments.SFT import SFT
from ..segments.UAC import UAC

from ..groups.EHC_E01_INVOICE_INFORMATION_SUBMIT import EHC_E01_INVOICE_INFORMATION_SUBMIT

_EHC_E01_INVOICE_INFORMATION_SUBMIT = EHC_E01_INVOICE_INFORMATION_SUBMIT
_MSH = MSH
_SFT = SFT
_UAC = UAC


class EHC_E01(BaseModel):
    """HL7 v2 EHC_E01 message.

    Attributes:
        MSH (MSH): required
        SFT (Optional[List[SFT]]): optional
        UAC (Optional[List[UAC]]): optional
        INVOICE_INFORMATION_SUBMIT (EHC_E01_INVOICE_INFORMATION_SUBMIT): required
    """

    MSH: _MSH = Field(
        default=...,
        title="MSH",
        description="Required",
    )

    SFT: Optional[List[_SFT]] = Field(
        default=None,
        title="SFT",
        description="Optional, repeating",
    )

    UAC: Optional[List[_UAC]] = Field(
        default=None,
        title="UAC",
        description="Optional, repeating",
    )

    INVOICE_INFORMATION_SUBMIT: _EHC_E01_INVOICE_INFORMATION_SUBMIT = Field(
        default=...,
        title="INVOICE_INFORMATION_SUBMIT",
        description="Required",
    )

    model_config = {"populate_by_name": True}

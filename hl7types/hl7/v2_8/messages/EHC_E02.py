"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8
Class: EHC_E02
Type: Message
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import BaseModel, Field

from ..segments.MSH import MSH
from ..segments.SFT import SFT
from ..segments.UAC import UAC

from ..groups.EHC_E02_INVOICE_INFORMATION_CANCEL import EHC_E02_INVOICE_INFORMATION_CANCEL

_EHC_E02_INVOICE_INFORMATION_CANCEL = EHC_E02_INVOICE_INFORMATION_CANCEL
_MSH = MSH
_SFT = SFT
_UAC = UAC


class EHC_E02(BaseModel):
    """HL7 v2 EHC_E02 message.

    Attributes:
        MSH (MSH): required
        SFT (Optional[List[SFT]]): optional
        UAC (Optional[List[UAC]]): optional
        INVOICE_INFORMATION_CANCEL (EHC_E02_INVOICE_INFORMATION_CANCEL): required
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

    INVOICE_INFORMATION_CANCEL: _EHC_E02_INVOICE_INFORMATION_CANCEL = Field(
        default=...,
        title="INVOICE_INFORMATION_CANCEL",
        description="Required",
    )

    model_config = {"populate_by_name": True}

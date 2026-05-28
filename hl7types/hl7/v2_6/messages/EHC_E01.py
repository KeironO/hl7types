"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.6
Class: EHC_E01
Type: Message
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..groups.EHC_E01_INVOICE_INFORMATION import EHC_E01_INVOICE_INFORMATION
from ..segments.MSH import MSH
from ..segments.SFT import SFT
from ..segments.UAC import UAC

_EHC_E01_INVOICE_INFORMATION = EHC_E01_INVOICE_INFORMATION
_MSH = MSH
_SFT = SFT
_UAC = UAC


class EHC_E01(BaseModel):
    """HL7 v2 EHC_E01 message.

    Attributes:
        MSH (MSH): required
        SFT (Optional[List[SFT]]): optional
        UAC (Optional[List[UAC]]): optional
        INVOICE_INFORMATION (EHC_E01_INVOICE_INFORMATION): required
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

    UAC: list[_UAC] | None = Field(
        default=None,
        title="UAC",
        description="Optional, repeating",
    )

    INVOICE_INFORMATION: _EHC_E01_INVOICE_INFORMATION = Field(
        default=...,
        title="INVOICE_INFORMATION",
        description="Required",
    )

    model_config = {"populate_by_name": True}

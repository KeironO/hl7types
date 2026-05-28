"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7.1
Class: EHC_E15
Type: Message
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..groups.EHC_E15_ADJUSTMENT_PAYEE import EHC_E15_ADJUSTMENT_PAYEE
from ..groups.EHC_E15_PAYMENT_REMITTANCE_DETAIL_INFO import EHC_E15_PAYMENT_REMITTANCE_DETAIL_INFO
from ..groups.EHC_E15_PAYMENT_REMITTANCE_HEADER_INFO import EHC_E15_PAYMENT_REMITTANCE_HEADER_INFO
from ..segments.MSH import MSH
from ..segments.SFT import SFT
from ..segments.UAC import UAC

_EHC_E15_ADJUSTMENT_PAYEE = EHC_E15_ADJUSTMENT_PAYEE
_EHC_E15_PAYMENT_REMITTANCE_DETAIL_INFO = EHC_E15_PAYMENT_REMITTANCE_DETAIL_INFO
_EHC_E15_PAYMENT_REMITTANCE_HEADER_INFO = EHC_E15_PAYMENT_REMITTANCE_HEADER_INFO
_MSH = MSH
_SFT = SFT
_UAC = UAC


class EHC_E15(BaseModel):
    """HL7 v2 EHC_E15 message.

    Attributes:
        MSH (MSH): required
        SFT (Optional[List[SFT]]): optional
        UAC (Optional[List[UAC]]): optional
        PAYMENT_REMITTANCE_HEADER_INFO (EHC_E15_PAYMENT_REMITTANCE_HEADER_INFO): required
        PAYMENT_REMITTANCE_DETAIL_INFO (Optional[List[EHC_E15_PAYMENT_REMITTANCE_DETAIL_INFO]]): optional
        ADJUSTMENT_PAYEE (Optional[List[EHC_E15_ADJUSTMENT_PAYEE]]): optional
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

    PAYMENT_REMITTANCE_HEADER_INFO: _EHC_E15_PAYMENT_REMITTANCE_HEADER_INFO = Field(
        default=...,
        title="PAYMENT_REMITTANCE_HEADER_INFO",
        description="Required",
    )

    PAYMENT_REMITTANCE_DETAIL_INFO: list[_EHC_E15_PAYMENT_REMITTANCE_DETAIL_INFO] | None = Field(
        default=None,
        title="PAYMENT_REMITTANCE_DETAIL_INFO",
        description="Optional, repeating",
    )

    ADJUSTMENT_PAYEE: list[_EHC_E15_ADJUSTMENT_PAYEE] | None = Field(
        default=None,
        title="ADJUSTMENT_PAYEE",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}

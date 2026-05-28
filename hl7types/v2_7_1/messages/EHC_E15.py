"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7.1
Class: EHC_E15
Type: Message
"""
from _future__ import annotations

from typing import Optional, List
from pydantic import BaseModel, Field

from ..segments.MSH import MSH
from ..segments.SFT import SFT
from ..segments.UAC import UAC

from ..groups.EHC_E15_ADJUSTMENT_PAYEE import EHC_E15_ADJUSTMENT_PAYEE
from ..groups.EHC_E15_PAYMENT_REMITTANCE_DETAIL_INFO import EHC_E15_PAYMENT_REMITTANCE_DETAIL_INFO
from ..groups.EHC_E15_PAYMENT_REMITTANCE_HEADER_INFO import EHC_E15_PAYMENT_REMITTANCE_HEADER_INFO

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

    PAYMENT_REMITTANCE_HEADER_INFO: _EHC_E15_PAYMENT_REMITTANCE_HEADER_INFO = Field(
        default=...,
        title="PAYMENT_REMITTANCE_HEADER_INFO",
        description="Required",
    )

    PAYMENT_REMITTANCE_DETAIL_INFO: Optional[List[_EHC_E15_PAYMENT_REMITTANCE_DETAIL_INFO]] = Field(
        default=None,
        title="PAYMENT_REMITTANCE_DETAIL_INFO",
        description="Optional, repeating",
    )

    ADJUSTMENT_PAYEE: Optional[List[_EHC_E15_ADJUSTMENT_PAYEE]] = Field(
        default=None,
        title="ADJUSTMENT_PAYEE",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}

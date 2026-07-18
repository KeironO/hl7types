"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7.1
Class: EHC_E15
Type: Message
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import ConfigDict, Field
from hl7types.hl7 import HL7Model

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


class EHC_E15(HL7Model):
    """Payment/Remittance Advice (S16.3.1).

    Attributes:
        MSH (MSH): Message Header, required
        SFT (Optional[List[SFT]]): Software Segment, optional
        UAC (Optional[List[UAC]]): User Authentication Credential Segment, optional
        PAYMENT_REMITTANCE_HEADER_INFO (EHC_E15_PAYMENT_REMITTANCE_HEADER_INFO): required
        PAYMENT_REMITTANCE_DETAIL_INFO (Optional[List[EHC_E15_PAYMENT_REMITTANCE_DETAIL_INFO]]): optional
        ADJUSTMENT_PAYEE (Optional[List[EHC_E15_ADJUSTMENT_PAYEE]]): optional
    """

    MSH: _MSH = Field(
        title="MSH",
        description="Message Header",
    )

    SFT: Optional[List[_SFT]] = Field(
        default=None,
        title="SFT",
        description="Software Segment",
    )

    UAC: Optional[List[_UAC]] = Field(
        default=None,
        title="UAC",
        description="User Authentication Credential Segment",
    )

    PAYMENT_REMITTANCE_HEADER_INFO: _EHC_E15_PAYMENT_REMITTANCE_HEADER_INFO = Field(
        title="PAYMENT_REMITTANCE_HEADER_INFO",
    )

    PAYMENT_REMITTANCE_DETAIL_INFO: Optional[List[_EHC_E15_PAYMENT_REMITTANCE_DETAIL_INFO]] = Field(
        default=None,
        title="PAYMENT_REMITTANCE_DETAIL_INFO",
    )

    ADJUSTMENT_PAYEE: Optional[List[_EHC_E15_ADJUSTMENT_PAYEE]] = Field(
        default=None,
        title="ADJUSTMENT_PAYEE",
    )

    model_config = ConfigDict(populate_by_name=True)

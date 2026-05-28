"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.1
Class: EHC_E15.PAYMENT_REMITTANCE_DETAIL_INFO
Type: Group
"""
from _future__ import annotations

from typing import Optional, List
from pydantic import BaseModel, Field

from ..segments.IPR import IPR
from ..segments.IVC import IVC

from .EHC_E15_PRODUCT_SERVICE_SECTION import EHC_E15_PRODUCT_SERVICE_SECTION

_EHC_E15_PRODUCT_SERVICE_SECTION = EHC_E15_PRODUCT_SERVICE_SECTION
_IPR = IPR
_IVC = IVC


class EHC_E15_PAYMENT_REMITTANCE_DETAIL_INFO(BaseModel):
    """HL7 v2 EHC_E15.PAYMENT_REMITTANCE_DETAIL_INFO group.

    Attributes:
        IPR (IPR): required
        IVC (IVC): required
        PRODUCT_SERVICE_SECTION (List[EHC_E15_PRODUCT_SERVICE_SECTION]): required
    """

    IPR: _IPR = Field(
        default=...,
        title="IPR",
        description="Required",
    )

    IVC: _IVC = Field(
        default=...,
        title="IVC",
        description="Required",
    )

    PRODUCT_SERVICE_SECTION: List[_EHC_E15_PRODUCT_SERVICE_SECTION] = Field(
        default=...,
        title="PRODUCT_SERVICE_SECTION",
        description="Required, repeating",
    )

    model_config = {"populate_by_name": True}

"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.6
Class: EHC_E15.PAYMENT_REMITTANCE_DETAIL_INFO
Type: Group
"""
from __future__ import annotations

from typing import List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.IPR import IPR
from ..segments.IVC import IVC

from .EHC_E15_PRODUCT_SERVICE_SECTION import EHC_E15_PRODUCT_SERVICE_SECTION

_EHC_E15_PRODUCT_SERVICE_SECTION = EHC_E15_PRODUCT_SERVICE_SECTION
_IPR = IPR
_IVC = IVC


class EHC_E15_PAYMENT_REMITTANCE_DETAIL_INFO(HL7Model):
    """HL7 v2 EHC_E15.PAYMENT_REMITTANCE_DETAIL_INFO group.

    Attributes:
        IPR (IPR): required
        IVC (IVC): required
        PRODUCT_SERVICE_SECTION (List[EHC_E15_PRODUCT_SERVICE_SECTION]): required
    """

    IPR: _IPR = Field(
        title="IPR",
        description="Required",
    )

    IVC: _IVC = Field(
        title="IVC",
        description="Required",
    )

    PRODUCT_SERVICE_SECTION: List[_EHC_E15_PRODUCT_SERVICE_SECTION] = Field(
        min_length=1,
        title="PRODUCT_SERVICE_SECTION",
        description="Required, repeating",
    )

    model_config = {"populate_by_name": True}

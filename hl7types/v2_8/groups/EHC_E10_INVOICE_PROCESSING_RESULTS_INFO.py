"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8
Class: EHC_E10.INVOICE_PROCESSING_RESULTS_INFO
Type: Group
"""
from _future__ import annotations

from typing import Optional, List
from pydantic import BaseModel, Field

from ..segments.IN1 import IN1
from ..segments.IN2 import IN2
from ..segments.IPR import IPR
from ..segments.IVC import IVC
from ..segments.NTE import NTE
from ..segments.PYE import PYE

from .EHC_E10_PRODUCT_SERVICE_SECTION import EHC_E10_PRODUCT_SERVICE_SECTION

_EHC_E10_PRODUCT_SERVICE_SECTION = EHC_E10_PRODUCT_SERVICE_SECTION
_IN1 = IN1
_IN2 = IN2
_IPR = IPR
_IVC = IVC
_NTE = NTE
_PYE = PYE


class EHC_E10_INVOICE_PROCESSING_RESULTS_INFO(BaseModel):
    """HL7 v2 EHC_E10.INVOICE_PROCESSING_RESULTS_INFO group.

    Attributes:
        IPR (IPR): required
        NTE (Optional[List[NTE]]): optional
        PYE (PYE): required
        IN1 (IN1): required
        IN2 (Optional[IN2]): optional
        IVC (IVC): required
        PRODUCT_SERVICE_SECTION (List[EHC_E10_PRODUCT_SERVICE_SECTION]): required
    """

    IPR: _IPR = Field(
        default=...,
        title="IPR",
        description="Required",
    )

    NTE: Optional[List[_NTE]] = Field(
        default=None,
        title="NTE",
        description="Optional, repeating",
    )

    PYE: _PYE = Field(
        default=...,
        title="PYE",
        description="Required",
    )

    IN1: _IN1 = Field(
        default=...,
        title="IN1",
        description="Required",
    )

    IN2: Optional[_IN2] = Field(
        default=None,
        title="IN2",
        description="Optional",
    )

    IVC: _IVC = Field(
        default=...,
        title="IVC",
        description="Required",
    )

    PRODUCT_SERVICE_SECTION: List[_EHC_E10_PRODUCT_SERVICE_SECTION] = Field(
        default=...,
        title="PRODUCT_SERVICE_SECTION",
        description="Required, repeating",
    )

    model_config = {"populate_by_name": True}

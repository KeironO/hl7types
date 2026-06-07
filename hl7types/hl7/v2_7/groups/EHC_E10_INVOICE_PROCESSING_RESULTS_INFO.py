"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7
Class: EHC_E10.INVOICE_PROCESSING_RESULTS_INFO
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

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


class EHC_E10_INVOICE_PROCESSING_RESULTS_INFO(HL7Model):
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
        title="IPR",
        description="Required",
    )

    NTE: Optional[List[_NTE]] = Field(
        default=None,
        title="NTE",
        description="Optional, repeating",
    )

    PYE: _PYE = Field(
        title="PYE",
        description="Required",
    )

    IN1: _IN1 = Field(
        title="IN1",
        description="Required",
    )

    IN2: Optional[_IN2] = Field(
        default=None,
        title="IN2",
        description="Optional",
    )

    IVC: _IVC = Field(
        title="IVC",
        description="Required",
    )

    PRODUCT_SERVICE_SECTION: List[_EHC_E10_PRODUCT_SERVICE_SECTION] = Field(
        min_length=1,
        title="PRODUCT_SERVICE_SECTION",
        description="Required, repeating",
    )

    model_config = {"populate_by_name": True}

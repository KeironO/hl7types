"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.6
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
        IPR (IPR): Invoice Processing Results, required
        NTE (Optional[List[NTE]]): Notes and Comments, optional
        PYE (PYE): Payee Information, required
        IN1 (IN1): Insurance, required
        IN2 (Optional[IN2]): Insurance Additional Information, optional
        IVC (IVC): Invoice Segment, required
        PRODUCT_SERVICE_SECTION (List[EHC_E10_PRODUCT_SERVICE_SECTION]): required
    """

    IPR: _IPR = Field(
        title="IPR",
        description="Invoice Processing Results",
    )

    NTE: Optional[List[_NTE]] = Field(
        default=None,
        title="NTE",
        description="Notes and Comments",
    )

    PYE: _PYE = Field(
        title="PYE",
        description="Payee Information",
    )

    IN1: _IN1 = Field(
        title="IN1",
        description="Insurance",
    )

    IN2: Optional[_IN2] = Field(
        default=None,
        title="IN2",
        description="Insurance Additional Information",
    )

    IVC: _IVC = Field(
        title="IVC",
        description="Invoice Segment",
    )

    PRODUCT_SERVICE_SECTION: List[_EHC_E10_PRODUCT_SERVICE_SECTION] = Field(
        min_length=1,
        title="PRODUCT_SERVICE_SECTION",
    )

    model_config = {"populate_by_name": True}

"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8
Class: EHC_E04.REASSESSMENT_REQUEST_INFO
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.IVC import IVC
from ..segments.NTE import NTE

from .EHC_E04_PRODUCT_SERVICE_SECTION import EHC_E04_PRODUCT_SERVICE_SECTION

_EHC_E04_PRODUCT_SERVICE_SECTION = EHC_E04_PRODUCT_SERVICE_SECTION
_IVC = IVC
_NTE = NTE


class EHC_E04_REASSESSMENT_REQUEST_INFO(HL7Model):
    """HL7 v2 EHC_E04.REASSESSMENT_REQUEST_INFO group.

    Attributes:
        IVC (Optional[IVC]): Invoice Segment, optional
        NTE (Optional[List[NTE]]): Notes and Comments, optional
        PRODUCT_SERVICE_SECTION (Optional[List[EHC_E04_PRODUCT_SERVICE_SECTION]]): optional
    """

    IVC: Optional[_IVC] = Field(
        default=None,
        title="IVC",
        description="Invoice Segment",
    )

    NTE: Optional[List[_NTE]] = Field(
        default=None,
        title="NTE",
        description="Notes and Comments",
    )

    PRODUCT_SERVICE_SECTION: Optional[List[_EHC_E04_PRODUCT_SERVICE_SECTION]] = Field(
        default=None,
        title="PRODUCT_SERVICE_SECTION",
    )

    model_config = {"populate_by_name": True}

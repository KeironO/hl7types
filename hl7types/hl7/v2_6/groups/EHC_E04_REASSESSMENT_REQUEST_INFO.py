"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.6
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
        IVC (Optional[IVC]): optional
        NTE (Optional[List[NTE]]): optional
        PRODUCT_SERVICE_SECTION (Optional[List[EHC_E04_PRODUCT_SERVICE_SECTION]]): optional
    """

    IVC: Optional[_IVC] = Field(
        default=None,
        title="IVC",
        description="Optional",
    )

    NTE: Optional[List[_NTE]] = Field(
        default=None,
        title="NTE",
        description="Optional, repeating",
    )

    PRODUCT_SERVICE_SECTION: Optional[List[_EHC_E04_PRODUCT_SERVICE_SECTION]] = Field(
        default=None,
        title="PRODUCT_SERVICE_SECTION",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}

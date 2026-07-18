"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7.1
Class: EHC_E02.INVOICE_INFORMATION
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import ConfigDict, Field
from hl7types.hl7 import HL7Model

from ..segments.CTD import CTD
from ..segments.IVC import IVC
from ..segments.NTE import NTE
from ..segments.PYE import PYE

from .EHC_E02_PRODUCT_SERVICE_SECTION import EHC_E02_PRODUCT_SERVICE_SECTION

_CTD = CTD
_EHC_E02_PRODUCT_SERVICE_SECTION = EHC_E02_PRODUCT_SERVICE_SECTION
_IVC = IVC
_NTE = NTE
_PYE = PYE


class EHC_E02_INVOICE_INFORMATION(HL7Model):
    """HL7 v2 EHC_E02.INVOICE_INFORMATION group.

    Attributes:
        IVC (Optional[IVC]): Invoice Segment, optional
        PYE (Optional[PYE]): Payee Information, optional
        CTD (Optional[List[CTD]]): Contact Data, optional
        NTE (Optional[List[NTE]]): Notes and Comments, optional
        PRODUCT_SERVICE_SECTION (Optional[List[EHC_E02_PRODUCT_SERVICE_SECTION]]): optional
    """

    IVC: Optional[_IVC] = Field(
        default=None,
        title="IVC",
        description="Invoice Segment",
    )

    PYE: Optional[_PYE] = Field(
        default=None,
        title="PYE",
        description="Payee Information",
    )

    CTD: Optional[List[_CTD]] = Field(
        default=None,
        title="CTD",
        description="Contact Data",
    )

    NTE: Optional[List[_NTE]] = Field(
        default=None,
        title="NTE",
        description="Notes and Comments",
    )

    PRODUCT_SERVICE_SECTION: Optional[List[_EHC_E02_PRODUCT_SERVICE_SECTION]] = Field(
        default=None,
        title="PRODUCT_SERVICE_SECTION",
    )

    model_config = ConfigDict(populate_by_name=True)

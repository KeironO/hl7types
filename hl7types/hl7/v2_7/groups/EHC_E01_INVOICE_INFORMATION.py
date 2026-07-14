"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7
Class: EHC_E01.INVOICE_INFORMATION
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.AUT import AUT
from ..segments.CTD import CTD
from ..segments.IVC import IVC
from ..segments.LOC import LOC
from ..segments.PYE import PYE
from ..segments.ROL import ROL

from .EHC_E01_PRODUCT_SERVICE_SECTION import EHC_E01_PRODUCT_SERVICE_SECTION

_AUT = AUT
_CTD = CTD
_EHC_E01_PRODUCT_SERVICE_SECTION = EHC_E01_PRODUCT_SERVICE_SECTION
_IVC = IVC
_LOC = LOC
_PYE = PYE
_ROL = ROL


class EHC_E01_INVOICE_INFORMATION(HL7Model):
    """HL7 v2 EHC_E01.INVOICE_INFORMATION group.

    Attributes:
        IVC (Optional[IVC]): Invoice Segment, optional
        PYE (Optional[PYE]): Payee Information, optional
        CTD (Optional[List[CTD]]): Contact Data, optional
        AUT (Optional[AUT]): Authorization Information, optional
        LOC (Optional[List[LOC]]): Location Identification, optional
        ROL (Optional[List[ROL]]): Role, optional
        PRODUCT_SERVICE_SECTION (Optional[List[EHC_E01_PRODUCT_SERVICE_SECTION]]): optional
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

    AUT: Optional[_AUT] = Field(
        default=None,
        title="AUT",
        description="Authorization Information",
    )

    LOC: Optional[List[_LOC]] = Field(
        default=None,
        title="LOC",
        description="Location Identification",
    )

    ROL: Optional[List[_ROL]] = Field(
        default=None,
        title="ROL",
        description="Role",
    )

    PRODUCT_SERVICE_SECTION: Optional[List[_EHC_E01_PRODUCT_SERVICE_SECTION]] = Field(
        default=None,
        title="PRODUCT_SERVICE_SECTION",
    )

    model_config = {"populate_by_name": True}

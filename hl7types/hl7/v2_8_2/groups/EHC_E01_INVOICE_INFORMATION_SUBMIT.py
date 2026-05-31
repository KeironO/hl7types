"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.2
Class: EHC_E01.INVOICE_INFORMATION_SUBMIT
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
from ..segments.PRT import PRT
from ..segments.PYE import PYE
from ..segments.ROL import ROL

from .EHC_E01_PRODUCT_SERVICE_SECTION import EHC_E01_PRODUCT_SERVICE_SECTION

_AUT = AUT
_CTD = CTD
_EHC_E01_PRODUCT_SERVICE_SECTION = EHC_E01_PRODUCT_SERVICE_SECTION
_IVC = IVC
_LOC = LOC
_PRT = PRT
_PYE = PYE
_ROL = ROL


class EHC_E01_INVOICE_INFORMATION_SUBMIT(HL7Model):
    """HL7 v2 EHC_E01.INVOICE_INFORMATION_SUBMIT group.

    Attributes:
        IVC (Optional[IVC]): optional
        PYE (Optional[PYE]): optional
        CTD (Optional[List[CTD]]): optional
        AUT (Optional[AUT]): optional
        LOC (Optional[List[LOC]]): optional
        PRT (Optional[List[PRT]]): optional
        ROL (Optional[List[ROL]]): optional
        PRODUCT_SERVICE_SECTION (Optional[List[EHC_E01_PRODUCT_SERVICE_SECTION]]): optional
    """

    IVC: Optional[_IVC] = Field(
        default=None,
        title="IVC",
        description="Optional",
    )

    PYE: Optional[_PYE] = Field(
        default=None,
        title="PYE",
        description="Optional",
    )

    CTD: Optional[List[_CTD]] = Field(
        default=None,
        title="CTD",
        description="Optional, repeating",
    )

    AUT: Optional[_AUT] = Field(
        default=None,
        title="AUT",
        description="Optional",
    )

    LOC: Optional[List[_LOC]] = Field(
        default=None,
        title="LOC",
        description="Optional, repeating",
    )

    PRT: Optional[List[_PRT]] = Field(
        default=None,
        title="PRT",
        description="Optional, repeating",
    )

    ROL: Optional[List[_ROL]] = Field(
        default=None,
        title="ROL",
        description="Optional, repeating",
    )

    PRODUCT_SERVICE_SECTION: Optional[List[_EHC_E01_PRODUCT_SERVICE_SECTION]] = Field(
        default=None,
        title="PRODUCT_SERVICE_SECTION",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}

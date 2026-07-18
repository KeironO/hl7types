"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8
Class: EHC_E01.PRODUCT_SERVICE_LINE_ITEM
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import ConfigDict, Field
from hl7types.hl7 import HL7Model

from ..segments.ADJ import ADJ
from ..segments.AUT import AUT
from ..segments.LOC import LOC
from ..segments.NTE import NTE
from ..segments.PRT import PRT
from ..segments.PSL import PSL
from ..segments.ROL import ROL

_ADJ = ADJ
_AUT = AUT
_LOC = LOC
_NTE = NTE
_PRT = PRT
_PSL = PSL
_ROL = ROL


class EHC_E01_PRODUCT_SERVICE_LINE_ITEM(HL7Model):
    """HL7 v2 EHC_E01.PRODUCT_SERVICE_LINE_ITEM group.

    Attributes:
        PSL (PSL): Product/Service Line Item, required
        NTE (Optional[List[NTE]]): Notes and Comments, optional
        ADJ (Optional[List[ADJ]]): Adjustment, optional
        AUT (Optional[AUT]): Authorization Information, optional
        LOC (Optional[List[LOC]]): Location Identification, optional
        PRT (Optional[List[PRT]]): Participation Information, optional
        ROL (Optional[List[ROL]]): Role, optional
    """

    PSL: _PSL = Field(
        title="PSL",
        description="Product/Service Line Item",
    )

    NTE: Optional[List[_NTE]] = Field(
        default=None,
        title="NTE",
        description="Notes and Comments",
    )

    ADJ: Optional[List[_ADJ]] = Field(
        default=None,
        title="ADJ",
        description="Adjustment",
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

    PRT: Optional[List[_PRT]] = Field(
        default=None,
        title="PRT",
        description="Participation Information",
    )

    ROL: Optional[List[_ROL]] = Field(
        default=None,
        title="ROL",
        description="Role",
    )

    model_config = ConfigDict(populate_by_name=True)

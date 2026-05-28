"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8
Class: EHC_E01.PRODUCT_SERVICE_LINE_ITEM
Type: Group
"""

from __future__ import annotations

from pydantic import BaseModel, Field

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


class EHC_E01_PRODUCT_SERVICE_LINE_ITEM(BaseModel):
    """HL7 v2 EHC_E01.PRODUCT_SERVICE_LINE_ITEM group.

    Attributes:
        PSL (PSL): required
        NTE (Optional[List[NTE]]): optional
        ADJ (Optional[List[ADJ]]): optional
        AUT (Optional[AUT]): optional
        LOC (Optional[List[LOC]]): optional
        PRT (Optional[List[PRT]]): optional
        ROL (Optional[List[ROL]]): optional
    """

    PSL: _PSL = Field(
        default=...,
        title="PSL",
        description="Required",
    )

    NTE: list[_NTE] | None = Field(
        default=None,
        title="NTE",
        description="Optional, repeating",
    )

    ADJ: list[_ADJ] | None = Field(
        default=None,
        title="ADJ",
        description="Optional, repeating",
    )

    AUT: _AUT | None = Field(
        default=None,
        title="AUT",
        description="Optional",
    )

    LOC: list[_LOC] | None = Field(
        default=None,
        title="LOC",
        description="Optional, repeating",
    )

    PRT: list[_PRT] | None = Field(
        default=None,
        title="PRT",
        description="Optional, repeating",
    )

    ROL: list[_ROL] | None = Field(
        default=None,
        title="ROL",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}

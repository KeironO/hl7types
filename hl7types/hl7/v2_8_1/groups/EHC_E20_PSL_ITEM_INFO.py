"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.1
Class: EHC_E20.PSL_ITEM_INFO
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.ADJ import ADJ
from ..segments.LOC import LOC
from ..segments.NTE import NTE
from ..segments.PRT import PRT
from ..segments.PSL import PSL
from ..segments.ROL import ROL

_ADJ = ADJ
_LOC = LOC
_NTE = NTE
_PRT = PRT
_PSL = PSL
_ROL = ROL


class EHC_E20_PSL_ITEM_INFO(HL7Model):
    """HL7 v2 EHC_E20.PSL_ITEM_INFO group.

    Attributes:
        PSL (PSL): required
        NTE (Optional[List[NTE]]): optional
        ADJ (Optional[List[ADJ]]): optional
        LOC (Optional[List[LOC]]): optional
        PRT (Optional[List[PRT]]): optional
        ROL (Optional[List[ROL]]): optional
    """

    PSL: _PSL = Field(
        title="PSL",
        description="Required",
    )

    NTE: Optional[List[_NTE]] = Field(
        default=None,
        title="NTE",
        description="Optional, repeating",
    )

    ADJ: Optional[List[_ADJ]] = Field(
        default=None,
        title="ADJ",
        description="Optional, repeating",
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

    model_config = {"populate_by_name": True}

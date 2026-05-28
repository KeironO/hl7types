"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.6
Class: EHC_E20.PSL_ITEM_INFO
Type: Group
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..segments.ADJ import ADJ
from ..segments.LOC import LOC
from ..segments.NTE import NTE
from ..segments.PSL import PSL
from ..segments.ROL import ROL

_ADJ = ADJ
_LOC = LOC
_NTE = NTE
_PSL = PSL
_ROL = ROL


class EHC_E20_PSL_ITEM_INFO(BaseModel):
    """HL7 v2 EHC_E20.PSL_ITEM_INFO group.

    Attributes:
        PSL (PSL): required
        NTE (Optional[List[NTE]]): optional
        ADJ (Optional[List[ADJ]]): optional
        LOC (Optional[List[LOC]]): optional
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

    LOC: list[_LOC] | None = Field(
        default=None,
        title="LOC",
        description="Optional, repeating",
    )

    ROL: list[_ROL] | None = Field(
        default=None,
        title="ROL",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}

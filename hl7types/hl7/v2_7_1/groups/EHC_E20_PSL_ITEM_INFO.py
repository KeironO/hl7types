"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7.1
Class: EHC_E20.PSL_ITEM_INFO
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import ConfigDict, Field
from hl7types.hl7 import HL7Model

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


class EHC_E20_PSL_ITEM_INFO(HL7Model):
    """HL7 v2 EHC_E20.PSL_ITEM_INFO group.

    Attributes:
        PSL (PSL): Product/Service Line Item, required
        NTE (Optional[List[NTE]]): Notes and Comments, optional
        ADJ (Optional[List[ADJ]]): Adjustment, optional
        LOC (Optional[List[LOC]]): Location Identification, optional
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

    model_config = ConfigDict(populate_by_name=True)

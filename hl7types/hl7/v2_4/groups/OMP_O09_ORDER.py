"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.4
Class: OMP_O09.ORDER
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import ConfigDict, Field
from hl7types.hl7 import HL7Model

from ..segments.BLG import BLG
from ..segments.FT1 import FT1
from ..segments.NTE import NTE
from ..segments.ORC import ORC
from ..segments.RXO import RXO
from ..segments.RXR import RXR

from .OMP_O09_COMPONENT import OMP_O09_COMPONENT
from .OMP_O09_OBSERVATION import OMP_O09_OBSERVATION

_BLG = BLG
_FT1 = FT1
_NTE = NTE
_OMP_O09_COMPONENT = OMP_O09_COMPONENT
_OMP_O09_OBSERVATION = OMP_O09_OBSERVATION
_ORC = ORC
_RXO = RXO
_RXR = RXR


class OMP_O09_ORDER(HL7Model):
    """HL7 v2 OMP_O09.ORDER group.

    Attributes:
        ORC (ORC): Common Order, required
        RXO (RXO): Pharmacy/Treatment Order, required
        NTE (Optional[List[NTE]]): Notes and Comments, optional
        RXR (List[RXR]): Pharmacy/Treatment Route, required
        COMPONENT (Optional[OMP_O09_COMPONENT]): optional
        OBSERVATION (Optional[List[OMP_O09_OBSERVATION]]): optional
        FT1 (Optional[List[FT1]]): Financial Transaction, optional
        BLG (Optional[BLG]): Billing, optional
    """

    ORC: _ORC = Field(
        title="ORC",
        description="Common Order",
    )

    RXO: _RXO = Field(
        title="RXO",
        description="Pharmacy/Treatment Order",
    )

    NTE: Optional[List[_NTE]] = Field(
        default=None,
        title="NTE",
        description="Notes and Comments",
    )

    RXR: List[_RXR] = Field(
        min_length=1,
        title="RXR",
        description="Pharmacy/Treatment Route",
    )

    COMPONENT: Optional[_OMP_O09_COMPONENT] = Field(
        default=None,
        title="COMPONENT",
    )

    OBSERVATION: Optional[List[_OMP_O09_OBSERVATION]] = Field(
        default=None,
        title="OBSERVATION",
    )

    FT1: Optional[List[_FT1]] = Field(
        default=None,
        title="FT1",
        description="Financial Transaction",
    )

    BLG: Optional[_BLG] = Field(
        default=None,
        title="BLG",
        description="Billing",
    )

    model_config = ConfigDict(populate_by_name=True)

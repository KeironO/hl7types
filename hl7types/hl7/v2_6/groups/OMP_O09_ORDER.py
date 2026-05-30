"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.6
Class: OMP_O09.ORDER
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.BLG import BLG
from ..segments.FT1 import FT1
from ..segments.NTE import NTE
from ..segments.ORC import ORC
from ..segments.RXO import RXO
from ..segments.RXR import RXR

from .OMP_O09_COMPONENT import OMP_O09_COMPONENT
from .OMP_O09_OBSERVATION import OMP_O09_OBSERVATION
from .OMP_O09_TIMING import OMP_O09_TIMING

_BLG = BLG
_FT1 = FT1
_NTE = NTE
_OMP_O09_COMPONENT = OMP_O09_COMPONENT
_OMP_O09_OBSERVATION = OMP_O09_OBSERVATION
_OMP_O09_TIMING = OMP_O09_TIMING
_ORC = ORC
_RXO = RXO
_RXR = RXR


class OMP_O09_ORDER(HL7Model):
    """HL7 v2 OMP_O09.ORDER group.

    Attributes:
        ORC (ORC): required
        TIMING (Optional[List[OMP_O09_TIMING]]): optional
        RXO (RXO): required
        NTE (Optional[List[NTE]]): optional
        RXR (List[RXR]): required
        COMPONENT (Optional[List[OMP_O09_COMPONENT]]): optional
        OBSERVATION (Optional[List[OMP_O09_OBSERVATION]]): optional
        FT1 (Optional[List[FT1]]): optional
        BLG (Optional[BLG]): optional
    """

    ORC: _ORC = Field(
        default=...,
        title="ORC",
        description="Required",
    )

    TIMING: Optional[List[_OMP_O09_TIMING]] = Field(
        default=None,
        title="TIMING",
        description="Optional, repeating",
    )

    RXO: _RXO = Field(
        default=...,
        title="RXO",
        description="Required",
    )

    NTE: Optional[List[_NTE]] = Field(
        default=None,
        title="NTE",
        description="Optional, repeating",
    )

    RXR: List[_RXR] = Field(
        default=...,
        title="RXR",
        description="Required, repeating",
    )

    COMPONENT: Optional[List[_OMP_O09_COMPONENT]] = Field(
        default=None,
        title="COMPONENT",
        description="Optional, repeating",
    )

    OBSERVATION: Optional[List[_OMP_O09_OBSERVATION]] = Field(
        default=None,
        title="OBSERVATION",
        description="Optional, repeating",
    )

    FT1: Optional[List[_FT1]] = Field(
        default=None,
        title="FT1",
        description="Optional, repeating",
    )

    BLG: Optional[_BLG] = Field(
        default=None,
        title="BLG",
        description="Optional",
    )

    model_config = {"populate_by_name": True}

"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8
Class: OMN_O07.ORDER
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.BLG import BLG
from ..segments.NTE import NTE
from ..segments.ORC import ORC
from ..segments.PRT import PRT
from ..segments.RQ1 import RQ1
from ..segments.RQD import RQD

from .OMN_O07_OBSERVATION import OMN_O07_OBSERVATION
from .OMN_O07_TIMING import OMN_O07_TIMING

_BLG = BLG
_NTE = NTE
_OMN_O07_OBSERVATION = OMN_O07_OBSERVATION
_OMN_O07_TIMING = OMN_O07_TIMING
_ORC = ORC
_PRT = PRT
_RQ1 = RQ1
_RQD = RQD


class OMN_O07_ORDER(HL7Model):
    """HL7 v2 OMN_O07.ORDER group.

    Attributes:
        ORC (ORC): required
        PRT (Optional[List[PRT]]): optional
        TIMING (Optional[List[OMN_O07_TIMING]]): optional
        RQD (RQD): required
        RQ1 (Optional[RQ1]): optional
        NTE (Optional[List[NTE]]): optional
        OBSERVATION (Optional[List[OMN_O07_OBSERVATION]]): optional
        BLG (Optional[BLG]): optional
    """

    ORC: _ORC = Field(
        default=...,
        title="ORC",
        description="Required",
    )

    PRT: Optional[List[_PRT]] = Field(
        default=None,
        title="PRT",
        description="Optional, repeating",
    )

    TIMING: Optional[List[_OMN_O07_TIMING]] = Field(
        default=None,
        title="TIMING",
        description="Optional, repeating",
    )

    RQD: _RQD = Field(
        default=...,
        title="RQD",
        description="Required",
    )

    RQ1: Optional[_RQ1] = Field(
        default=None,
        title="RQ1",
        description="Optional",
    )

    NTE: Optional[List[_NTE]] = Field(
        default=None,
        title="NTE",
        description="Optional, repeating",
    )

    OBSERVATION: Optional[List[_OMN_O07_OBSERVATION]] = Field(
        default=None,
        title="OBSERVATION",
        description="Optional, repeating",
    )

    BLG: Optional[_BLG] = Field(
        default=None,
        title="BLG",
        description="Optional",
    )

    model_config = {"populate_by_name": True}

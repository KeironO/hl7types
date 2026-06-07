"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.2
Class: OMB_O27.ORDER
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.BLG import BLG
from ..segments.BPO import BPO
from ..segments.DG1 import DG1
from ..segments.FT1 import FT1
from ..segments.NTE import NTE
from ..segments.ORC import ORC
from ..segments.PRT import PRT
from ..segments.SPM import SPM

from .OMB_O27_OBSERVATION import OMB_O27_OBSERVATION
from .OMB_O27_TIMING import OMB_O27_TIMING

_BLG = BLG
_BPO = BPO
_DG1 = DG1
_FT1 = FT1
_NTE = NTE
_OMB_O27_OBSERVATION = OMB_O27_OBSERVATION
_OMB_O27_TIMING = OMB_O27_TIMING
_ORC = ORC
_PRT = PRT
_SPM = SPM


class OMB_O27_ORDER(HL7Model):
    """HL7 v2 OMB_O27.ORDER group.

    Attributes:
        ORC (ORC): required
        PRT (Optional[List[PRT]]): optional
        TIMING (Optional[List[OMB_O27_TIMING]]): optional
        BPO (BPO): required
        SPM (Optional[SPM]): optional
        NTE (Optional[List[NTE]]): optional
        DG1 (Optional[List[DG1]]): optional
        OBSERVATION (Optional[List[OMB_O27_OBSERVATION]]): optional
        FT1 (Optional[List[FT1]]): optional
        BLG (Optional[BLG]): optional
    """

    ORC: _ORC = Field(
        title="ORC",
        description="Required",
    )

    PRT: Optional[List[_PRT]] = Field(
        default=None,
        title="PRT",
        description="Optional, repeating",
    )

    TIMING: Optional[List[_OMB_O27_TIMING]] = Field(
        default=None,
        title="TIMING",
        description="Optional, repeating",
    )

    BPO: _BPO = Field(
        title="BPO",
        description="Required",
    )

    SPM: Optional[_SPM] = Field(
        default=None,
        title="SPM",
        description="Optional",
    )

    NTE: Optional[List[_NTE]] = Field(
        default=None,
        title="NTE",
        description="Optional, repeating",
    )

    DG1: Optional[List[_DG1]] = Field(
        default=None,
        title="DG1",
        description="Optional, repeating",
    )

    OBSERVATION: Optional[List[_OMB_O27_OBSERVATION]] = Field(
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

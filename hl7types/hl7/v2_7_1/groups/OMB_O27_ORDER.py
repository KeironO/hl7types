"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7.1
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
_SPM = SPM


class OMB_O27_ORDER(HL7Model):
    """HL7 v2 OMB_O27.ORDER group.

    Attributes:
        ORC (ORC): Common Order, required
        TIMING (Optional[List[OMB_O27_TIMING]]): optional
        BPO (BPO): Blood product order, required
        SPM (Optional[SPM]): Specimen, optional
        NTE (Optional[List[NTE]]): Notes and Comments, optional
        DG1 (Optional[List[DG1]]): Diagnosis, optional
        OBSERVATION (Optional[List[OMB_O27_OBSERVATION]]): optional
        FT1 (Optional[List[FT1]]): Financial Transaction, optional
        BLG (Optional[BLG]): Billing, optional
    """

    ORC: _ORC = Field(
        title="ORC",
        description="Common Order",
    )

    TIMING: Optional[List[_OMB_O27_TIMING]] = Field(
        default=None,
        title="TIMING",
    )

    BPO: _BPO = Field(
        title="BPO",
        description="Blood product order",
    )

    SPM: Optional[_SPM] = Field(
        default=None,
        title="SPM",
        description="Specimen",
    )

    NTE: Optional[List[_NTE]] = Field(
        default=None,
        title="NTE",
        description="Notes and Comments",
    )

    DG1: Optional[List[_DG1]] = Field(
        default=None,
        title="DG1",
        description="Diagnosis",
    )

    OBSERVATION: Optional[List[_OMB_O27_OBSERVATION]] = Field(
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

    model_config = {"populate_by_name": True}

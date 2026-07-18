"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7
Class: OPU_R25.ORDER
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import ConfigDict, Field
from hl7types.hl7 import HL7Model

from ..segments.NTE import NTE
from ..segments.OBR import OBR
from ..segments.ORC import ORC
from ..segments.PRT import PRT

from .OPU_R25_RESULT import OPU_R25_RESULT
from .OPU_R25_TIMING_QTY import OPU_R25_TIMING_QTY

_NTE = NTE
_OBR = OBR
_OPU_R25_RESULT = OPU_R25_RESULT
_OPU_R25_TIMING_QTY = OPU_R25_TIMING_QTY
_ORC = ORC
_PRT = PRT


class OPU_R25_ORDER(HL7Model):
    """HL7 v2 OPU_R25.ORDER group.

    Attributes:
        OBR (OBR): Observation Request, required
        ORC (Optional[ORC]): Common Order, optional
        NTE (Optional[List[NTE]]): Notes and Comments, optional
        PRT (Optional[List[PRT]]): Participation Information, optional
        TIMING_QTY (Optional[List[OPU_R25_TIMING_QTY]]): optional
        RESULT (List[OPU_R25_RESULT]): required
    """

    OBR: _OBR = Field(
        title="OBR",
        description="Observation Request",
    )

    ORC: Optional[_ORC] = Field(
        default=None,
        title="ORC",
        description="Common Order",
    )

    NTE: Optional[List[_NTE]] = Field(
        default=None,
        title="NTE",
        description="Notes and Comments",
    )

    PRT: Optional[List[_PRT]] = Field(
        default=None,
        title="PRT",
        description="Participation Information",
    )

    TIMING_QTY: Optional[List[_OPU_R25_TIMING_QTY]] = Field(
        default=None,
        title="TIMING_QTY",
    )

    RESULT: List[_OPU_R25_RESULT] = Field(
        min_length=1,
        title="RESULT",
    )

    model_config = ConfigDict(populate_by_name=True)

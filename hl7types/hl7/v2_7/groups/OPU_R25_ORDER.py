"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7
Class: OPU_R25.ORDER
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import BaseModel, Field

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


class OPU_R25_ORDER(BaseModel):
    """HL7 v2 OPU_R25.ORDER group.

    Attributes:
        OBR (OBR): required
        ORC (Optional[ORC]): optional
        NTE (Optional[List[NTE]]): optional
        PRT (Optional[List[PRT]]): optional
        TIMING_QTY (Optional[List[OPU_R25_TIMING_QTY]]): optional
        RESULT (List[OPU_R25_RESULT]): required
    """

    OBR: _OBR = Field(
        default=...,
        title="OBR",
        description="Required",
    )

    ORC: Optional[_ORC] = Field(
        default=None,
        title="ORC",
        description="Optional",
    )

    NTE: Optional[List[_NTE]] = Field(
        default=None,
        title="NTE",
        description="Optional, repeating",
    )

    PRT: Optional[List[_PRT]] = Field(
        default=None,
        title="PRT",
        description="Optional, repeating",
    )

    TIMING_QTY: Optional[List[_OPU_R25_TIMING_QTY]] = Field(
        default=None,
        title="TIMING_QTY",
        description="Optional, repeating",
    )

    RESULT: List[_OPU_R25_RESULT] = Field(
        default=...,
        title="RESULT",
        description="Required, repeating",
    )

    model_config = {"populate_by_name": True}

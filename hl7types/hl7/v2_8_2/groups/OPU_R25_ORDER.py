"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.2
Class: OPU_R25.ORDER
Type: Group
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..segments.NTE import NTE
from ..segments.OBR import OBR
from ..segments.PRT import PRT
from .OPU_R25_COMMON_ORDER import OPU_R25_COMMON_ORDER
from .OPU_R25_RESULT import OPU_R25_RESULT
from .OPU_R25_TIMING_QTY import OPU_R25_TIMING_QTY

_NTE = NTE
_OBR = OBR
_OPU_R25_COMMON_ORDER = OPU_R25_COMMON_ORDER
_OPU_R25_RESULT = OPU_R25_RESULT
_OPU_R25_TIMING_QTY = OPU_R25_TIMING_QTY
_PRT = PRT


class OPU_R25_ORDER(BaseModel):
    """HL7 v2 OPU_R25.ORDER group.

    Attributes:
        OBR (OBR): required
        PRT (Optional[List[PRT]]): optional
        COMMON_ORDER (Optional[OPU_R25_COMMON_ORDER]): optional
        NTE (Optional[List[NTE]]): optional
        TIMING_QTY (Optional[List[OPU_R25_TIMING_QTY]]): optional
        RESULT (List[OPU_R25_RESULT]): required
    """

    OBR: _OBR = Field(
        default=...,
        title="OBR",
        description="Required",
    )

    PRT: list[_PRT] | None = Field(
        default=None,
        title="PRT",
        description="Optional, repeating",
    )

    COMMON_ORDER: _OPU_R25_COMMON_ORDER | None = Field(
        default=None,
        title="COMMON_ORDER",
        description="Optional",
    )

    NTE: list[_NTE] | None = Field(
        default=None,
        title="NTE",
        description="Optional, repeating",
    )

    TIMING_QTY: list[_OPU_R25_TIMING_QTY] | None = Field(
        default=None,
        title="TIMING_QTY",
        description="Optional, repeating",
    )

    RESULT: list[_OPU_R25_RESULT] = Field(
        default=...,
        title="RESULT",
        description="Required, repeating",
    )

    model_config = {"populate_by_name": True}

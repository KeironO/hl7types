"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5
Class: OUL_R23.ORDER
Type: Group
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..segments.CTI import CTI
from ..segments.NTE import NTE
from ..segments.OBR import OBR
from ..segments.ORC import ORC
from .OUL_R23_RESULT import OUL_R23_RESULT
from .OUL_R23_TIMING_QTY import OUL_R23_TIMING_QTY

_CTI = CTI
_NTE = NTE
_OBR = OBR
_ORC = ORC
_OUL_R23_RESULT = OUL_R23_RESULT
_OUL_R23_TIMING_QTY = OUL_R23_TIMING_QTY


class OUL_R23_ORDER(BaseModel):
    """HL7 v2 OUL_R23.ORDER group.

    Attributes:
        OBR (OBR): required
        ORC (Optional[ORC]): optional
        NTE (Optional[List[NTE]]): optional
        TIMING_QTY (Optional[List[OUL_R23_TIMING_QTY]]): optional
        RESULT (Optional[List[OUL_R23_RESULT]]): optional
        CTI (Optional[List[CTI]]): optional
    """

    OBR: _OBR = Field(
        default=...,
        title="OBR",
        description="Required",
    )

    ORC: _ORC | None = Field(
        default=None,
        title="ORC",
        description="Optional",
    )

    NTE: list[_NTE] | None = Field(
        default=None,
        title="NTE",
        description="Optional, repeating",
    )

    TIMING_QTY: list[_OUL_R23_TIMING_QTY] | None = Field(
        default=None,
        title="TIMING_QTY",
        description="Optional, repeating",
    )

    RESULT: list[_OUL_R23_RESULT] | None = Field(
        default=None,
        title="RESULT",
        description="Optional, repeating",
    )

    CTI: list[_CTI] | None = Field(
        default=None,
        title="CTI",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}

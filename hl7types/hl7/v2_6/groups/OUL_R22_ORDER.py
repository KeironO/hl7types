"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.6
Class: OUL_R22.ORDER
Type: Group
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..segments.CTI import CTI
from ..segments.NTE import NTE
from ..segments.OBR import OBR
from ..segments.ORC import ORC
from ..segments.ROL import ROL
from .OUL_R22_RESULT import OUL_R22_RESULT
from .OUL_R22_TIMING_QTY import OUL_R22_TIMING_QTY

_CTI = CTI
_NTE = NTE
_OBR = OBR
_ORC = ORC
_OUL_R22_RESULT = OUL_R22_RESULT
_OUL_R22_TIMING_QTY = OUL_R22_TIMING_QTY
_ROL = ROL


class OUL_R22_ORDER(BaseModel):
    """HL7 v2 OUL_R22.ORDER group.

    Attributes:
        OBR (OBR): required
        ORC (Optional[ORC]): optional
        NTE (Optional[List[NTE]]): optional
        ROL (Optional[List[ROL]]): optional
        TIMING_QTY (Optional[List[OUL_R22_TIMING_QTY]]): optional
        RESULT (Optional[List[OUL_R22_RESULT]]): optional
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

    ROL: list[_ROL] | None = Field(
        default=None,
        title="ROL",
        description="Optional, repeating",
    )

    TIMING_QTY: list[_OUL_R22_TIMING_QTY] | None = Field(
        default=None,
        title="TIMING_QTY",
        description="Optional, repeating",
    )

    RESULT: list[_OUL_R22_RESULT] | None = Field(
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

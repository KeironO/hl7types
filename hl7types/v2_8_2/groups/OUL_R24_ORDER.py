"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.2
Class: OUL_R24.ORDER
Type: Group
"""
from _future__ import annotations

from typing import Optional, List
from pydantic import BaseModel, Field

from ..segments.CTI import CTI
from ..segments.NTE import NTE
from ..segments.OBR import OBR
from ..segments.PRT import PRT

from .OUL_R24_COMMON_ORDER import OUL_R24_COMMON_ORDER
from .OUL_R24_RESULT import OUL_R24_RESULT
from .OUL_R24_SPECIMEN import OUL_R24_SPECIMEN
from .OUL_R24_TIMING_QTY import OUL_R24_TIMING_QTY

_CTI = CTI
_NTE = NTE
_OBR = OBR
_OUL_R24_COMMON_ORDER = OUL_R24_COMMON_ORDER
_OUL_R24_RESULT = OUL_R24_RESULT
_OUL_R24_SPECIMEN = OUL_R24_SPECIMEN
_OUL_R24_TIMING_QTY = OUL_R24_TIMING_QTY
_PRT = PRT


class OUL_R24_ORDER(BaseModel):
    """HL7 v2 OUL_R24.ORDER group.

    Attributes:
        OBR (OBR): required
        PRT (Optional[List[PRT]]): optional
        COMMON_ORDER (Optional[OUL_R24_COMMON_ORDER]): optional
        NTE (Optional[List[NTE]]): optional
        TIMING_QTY (Optional[List[OUL_R24_TIMING_QTY]]): optional
        SPECIMEN (Optional[List[OUL_R24_SPECIMEN]]): optional
        RESULT (Optional[List[OUL_R24_RESULT]]): optional
        CTI (Optional[List[CTI]]): optional
    """

    OBR: _OBR = Field(
        default=...,
        title="OBR",
        description="Required",
    )

    PRT: Optional[List[_PRT]] = Field(
        default=None,
        title="PRT",
        description="Optional, repeating",
    )

    COMMON_ORDER: Optional[_OUL_R24_COMMON_ORDER] = Field(
        default=None,
        title="COMMON_ORDER",
        description="Optional",
    )

    NTE: Optional[List[_NTE]] = Field(
        default=None,
        title="NTE",
        description="Optional, repeating",
    )

    TIMING_QTY: Optional[List[_OUL_R24_TIMING_QTY]] = Field(
        default=None,
        title="TIMING_QTY",
        description="Optional, repeating",
    )

    SPECIMEN: Optional[List[_OUL_R24_SPECIMEN]] = Field(
        default=None,
        title="SPECIMEN",
        description="Optional, repeating",
    )

    RESULT: Optional[List[_OUL_R24_RESULT]] = Field(
        default=None,
        title="RESULT",
        description="Optional, repeating",
    )

    CTI: Optional[List[_CTI]] = Field(
        default=None,
        title="CTI",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}

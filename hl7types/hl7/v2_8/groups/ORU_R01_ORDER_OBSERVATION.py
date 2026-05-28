"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8
Class: ORU_R01.ORDER_OBSERVATION
Type: Group
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..segments.CTD import CTD
from ..segments.CTI import CTI
from ..segments.FT1 import FT1
from ..segments.NTE import NTE
from ..segments.OBR import OBR
from ..segments.PRT import PRT
from .ORU_R01_COMMON_ORDER import ORU_R01_COMMON_ORDER
from .ORU_R01_OBSERVATION import ORU_R01_OBSERVATION
from .ORU_R01_SPECIMEN import ORU_R01_SPECIMEN
from .ORU_R01_TIMING_QTY import ORU_R01_TIMING_QTY

_CTD = CTD
_CTI = CTI
_FT1 = FT1
_NTE = NTE
_OBR = OBR
_ORU_R01_COMMON_ORDER = ORU_R01_COMMON_ORDER
_ORU_R01_OBSERVATION = ORU_R01_OBSERVATION
_ORU_R01_SPECIMEN = ORU_R01_SPECIMEN
_ORU_R01_TIMING_QTY = ORU_R01_TIMING_QTY
_PRT = PRT


class ORU_R01_ORDER_OBSERVATION(BaseModel):
    """HL7 v2 ORU_R01.ORDER_OBSERVATION group.

    Attributes:
        COMMON_ORDER (Optional[ORU_R01_COMMON_ORDER]): optional
        OBR (OBR): required
        NTE (Optional[List[NTE]]): optional
        PRT (Optional[List[PRT]]): optional
        TIMING_QTY (Optional[List[ORU_R01_TIMING_QTY]]): optional
        CTD (Optional[CTD]): optional
        OBSERVATION (Optional[List[ORU_R01_OBSERVATION]]): optional
        FT1 (Optional[List[FT1]]): optional
        CTI (Optional[List[CTI]]): optional
        SPECIMEN (Optional[List[ORU_R01_SPECIMEN]]): optional
    """

    COMMON_ORDER: _ORU_R01_COMMON_ORDER | None = Field(
        default=None,
        title="COMMON_ORDER",
        description="Optional",
    )

    OBR: _OBR = Field(
        default=...,
        title="OBR",
        description="Required",
    )

    NTE: list[_NTE] | None = Field(
        default=None,
        title="NTE",
        description="Optional, repeating",
    )

    PRT: list[_PRT] | None = Field(
        default=None,
        title="PRT",
        description="Optional, repeating",
    )

    TIMING_QTY: list[_ORU_R01_TIMING_QTY] | None = Field(
        default=None,
        title="TIMING_QTY",
        description="Optional, repeating",
    )

    CTD: _CTD | None = Field(
        default=None,
        title="CTD",
        description="Optional",
    )

    OBSERVATION: list[_ORU_R01_OBSERVATION] | None = Field(
        default=None,
        title="OBSERVATION",
        description="Optional, repeating",
    )

    FT1: list[_FT1] | None = Field(
        default=None,
        title="FT1",
        description="Optional, repeating",
    )

    CTI: list[_CTI] | None = Field(
        default=None,
        title="CTI",
        description="Optional, repeating",
    )

    SPECIMEN: list[_ORU_R01_SPECIMEN] | None = Field(
        default=None,
        title="SPECIMEN",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}

"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5.1
Class: ORU_R01.ORDER_OBSERVATION
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.CTD import CTD
from ..segments.CTI import CTI
from ..segments.FT1 import FT1
from ..segments.NTE import NTE
from ..segments.OBR import OBR
from ..segments.ORC import ORC

from .ORU_R01_OBSERVATION import ORU_R01_OBSERVATION
from .ORU_R01_SPECIMEN import ORU_R01_SPECIMEN
from .ORU_R01_TIMING_QTY import ORU_R01_TIMING_QTY

_CTD = CTD
_CTI = CTI
_FT1 = FT1
_NTE = NTE
_OBR = OBR
_ORC = ORC
_ORU_R01_OBSERVATION = ORU_R01_OBSERVATION
_ORU_R01_SPECIMEN = ORU_R01_SPECIMEN
_ORU_R01_TIMING_QTY = ORU_R01_TIMING_QTY


class ORU_R01_ORDER_OBSERVATION(HL7Model):
    """HL7 v2 ORU_R01.ORDER_OBSERVATION group.

    Attributes:
        ORC (Optional[ORC]): optional
        OBR (OBR): required
        NTE (Optional[List[NTE]]): optional
        TIMING_QTY (Optional[List[ORU_R01_TIMING_QTY]]): optional
        CTD (Optional[CTD]): optional
        OBSERVATION (Optional[List[ORU_R01_OBSERVATION]]): optional
        FT1 (Optional[List[FT1]]): optional
        CTI (Optional[List[CTI]]): optional
        SPECIMEN (Optional[List[ORU_R01_SPECIMEN]]): optional
    """

    ORC: Optional[_ORC] = Field(
        default=None,
        title="ORC",
        description="Optional",
    )

    OBR: _OBR = Field(
        default=...,
        title="OBR",
        description="Required",
    )

    NTE: Optional[List[_NTE]] = Field(
        default=None,
        title="NTE",
        description="Optional, repeating",
    )

    TIMING_QTY: Optional[List[_ORU_R01_TIMING_QTY]] = Field(
        default=None,
        title="TIMING_QTY",
        description="Optional, repeating",
    )

    CTD: Optional[_CTD] = Field(
        default=None,
        title="CTD",
        description="Optional",
    )

    OBSERVATION: Optional[List[_ORU_R01_OBSERVATION]] = Field(
        default=None,
        title="OBSERVATION",
        description="Optional, repeating",
    )

    FT1: Optional[List[_FT1]] = Field(
        default=None,
        title="FT1",
        description="Optional, repeating",
    )

    CTI: Optional[List[_CTI]] = Field(
        default=None,
        title="CTI",
        description="Optional, repeating",
    )

    SPECIMEN: Optional[List[_ORU_R01_SPECIMEN]] = Field(
        default=None,
        title="SPECIMEN",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}

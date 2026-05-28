"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5
Class: ORF_R04.ORDER
Type: Group
"""
from _future__ import annotations

from typing import Optional, List
from pydantic import BaseModel, Field

from ..segments.CTD import CTD
from ..segments.CTI import CTI
from ..segments.NTE import NTE
from ..segments.OBR import OBR
from ..segments.ORC import ORC

from .ORF_R04_OBSERVATION import ORF_R04_OBSERVATION
from .ORF_R04_TIMING_QTY import ORF_R04_TIMING_QTY

_CTD = CTD
_CTI = CTI
_NTE = NTE
_OBR = OBR
_ORC = ORC
_ORF_R04_OBSERVATION = ORF_R04_OBSERVATION
_ORF_R04_TIMING_QTY = ORF_R04_TIMING_QTY


class ORF_R04_ORDER(BaseModel):
    """HL7 v2 ORF_R04.ORDER group.

    Attributes:
        ORC (Optional[ORC]): optional
        OBR (OBR): required
        NTE (Optional[List[NTE]]): optional
        TIMING_QTY (Optional[List[ORF_R04_TIMING_QTY]]): optional
        CTD (Optional[CTD]): optional
        OBSERVATION (List[ORF_R04_OBSERVATION]): required
        CTI (Optional[List[CTI]]): optional
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

    TIMING_QTY: Optional[List[_ORF_R04_TIMING_QTY]] = Field(
        default=None,
        title="TIMING_QTY",
        description="Optional, repeating",
    )

    CTD: Optional[_CTD] = Field(
        default=None,
        title="CTD",
        description="Optional",
    )

    OBSERVATION: List[_ORF_R04_OBSERVATION] = Field(
        default=...,
        title="OBSERVATION",
        description="Required, repeating",
    )

    CTI: Optional[List[_CTI]] = Field(
        default=None,
        title="CTI",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}

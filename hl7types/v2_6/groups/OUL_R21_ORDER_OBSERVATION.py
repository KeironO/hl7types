"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.6
Class: OUL_R21.ORDER_OBSERVATION
Type: Group
"""
from _future__ import annotations

from typing import Optional, List
from pydantic import BaseModel, Field

from ..segments.CTI import CTI
from ..segments.NTE import NTE
from ..segments.OBR import OBR
from ..segments.ORC import ORC

from .OUL_R21_CONTAINER import OUL_R21_CONTAINER
from .OUL_R21_OBSERVATION import OUL_R21_OBSERVATION
from .OUL_R21_TIMING_QTY import OUL_R21_TIMING_QTY

_CTI = CTI
_NTE = NTE
_OBR = OBR
_ORC = ORC
_OUL_R21_CONTAINER = OUL_R21_CONTAINER
_OUL_R21_OBSERVATION = OUL_R21_OBSERVATION
_OUL_R21_TIMING_QTY = OUL_R21_TIMING_QTY


class OUL_R21_ORDER_OBSERVATION(BaseModel):
    """HL7 v2 OUL_R21.ORDER_OBSERVATION group.

    Attributes:
        CONTAINER (Optional[OUL_R21_CONTAINER]): optional
        ORC (Optional[ORC]): optional
        OBR (OBR): required
        NTE (Optional[List[NTE]]): optional
        TIMING_QTY (Optional[List[OUL_R21_TIMING_QTY]]): optional
        OBSERVATION (List[OUL_R21_OBSERVATION]): required
        CTI (Optional[List[CTI]]): optional
    """

    CONTAINER: Optional[_OUL_R21_CONTAINER] = Field(
        default=None,
        title="CONTAINER",
        description="Optional",
    )

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

    TIMING_QTY: Optional[List[_OUL_R21_TIMING_QTY]] = Field(
        default=None,
        title="TIMING_QTY",
        description="Optional, repeating",
    )

    OBSERVATION: List[_OUL_R21_OBSERVATION] = Field(
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

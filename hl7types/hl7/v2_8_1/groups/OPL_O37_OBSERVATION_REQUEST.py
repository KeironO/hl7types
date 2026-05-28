"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.1
Class: OPL_O37.OBSERVATION_REQUEST
Type: Group
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..segments.DG1 import DG1
from ..segments.OBR import OBR
from ..segments.ORC import ORC
from ..segments.PRT import PRT
from ..segments.TCD import TCD
from .OPL_O37_ORDER_RELATED_OBSERVATION import OPL_O37_ORDER_RELATED_OBSERVATION
from .OPL_O37_TIMING import OPL_O37_TIMING

_DG1 = DG1
_OBR = OBR
_OPL_O37_ORDER_RELATED_OBSERVATION = OPL_O37_ORDER_RELATED_OBSERVATION
_OPL_O37_TIMING = OPL_O37_TIMING
_ORC = ORC
_PRT = PRT
_TCD = TCD


class OPL_O37_OBSERVATION_REQUEST(BaseModel):
    """HL7 v2 OPL_O37.OBSERVATION_REQUEST group.

    Attributes:
        ORC (ORC): required
        PRT (Optional[List[PRT]]): optional
        OBR (OBR): required
        TIMING (Optional[List[OPL_O37_TIMING]]): optional
        TCD (Optional[TCD]): optional
        DG1 (Optional[List[DG1]]): optional
        ORDER_RELATED_OBSERVATION (Optional[List[OPL_O37_ORDER_RELATED_OBSERVATION]]): optional
    """

    ORC: _ORC = Field(
        default=...,
        title="ORC",
        description="Required",
    )

    PRT: list[_PRT] | None = Field(
        default=None,
        title="PRT",
        description="Optional, repeating",
    )

    OBR: _OBR = Field(
        default=...,
        title="OBR",
        description="Required",
    )

    TIMING: list[_OPL_O37_TIMING] | None = Field(
        default=None,
        title="TIMING",
        description="Optional, repeating",
    )

    TCD: _TCD | None = Field(
        default=None,
        title="TCD",
        description="Optional",
    )

    DG1: list[_DG1] | None = Field(
        default=None,
        title="DG1",
        description="Optional, repeating",
    )

    ORDER_RELATED_OBSERVATION: list[_OPL_O37_ORDER_RELATED_OBSERVATION] | None = Field(
        default=None,
        title="ORDER_RELATED_OBSERVATION",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}

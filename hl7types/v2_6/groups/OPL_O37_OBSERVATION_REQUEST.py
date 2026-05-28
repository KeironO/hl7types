"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.6
Class: OPL_O37.OBSERVATION_REQUEST
Type: Group
"""
from _future__ import annotations

from typing import Optional, List
from pydantic import BaseModel, Field

from ..segments.DG1 import DG1
from ..segments.OBR import OBR
from ..segments.OBX import OBX
from ..segments.ORC import ORC
from ..segments.ROL import ROL
from ..segments.TCD import TCD

from .OPL_O37_TIMING import OPL_O37_TIMING

_DG1 = DG1
_OBR = OBR
_OBX = OBX
_OPL_O37_TIMING = OPL_O37_TIMING
_ORC = ORC
_ROL = ROL
_TCD = TCD


class OPL_O37_OBSERVATION_REQUEST(BaseModel):
    """HL7 v2 OPL_O37.OBSERVATION_REQUEST group.

    Attributes:
        ORC (ORC): required
        OBR (OBR): required
        ROL (Optional[List[ROL]]): optional
        TIMING (Optional[List[OPL_O37_TIMING]]): optional
        TCD (Optional[TCD]): optional
        DG1 (Optional[List[DG1]]): optional
        OBX (Optional[List[OBX]]): optional
    """

    ORC: _ORC = Field(
        default=...,
        title="ORC",
        description="Required",
    )

    OBR: _OBR = Field(
        default=...,
        title="OBR",
        description="Required",
    )

    ROL: Optional[List[_ROL]] = Field(
        default=None,
        title="ROL",
        description="Optional, repeating",
    )

    TIMING: Optional[List[_OPL_O37_TIMING]] = Field(
        default=None,
        title="TIMING",
        description="Optional, repeating",
    )

    TCD: Optional[_TCD] = Field(
        default=None,
        title="TCD",
        description="Optional",
    )

    DG1: Optional[List[_DG1]] = Field(
        default=None,
        title="DG1",
        description="Optional, repeating",
    )

    OBX: Optional[List[_OBX]] = Field(
        default=None,
        title="OBX",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}

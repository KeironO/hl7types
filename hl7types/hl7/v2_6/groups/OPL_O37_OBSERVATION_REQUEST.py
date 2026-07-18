"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.6
Class: OPL_O37.OBSERVATION_REQUEST
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import ConfigDict, Field
from hl7types.hl7 import HL7Model

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


class OPL_O37_OBSERVATION_REQUEST(HL7Model):
    """HL7 v2 OPL_O37.OBSERVATION_REQUEST group.

    Attributes:
        ORC (ORC): Common Order, required
        OBR (OBR): Observation Request, required
        ROL (Optional[List[ROL]]): Role, optional
        TIMING (Optional[List[OPL_O37_TIMING]]): optional
        TCD (Optional[TCD]): Test Code Detail, optional
        DG1 (Optional[List[DG1]]): Diagnosis, optional
        OBX (Optional[List[OBX]]): Observation/Result, optional
    """

    ORC: _ORC = Field(
        title="ORC",
        description="Common Order",
    )

    OBR: _OBR = Field(
        title="OBR",
        description="Observation Request",
    )

    ROL: Optional[List[_ROL]] = Field(
        default=None,
        title="ROL",
        description="Role",
    )

    TIMING: Optional[List[_OPL_O37_TIMING]] = Field(
        default=None,
        title="TIMING",
    )

    TCD: Optional[_TCD] = Field(
        default=None,
        title="TCD",
        description="Test Code Detail",
    )

    DG1: Optional[List[_DG1]] = Field(
        default=None,
        title="DG1",
        description="Diagnosis",
    )

    OBX: Optional[List[_OBX]] = Field(
        default=None,
        title="OBX",
        description="Observation/Result",
    )

    model_config = ConfigDict(populate_by_name=True)

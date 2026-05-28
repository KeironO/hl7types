"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.6
Class: OPR_O38.OBSERVATION_REQUEST
Type: Group
"""
from _future__ import annotations

from typing import Optional, List
from pydantic import BaseModel, Field

from ..segments.OBR import OBR
from ..segments.ORC import ORC
from ..segments.ROL import ROL

_OBR = OBR
_ORC = ORC
_ROL = ROL


class OPR_O38_OBSERVATION_REQUEST(BaseModel):
    """HL7 v2 OPR_O38.OBSERVATION_REQUEST group.

    Attributes:
        ORC (ORC): required
        OBR (OBR): required
        ROL (Optional[List[ROL]]): optional
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

    model_config = {"populate_by_name": True}

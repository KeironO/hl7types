"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.6
Class: OPR_O38.OBSERVATION_REQUEST
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.OBR import OBR
from ..segments.ORC import ORC
from ..segments.ROL import ROL

_OBR = OBR
_ORC = ORC
_ROL = ROL


class OPR_O38_OBSERVATION_REQUEST(HL7Model):
    """HL7 v2 OPR_O38.OBSERVATION_REQUEST group.

    Attributes:
        ORC (ORC): Common Order, required
        OBR (OBR): Observation Request, required
        ROL (Optional[List[ROL]]): Role, optional
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

    model_config = {"populate_by_name": True}

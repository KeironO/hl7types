"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5
Class: OMG_O19.CONTAINER
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.OBX import OBX
from ..segments.SAC import SAC

_OBX = OBX
_SAC = SAC


class OMG_O19_CONTAINER(HL7Model):
    """HL7 v2 OMG_O19.CONTAINER group.

    Attributes:
        SAC (SAC): Specimen Container detail, required
        OBX (Optional[List[OBX]]): Observation/Result, optional
    """

    SAC: _SAC = Field(
        title="SAC",
        description="Specimen Container detail",
    )

    OBX: Optional[List[_OBX]] = Field(
        default=None,
        title="OBX",
        description="Observation/Result",
    )

    model_config = {"populate_by_name": True}

"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5.1
Class: OMG_O19.CONTAINER
Type: Group
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..segments.OBX import OBX
from ..segments.SAC import SAC

_OBX = OBX
_SAC = SAC


class OMG_O19_CONTAINER(BaseModel):
    """HL7 v2 OMG_O19.CONTAINER group.

    Attributes:
        SAC (SAC): required
        OBX (Optional[List[OBX]]): optional
    """

    SAC: _SAC = Field(
        default=...,
        title="SAC",
        description="Required",
    )

    OBX: list[_OBX] | None = Field(
        default=None,
        title="OBX",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}

"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.4
Class: SSU_U03.SPECIMEN_CONTAINER
Type: Group
"""
from __future__ import annotations

from typing import Optional
from pydantic import BaseModel, Field

from ..segments.OBX import OBX
from ..segments.SAC import SAC

_OBX = OBX
_SAC = SAC


class SSU_U03_SPECIMEN_CONTAINER(BaseModel):
    """HL7 v2 SSU_U03.SPECIMEN_CONTAINER group.

    Attributes:
        SAC (SAC): required
        OBX (Optional[OBX]): optional
    """

    SAC: _SAC = Field(
        default=...,
        title="SAC",
        description="Required",
    )

    OBX: Optional[_OBX] = Field(
        default=None,
        title="OBX",
        description="Optional",
    )

    model_config = {"populate_by_name": True}

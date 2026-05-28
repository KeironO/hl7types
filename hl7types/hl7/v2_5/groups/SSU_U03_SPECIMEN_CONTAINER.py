"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5
Class: SSU_U03.SPECIMEN_CONTAINER
Type: Group
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..segments.OBX import OBX
from ..segments.SAC import SAC
from .SSU_U03_SPECIMEN import SSU_U03_SPECIMEN

_OBX = OBX
_SAC = SAC
_SSU_U03_SPECIMEN = SSU_U03_SPECIMEN


class SSU_U03_SPECIMEN_CONTAINER(BaseModel):
    """HL7 v2 SSU_U03.SPECIMEN_CONTAINER group.

    Attributes:
        SAC (SAC): required
        OBX (Optional[List[OBX]]): optional
        SPECIMEN (Optional[List[SSU_U03_SPECIMEN]]): optional
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

    SPECIMEN: list[_SSU_U03_SPECIMEN] | None = Field(
        default=None,
        title="SPECIMEN",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}

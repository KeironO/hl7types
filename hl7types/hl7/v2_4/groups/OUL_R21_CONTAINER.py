"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.4
Class: OUL_R21.CONTAINER
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import BaseModel, Field

from ..segments.OBX import OBX
from ..segments.SAC import SAC
from ..segments.SID import SID

_OBX = OBX
_SAC = SAC
_SID = SID


class OUL_R21_CONTAINER(BaseModel):
    """HL7 v2 OUL_R21.CONTAINER group.

    Attributes:
        SAC (SAC): required
        SID (Optional[SID]): optional
        OBX (Optional[List[OBX]]): optional
    """

    SAC: _SAC = Field(
        default=...,
        title="SAC",
        description="Required",
    )

    SID: Optional[_SID] = Field(
        default=None,
        title="SID",
        description="Optional",
    )

    OBX: Optional[List[_OBX]] = Field(
        default=None,
        title="OBX",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}

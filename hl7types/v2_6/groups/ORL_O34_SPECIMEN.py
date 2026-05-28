"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.6
Class: ORL_O34.SPECIMEN
Type: Group
"""
from _future__ import annotations

from typing import Optional, List
from pydantic import BaseModel, Field

from ..segments.OBX import OBX
from ..segments.SAC import SAC
from ..segments.SPM import SPM

from .ORL_O34_ORDER import ORL_O34_ORDER

_OBX = OBX
_ORL_O34_ORDER = ORL_O34_ORDER
_SAC = SAC
_SPM = SPM


class ORL_O34_SPECIMEN(BaseModel):
    """HL7 v2 ORL_O34.SPECIMEN group.

    Attributes:
        SPM (SPM): required
        OBX (Optional[List[OBX]]): optional
        SAC (Optional[List[SAC]]): optional
        ORDER (Optional[List[ORL_O34_ORDER]]): optional
    """

    SPM: _SPM = Field(
        default=...,
        title="SPM",
        description="Required",
    )

    OBX: Optional[List[_OBX]] = Field(
        default=None,
        title="OBX",
        description="Optional, repeating",
    )

    SAC: Optional[List[_SAC]] = Field(
        default=None,
        title="SAC",
        description="Optional, repeating",
    )

    ORDER: Optional[List[_ORL_O34_ORDER]] = Field(
        default=None,
        title="ORDER",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}

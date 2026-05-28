"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8
Class: ORG_O20.OBSERVATION_GROUP
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import BaseModel, Field

from ..segments.OBR import OBR
from ..segments.PRT import PRT

_OBR = OBR
_PRT = PRT


class ORG_O20_OBSERVATION_GROUP(BaseModel):
    """HL7 v2 ORG_O20.OBSERVATION_GROUP group.

    Attributes:
        OBR (OBR): required
        PRT (Optional[List[PRT]]): optional
    """

    OBR: _OBR = Field(
        default=...,
        title="OBR",
        description="Required",
    )

    PRT: Optional[List[_PRT]] = Field(
        default=None,
        title="PRT",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}

"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.1
Class: ORG_O20.OBSERVATION_GROUP
Type: Group
"""
from _future__ import annotations

from typing import Optional
from pydantic import BaseModel, Field

from ..segments.OBR import OBR

_OBR = OBR


class ORG_O20_OBSERVATION_GROUP(BaseModel):
    """HL7 v2 ORG_O20.OBSERVATION_GROUP group.

    Attributes:
        OBR (OBR): required
    """

    OBR: _OBR = Field(
        default=...,
        title="OBR",
        description="Required",
    )

    model_config = {"populate_by_name": True}

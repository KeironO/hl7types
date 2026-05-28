"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5
Class: ORL_O36.OBSERVATION_REQUEST
Type: Group
"""
from _future__ import annotations

from typing import Optional
from pydantic import BaseModel, Field

from ..segments.OBR import OBR

_OBR = OBR


class ORL_O36_OBSERVATION_REQUEST(BaseModel):
    """HL7 v2 ORL_O36.OBSERVATION_REQUEST group.

    Attributes:
        OBR (OBR): required
    """

    OBR: _OBR = Field(
        default=...,
        title="OBR",
        description="Required",
    )

    model_config = {"populate_by_name": True}

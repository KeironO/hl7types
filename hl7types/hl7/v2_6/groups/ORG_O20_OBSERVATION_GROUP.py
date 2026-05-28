"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.6
Class: ORG_O20.OBSERVATION_GROUP
Type: Group
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..segments.OBR import OBR
from ..segments.ROL import ROL

_OBR = OBR
_ROL = ROL


class ORG_O20_OBSERVATION_GROUP(BaseModel):
    """HL7 v2 ORG_O20.OBSERVATION_GROUP group.

    Attributes:
        OBR (OBR): required
        ROL (Optional[List[ROL]]): optional
    """

    OBR: _OBR = Field(
        default=...,
        title="OBR",
        description="Required",
    )

    ROL: list[_ROL] | None = Field(
        default=None,
        title="ROL",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}

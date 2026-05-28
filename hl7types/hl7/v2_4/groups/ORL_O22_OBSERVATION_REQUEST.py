"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.4
Class: ORL_O22.OBSERVATION_REQUEST
Type: Group
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..segments.OBR import OBR
from ..segments.SAC import SAC

_OBR = OBR
_SAC = SAC


class ORL_O22_OBSERVATION_REQUEST(BaseModel):
    """HL7 v2 ORL_O22.OBSERVATION_REQUEST group.

    Attributes:
        OBR (OBR): required
        SAC (Optional[List[SAC]]): optional
    """

    OBR: _OBR = Field(
        default=...,
        title="OBR",
        description="Required",
    )

    SAC: list[_SAC] | None = Field(
        default=None,
        title="SAC",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}

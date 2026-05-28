"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5.1
Class: ORL_O22.OBSERVATION_REQUEST
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import BaseModel, Field

from ..segments.OBR import OBR

from .ORL_O22_SPECIMEN import ORL_O22_SPECIMEN

_OBR = OBR
_ORL_O22_SPECIMEN = ORL_O22_SPECIMEN


class ORL_O22_OBSERVATION_REQUEST(BaseModel):
    """HL7 v2 ORL_O22.OBSERVATION_REQUEST group.

    Attributes:
        OBR (OBR): required
        SPECIMEN (Optional[List[ORL_O22_SPECIMEN]]): optional
    """

    OBR: _OBR = Field(
        default=...,
        title="OBR",
        description="Required",
    )

    SPECIMEN: Optional[List[_ORL_O22_SPECIMEN]] = Field(
        default=None,
        title="SPECIMEN",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}

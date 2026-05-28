"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.1
Class: CCR_I16.CLINICAL_HISTORY_OBSERVATION
Type: Group
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..segments.OBX import OBX
from ..segments.PRT import PRT

_OBX = OBX
_PRT = PRT


class CCR_I16_CLINICAL_HISTORY_OBSERVATION(BaseModel):
    """HL7 v2 CCR_I16.CLINICAL_HISTORY_OBSERVATION group.

    Attributes:
        OBX (OBX): required
        PRT (Optional[List[PRT]]): optional
    """

    OBX: _OBX = Field(
        default=...,
        title="OBX",
        description="Required",
    )

    PRT: list[_PRT] | None = Field(
        default=None,
        title="PRT",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}

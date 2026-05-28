"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8
Class: CQU_I19.PROBLEM_OBSERVATION
Type: Group
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..segments.OBX import OBX
from ..segments.PRT import PRT

_OBX = OBX
_PRT = PRT


class CQU_I19_PROBLEM_OBSERVATION(BaseModel):
    """HL7 v2 CQU_I19.PROBLEM_OBSERVATION group.

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

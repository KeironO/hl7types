"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5.1
Class: PPT_PCL.PROBLEM_OBSERVATION
Type: Group
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..segments.NTE import NTE
from ..segments.OBX import OBX

_NTE = NTE
_OBX = OBX


class PPT_PCL_PROBLEM_OBSERVATION(BaseModel):
    """HL7 v2 PPT_PCL.PROBLEM_OBSERVATION group.

    Attributes:
        OBX (OBX): required
        NTE (Optional[List[NTE]]): optional
    """

    OBX: _OBX = Field(
        default=...,
        title="OBX",
        description="Required",
    )

    NTE: list[_NTE] | None = Field(
        default=None,
        title="NTE",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}

"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7
Class: MFN_M16.STERILIZATION
Type: Group
"""
from _future__ import annotations

from typing import Optional, List
from pydantic import BaseModel, Field

from ..segments.NTE import NTE
from ..segments.STZ import STZ

_NTE = NTE
_STZ = STZ


class MFN_M16_STERILIZATION(BaseModel):
    """HL7 v2 MFN_M16.STERILIZATION group.

    Attributes:
        STZ (STZ): required
        NTE (Optional[List[NTE]]): optional
    """

    STZ: _STZ = Field(
        default=...,
        title="STZ",
        description="Required",
    )

    NTE: Optional[List[_NTE]] = Field(
        default=None,
        title="NTE",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}

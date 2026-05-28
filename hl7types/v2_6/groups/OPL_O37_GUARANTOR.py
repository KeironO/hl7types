"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.6
Class: OPL_O37.GUARANTOR
Type: Group
"""
from _future__ import annotations

from typing import Optional, List
from pydantic import BaseModel, Field

from ..segments.GT1 import GT1
from ..segments.NTE import NTE

_GT1 = GT1
_NTE = NTE


class OPL_O37_GUARANTOR(BaseModel):
    """HL7 v2 OPL_O37.GUARANTOR group.

    Attributes:
        GT1 (GT1): required
        NTE (Optional[List[NTE]]): optional
    """

    GT1: _GT1 = Field(
        default=...,
        title="GT1",
        description="Required",
    )

    NTE: Optional[List[_NTE]] = Field(
        default=None,
        title="NTE",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}

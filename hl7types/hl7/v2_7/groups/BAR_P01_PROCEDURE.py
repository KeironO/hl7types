"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7
Class: BAR_P01.PROCEDURE
Type: Group
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..segments.PR1 import PR1
from ..segments.ROL import ROL

_PR1 = PR1
_ROL = ROL


class BAR_P01_PROCEDURE(BaseModel):
    """HL7 v2 BAR_P01.PROCEDURE group.

    Attributes:
        PR1 (PR1): required
        ROL (Optional[List[ROL]]): optional
    """

    PR1: _PR1 = Field(
        default=...,
        title="PR1",
        description="Required",
    )

    ROL: list[_ROL] | None = Field(
        default=None,
        title="ROL",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}

"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.6
Class: BAR_P01.PROCEDURE
Type: Group
"""
from _future__ import annotations

from typing import Optional, List
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

    ROL: Optional[List[_ROL]] = Field(
        default=None,
        title="ROL",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}

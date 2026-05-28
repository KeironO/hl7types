"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3
Class: ARD_A19.PROCEDURE
Type: Group
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..segments.PR1 import PR1
from ..segments.ROL import ROL

_PR1 = PR1
_ROL = ROL


class ARD_A19_PROCEDURE(BaseModel):
    """HL7 v2 ARD_A19.PROCEDURE group.

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

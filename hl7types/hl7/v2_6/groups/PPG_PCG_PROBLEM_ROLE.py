"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.6
Class: PPG_PCG.PROBLEM_ROLE
Type: Group
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..segments.ROL import ROL
from ..segments.VAR import VAR

_ROL = ROL
_VAR = VAR


class PPG_PCG_PROBLEM_ROLE(BaseModel):
    """HL7 v2 PPG_PCG.PROBLEM_ROLE group.

    Attributes:
        ROL (ROL): required
        VAR (Optional[List[VAR]]): optional
    """

    ROL: _ROL = Field(
        default=...,
        title="ROL",
        description="Required",
    )

    VAR: list[_VAR] | None = Field(
        default=None,
        title="VAR",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}

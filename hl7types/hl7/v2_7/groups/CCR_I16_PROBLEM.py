"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7
Class: CCR_I16.PROBLEM
Type: Group
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..segments.OBX import OBX
from ..segments.PRB import PRB
from ..segments.VAR import VAR
from .CCR_I16_ROLE_PROBLEM import CCR_I16_ROLE_PROBLEM

_CCR_I16_ROLE_PROBLEM = CCR_I16_ROLE_PROBLEM
_OBX = OBX
_PRB = PRB
_VAR = VAR


class CCR_I16_PROBLEM(BaseModel):
    """HL7 v2 CCR_I16.PROBLEM group.

    Attributes:
        PRB (PRB): required
        VAR (Optional[List[VAR]]): optional
        ROLE_PROBLEM (Optional[List[CCR_I16_ROLE_PROBLEM]]): optional
        OBX (Optional[List[OBX]]): optional
    """

    PRB: _PRB = Field(
        default=...,
        title="PRB",
        description="Required",
    )

    VAR: list[_VAR] | None = Field(
        default=None,
        title="VAR",
        description="Optional, repeating",
    )

    ROLE_PROBLEM: list[_CCR_I16_ROLE_PROBLEM] | None = Field(
        default=None,
        title="ROLE_PROBLEM",
        description="Optional, repeating",
    )

    OBX: list[_OBX] | None = Field(
        default=None,
        title="OBX",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}

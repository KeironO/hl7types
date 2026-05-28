"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7
Class: CCU_I20.PROBLEM
Type: Group
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..segments.OBX import OBX
from ..segments.PRB import PRB
from ..segments.VAR import VAR
from .CCU_I20_ROLE_PROBLEM import CCU_I20_ROLE_PROBLEM

_CCU_I20_ROLE_PROBLEM = CCU_I20_ROLE_PROBLEM
_OBX = OBX
_PRB = PRB
_VAR = VAR


class CCU_I20_PROBLEM(BaseModel):
    """HL7 v2 CCU_I20.PROBLEM group.

    Attributes:
        PRB (PRB): required
        VAR (Optional[List[VAR]]): optional
        ROLE_PROBLEM (Optional[List[CCU_I20_ROLE_PROBLEM]]): optional
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

    ROLE_PROBLEM: list[_CCU_I20_ROLE_PROBLEM] | None = Field(
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

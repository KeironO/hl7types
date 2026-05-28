"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7
Class: CCI_I22.PROBLEM
Type: Group
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..segments.OBX import OBX
from ..segments.PRB import PRB
from ..segments.VAR import VAR
from .CCI_I22_ROLE_PROBLEM import CCI_I22_ROLE_PROBLEM

_CCI_I22_ROLE_PROBLEM = CCI_I22_ROLE_PROBLEM
_OBX = OBX
_PRB = PRB
_VAR = VAR


class CCI_I22_PROBLEM(BaseModel):
    """HL7 v2 CCI_I22.PROBLEM group.

    Attributes:
        PRB (PRB): required
        VAR (Optional[List[VAR]]): optional
        ROLE_PROBLEM (Optional[List[CCI_I22_ROLE_PROBLEM]]): optional
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

    ROLE_PROBLEM: list[_CCI_I22_ROLE_PROBLEM] | None = Field(
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

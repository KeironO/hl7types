"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7
Class: CQU_I19.GOAL
Type: Group
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..segments.GOL import GOL
from ..segments.OBX import OBX
from ..segments.VAR import VAR
from .CQU_I19_ROLE_GOAL import CQU_I19_ROLE_GOAL

_CQU_I19_ROLE_GOAL = CQU_I19_ROLE_GOAL
_GOL = GOL
_OBX = OBX
_VAR = VAR


class CQU_I19_GOAL(BaseModel):
    """HL7 v2 CQU_I19.GOAL group.

    Attributes:
        GOL (GOL): required
        VAR (Optional[List[VAR]]): optional
        ROLE_GOAL (Optional[List[CQU_I19_ROLE_GOAL]]): optional
        OBX (Optional[List[OBX]]): optional
    """

    GOL: _GOL = Field(
        default=...,
        title="GOL",
        description="Required",
    )

    VAR: list[_VAR] | None = Field(
        default=None,
        title="VAR",
        description="Optional, repeating",
    )

    ROLE_GOAL: list[_CQU_I19_ROLE_GOAL] | None = Field(
        default=None,
        title="ROLE_GOAL",
        description="Optional, repeating",
    )

    OBX: list[_OBX] | None = Field(
        default=None,
        title="OBX",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}

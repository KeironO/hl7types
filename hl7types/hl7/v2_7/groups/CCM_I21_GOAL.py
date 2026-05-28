"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7
Class: CCM_I21.GOAL
Type: Group
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..segments.GOL import GOL
from ..segments.OBX import OBX
from ..segments.VAR import VAR
from .CCM_I21_ROLE_GOAL import CCM_I21_ROLE_GOAL

_CCM_I21_ROLE_GOAL = CCM_I21_ROLE_GOAL
_GOL = GOL
_OBX = OBX
_VAR = VAR


class CCM_I21_GOAL(BaseModel):
    """HL7 v2 CCM_I21.GOAL group.

    Attributes:
        GOL (GOL): required
        VAR (Optional[List[VAR]]): optional
        ROLE_GOAL (Optional[List[CCM_I21_ROLE_GOAL]]): optional
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

    ROLE_GOAL: list[_CCM_I21_ROLE_GOAL] | None = Field(
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

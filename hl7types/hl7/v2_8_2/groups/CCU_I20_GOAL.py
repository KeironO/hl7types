"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.2
Class: CCU_I20.GOAL
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.GOL import GOL
from ..segments.VAR import VAR

from .CCU_I20_GOAL_OBSERVATION import CCU_I20_GOAL_OBSERVATION
from .CCU_I20_ROLE_GOAL import CCU_I20_ROLE_GOAL

_CCU_I20_GOAL_OBSERVATION = CCU_I20_GOAL_OBSERVATION
_CCU_I20_ROLE_GOAL = CCU_I20_ROLE_GOAL
_GOL = GOL
_VAR = VAR


class CCU_I20_GOAL(HL7Model):
    """HL7 v2 CCU_I20.GOAL group.

    Attributes:
        GOL (GOL): required
        VAR (Optional[List[VAR]]): optional
        ROLE_GOAL (Optional[List[CCU_I20_ROLE_GOAL]]): optional
        GOAL_OBSERVATION (Optional[List[CCU_I20_GOAL_OBSERVATION]]): optional
    """

    GOL: _GOL = Field(
        title="GOL",
        description="Required",
    )

    VAR: Optional[List[_VAR]] = Field(
        default=None,
        title="VAR",
        description="Optional, repeating",
    )

    ROLE_GOAL: Optional[List[_CCU_I20_ROLE_GOAL]] = Field(
        default=None,
        title="ROLE_GOAL",
        description="Optional, repeating",
    )

    GOAL_OBSERVATION: Optional[List[_CCU_I20_GOAL_OBSERVATION]] = Field(
        default=None,
        title="GOAL_OBSERVATION",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}

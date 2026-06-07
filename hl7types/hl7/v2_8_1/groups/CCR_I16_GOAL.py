"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.1
Class: CCR_I16.GOAL
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.GOL import GOL
from ..segments.VAR import VAR

from .CCR_I16_GOAL_OBSERVATION import CCR_I16_GOAL_OBSERVATION
from .CCR_I16_ROLE_GOAL import CCR_I16_ROLE_GOAL

_CCR_I16_GOAL_OBSERVATION = CCR_I16_GOAL_OBSERVATION
_CCR_I16_ROLE_GOAL = CCR_I16_ROLE_GOAL
_GOL = GOL
_VAR = VAR


class CCR_I16_GOAL(HL7Model):
    """HL7 v2 CCR_I16.GOAL group.

    Attributes:
        GOL (GOL): required
        VAR (Optional[List[VAR]]): optional
        ROLE_GOAL (Optional[List[CCR_I16_ROLE_GOAL]]): optional
        GOAL_OBSERVATION (Optional[List[CCR_I16_GOAL_OBSERVATION]]): optional
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

    ROLE_GOAL: Optional[List[_CCR_I16_ROLE_GOAL]] = Field(
        default=None,
        title="ROLE_GOAL",
        description="Optional, repeating",
    )

    GOAL_OBSERVATION: Optional[List[_CCR_I16_GOAL_OBSERVATION]] = Field(
        default=None,
        title="GOAL_OBSERVATION",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}

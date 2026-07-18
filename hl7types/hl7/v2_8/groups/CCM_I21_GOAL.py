"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8
Class: CCM_I21.GOAL
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import ConfigDict, Field
from hl7types.hl7 import HL7Model

from ..segments.GOL import GOL
from ..segments.VAR import VAR

from .CCM_I21_GOAL_OBSERVATION import CCM_I21_GOAL_OBSERVATION
from .CCM_I21_ROLE_GOAL import CCM_I21_ROLE_GOAL

_CCM_I21_GOAL_OBSERVATION = CCM_I21_GOAL_OBSERVATION
_CCM_I21_ROLE_GOAL = CCM_I21_ROLE_GOAL
_GOL = GOL
_VAR = VAR


class CCM_I21_GOAL(HL7Model):
    """HL7 v2 CCM_I21.GOAL group.

    Attributes:
        GOL (GOL): Goal Detail, required
        VAR (Optional[List[VAR]]): Variance, optional
        ROLE_GOAL (Optional[List[CCM_I21_ROLE_GOAL]]): optional
        GOAL_OBSERVATION (Optional[List[CCM_I21_GOAL_OBSERVATION]]): optional
    """

    GOL: _GOL = Field(
        title="GOL",
        description="Goal Detail",
    )

    VAR: Optional[List[_VAR]] = Field(
        default=None,
        title="VAR",
        description="Variance",
    )

    ROLE_GOAL: Optional[List[_CCM_I21_ROLE_GOAL]] = Field(
        default=None,
        title="ROLE_GOAL",
    )

    GOAL_OBSERVATION: Optional[List[_CCM_I21_GOAL_OBSERVATION]] = Field(
        default=None,
        title="GOAL_OBSERVATION",
    )

    model_config = ConfigDict(populate_by_name=True)

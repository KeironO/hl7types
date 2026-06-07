"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.6
Class: PPG_PCG.GOAL
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.GOL import GOL
from ..segments.NTE import NTE
from ..segments.VAR import VAR

from .PPG_PCG_GOAL_OBSERVATION import PPG_PCG_GOAL_OBSERVATION
from .PPG_PCG_GOAL_ROLE import PPG_PCG_GOAL_ROLE
from .PPG_PCG_ORDER import PPG_PCG_ORDER
from .PPG_PCG_PROBLEM import PPG_PCG_PROBLEM

_GOL = GOL
_NTE = NTE
_PPG_PCG_GOAL_OBSERVATION = PPG_PCG_GOAL_OBSERVATION
_PPG_PCG_GOAL_ROLE = PPG_PCG_GOAL_ROLE
_PPG_PCG_ORDER = PPG_PCG_ORDER
_PPG_PCG_PROBLEM = PPG_PCG_PROBLEM
_VAR = VAR


class PPG_PCG_GOAL(HL7Model):
    """HL7 v2 PPG_PCG.GOAL group.

    Attributes:
        GOL (GOL): required
        NTE (Optional[List[NTE]]): optional
        VAR (Optional[List[VAR]]): optional
        GOAL_ROLE (Optional[List[PPG_PCG_GOAL_ROLE]]): optional
        GOAL_OBSERVATION (Optional[List[PPG_PCG_GOAL_OBSERVATION]]): optional
        PROBLEM (Optional[List[PPG_PCG_PROBLEM]]): optional
        ORDER (Optional[List[PPG_PCG_ORDER]]): optional
    """

    GOL: _GOL = Field(
        title="GOL",
        description="Required",
    )

    NTE: Optional[List[_NTE]] = Field(
        default=None,
        title="NTE",
        description="Optional, repeating",
    )

    VAR: Optional[List[_VAR]] = Field(
        default=None,
        title="VAR",
        description="Optional, repeating",
    )

    GOAL_ROLE: Optional[List[_PPG_PCG_GOAL_ROLE]] = Field(
        default=None,
        title="GOAL_ROLE",
        description="Optional, repeating",
    )

    GOAL_OBSERVATION: Optional[List[_PPG_PCG_GOAL_OBSERVATION]] = Field(
        default=None,
        title="GOAL_OBSERVATION",
        description="Optional, repeating",
    )

    PROBLEM: Optional[List[_PPG_PCG_PROBLEM]] = Field(
        default=None,
        title="PROBLEM",
        description="Optional, repeating",
    )

    ORDER: Optional[List[_PPG_PCG_ORDER]] = Field(
        default=None,
        title="ORDER",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}

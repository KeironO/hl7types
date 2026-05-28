"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5.1
Class: PPT_PCL.GOAL
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import BaseModel, Field

from ..segments.GOL import GOL
from ..segments.NTE import NTE
from ..segments.VAR import VAR

from .PPT_PCL_GOAL_OBSERVATION import PPT_PCL_GOAL_OBSERVATION
from .PPT_PCL_GOAL_ROLE import PPT_PCL_GOAL_ROLE
from .PPT_PCL_ORDER import PPT_PCL_ORDER
from .PPT_PCL_PROBLEM import PPT_PCL_PROBLEM

_GOL = GOL
_NTE = NTE
_PPT_PCL_GOAL_OBSERVATION = PPT_PCL_GOAL_OBSERVATION
_PPT_PCL_GOAL_ROLE = PPT_PCL_GOAL_ROLE
_PPT_PCL_ORDER = PPT_PCL_ORDER
_PPT_PCL_PROBLEM = PPT_PCL_PROBLEM
_VAR = VAR


class PPT_PCL_GOAL(BaseModel):
    """HL7 v2 PPT_PCL.GOAL group.

    Attributes:
        GOL (GOL): required
        NTE (Optional[List[NTE]]): optional
        VAR (Optional[List[VAR]]): optional
        GOAL_ROLE (Optional[List[PPT_PCL_GOAL_ROLE]]): optional
        GOAL_OBSERVATION (Optional[List[PPT_PCL_GOAL_OBSERVATION]]): optional
        PROBLEM (Optional[List[PPT_PCL_PROBLEM]]): optional
        ORDER (Optional[List[PPT_PCL_ORDER]]): optional
    """

    GOL: _GOL = Field(
        default=...,
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

    GOAL_ROLE: Optional[List[_PPT_PCL_GOAL_ROLE]] = Field(
        default=None,
        title="GOAL_ROLE",
        description="Optional, repeating",
    )

    GOAL_OBSERVATION: Optional[List[_PPT_PCL_GOAL_OBSERVATION]] = Field(
        default=None,
        title="GOAL_OBSERVATION",
        description="Optional, repeating",
    )

    PROBLEM: Optional[List[_PPT_PCL_PROBLEM]] = Field(
        default=None,
        title="PROBLEM",
        description="Optional, repeating",
    )

    ORDER: Optional[List[_PPT_PCL_ORDER]] = Field(
        default=None,
        title="ORDER",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}

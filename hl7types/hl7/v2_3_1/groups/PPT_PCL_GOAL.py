"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3.1
Class: PPT_PCL.GOAL
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import ConfigDict, Field
from hl7types.hl7 import HL7Model

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


class PPT_PCL_GOAL(HL7Model):
    """HL7 v2 PPT_PCL.GOAL group.

    Attributes:
        GOL (GOL): Goal Detail, required
        NTE (Optional[List[NTE]]): NTE - notes and comments segment, optional
        VAR (Optional[List[VAR]]): Variance, optional
        GOAL_ROLE (Optional[List[PPT_PCL_GOAL_ROLE]]): optional
        GOAL_OBSERVATION (Optional[List[PPT_PCL_GOAL_OBSERVATION]]): optional
        PROBLEM (Optional[List[PPT_PCL_PROBLEM]]): optional
        ORDER (Optional[List[PPT_PCL_ORDER]]): optional
    """

    GOL: _GOL = Field(
        title="GOL",
        description="Goal Detail",
    )

    NTE: Optional[List[_NTE]] = Field(
        default=None,
        title="NTE",
        description="NTE - notes and comments segment",
    )

    VAR: Optional[List[_VAR]] = Field(
        default=None,
        title="VAR",
        description="Variance",
    )

    GOAL_ROLE: Optional[List[_PPT_PCL_GOAL_ROLE]] = Field(
        default=None,
        title="GOAL_ROLE",
    )

    GOAL_OBSERVATION: Optional[List[_PPT_PCL_GOAL_OBSERVATION]] = Field(
        default=None,
        title="GOAL_OBSERVATION",
    )

    PROBLEM: Optional[List[_PPT_PCL_PROBLEM]] = Field(
        default=None,
        title="PROBLEM",
    )

    ORDER: Optional[List[_PPT_PCL_ORDER]] = Field(
        default=None,
        title="ORDER",
    )

    model_config = ConfigDict(populate_by_name=True)

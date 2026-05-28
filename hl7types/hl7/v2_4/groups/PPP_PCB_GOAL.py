"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.4
Class: PPP_PCB.GOAL
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import BaseModel, Field

from ..segments.GOL import GOL
from ..segments.NTE import NTE
from ..segments.VAR import VAR

from .PPP_PCB_GOAL_OBSERVATION import PPP_PCB_GOAL_OBSERVATION
from .PPP_PCB_GOAL_ROLE import PPP_PCB_GOAL_ROLE

_GOL = GOL
_NTE = NTE
_PPP_PCB_GOAL_OBSERVATION = PPP_PCB_GOAL_OBSERVATION
_PPP_PCB_GOAL_ROLE = PPP_PCB_GOAL_ROLE
_VAR = VAR


class PPP_PCB_GOAL(BaseModel):
    """HL7 v2 PPP_PCB.GOAL group.

    Attributes:
        GOL (GOL): required
        NTE (Optional[List[NTE]]): optional
        VAR (Optional[List[VAR]]): optional
        GOAL_ROLE (Optional[List[PPP_PCB_GOAL_ROLE]]): optional
        GOAL_OBSERVATION (Optional[List[PPP_PCB_GOAL_OBSERVATION]]): optional
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

    GOAL_ROLE: Optional[List[_PPP_PCB_GOAL_ROLE]] = Field(
        default=None,
        title="GOAL_ROLE",
        description="Optional, repeating",
    )

    GOAL_OBSERVATION: Optional[List[_PPP_PCB_GOAL_OBSERVATION]] = Field(
        default=None,
        title="GOAL_OBSERVATION",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}

"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5
Class: PGL_PC6.GOAL
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import BaseModel, Field

from ..segments.GOL import GOL
from ..segments.NTE import NTE
from ..segments.VAR import VAR

from .PGL_PC6_GOAL_ROLE import PGL_PC6_GOAL_ROLE
from .PGL_PC6_OBSERVATION import PGL_PC6_OBSERVATION
from .PGL_PC6_ORDER import PGL_PC6_ORDER
from .PGL_PC6_PATHWAY import PGL_PC6_PATHWAY
from .PGL_PC6_PROBLEM import PGL_PC6_PROBLEM

_GOL = GOL
_NTE = NTE
_PGL_PC6_GOAL_ROLE = PGL_PC6_GOAL_ROLE
_PGL_PC6_OBSERVATION = PGL_PC6_OBSERVATION
_PGL_PC6_ORDER = PGL_PC6_ORDER
_PGL_PC6_PATHWAY = PGL_PC6_PATHWAY
_PGL_PC6_PROBLEM = PGL_PC6_PROBLEM
_VAR = VAR


class PGL_PC6_GOAL(BaseModel):
    """HL7 v2 PGL_PC6.GOAL group.

    Attributes:
        GOL (GOL): required
        NTE (Optional[List[NTE]]): optional
        VAR (Optional[List[VAR]]): optional
        GOAL_ROLE (Optional[List[PGL_PC6_GOAL_ROLE]]): optional
        PATHWAY (Optional[List[PGL_PC6_PATHWAY]]): optional
        OBSERVATION (Optional[List[PGL_PC6_OBSERVATION]]): optional
        PROBLEM (Optional[List[PGL_PC6_PROBLEM]]): optional
        ORDER (Optional[List[PGL_PC6_ORDER]]): optional
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

    GOAL_ROLE: Optional[List[_PGL_PC6_GOAL_ROLE]] = Field(
        default=None,
        title="GOAL_ROLE",
        description="Optional, repeating",
    )

    PATHWAY: Optional[List[_PGL_PC6_PATHWAY]] = Field(
        default=None,
        title="PATHWAY",
        description="Optional, repeating",
    )

    OBSERVATION: Optional[List[_PGL_PC6_OBSERVATION]] = Field(
        default=None,
        title="OBSERVATION",
        description="Optional, repeating",
    )

    PROBLEM: Optional[List[_PGL_PC6_PROBLEM]] = Field(
        default=None,
        title="PROBLEM",
        description="Optional, repeating",
    )

    ORDER: Optional[List[_PGL_PC6_ORDER]] = Field(
        default=None,
        title="ORDER",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}

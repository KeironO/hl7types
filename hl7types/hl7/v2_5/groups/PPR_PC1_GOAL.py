"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5
Class: PPR_PC1.GOAL
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.GOL import GOL
from ..segments.NTE import NTE
from ..segments.VAR import VAR

from .PPR_PC1_GOAL_OBSERVATION import PPR_PC1_GOAL_OBSERVATION
from .PPR_PC1_GOAL_ROLE import PPR_PC1_GOAL_ROLE

_GOL = GOL
_NTE = NTE
_PPR_PC1_GOAL_OBSERVATION = PPR_PC1_GOAL_OBSERVATION
_PPR_PC1_GOAL_ROLE = PPR_PC1_GOAL_ROLE
_VAR = VAR


class PPR_PC1_GOAL(HL7Model):
    """HL7 v2 PPR_PC1.GOAL group.

    Attributes:
        GOL (GOL): Goal Detail, required
        NTE (Optional[List[NTE]]): Notes and Comments, optional
        VAR (Optional[List[VAR]]): Variance, optional
        GOAL_ROLE (Optional[List[PPR_PC1_GOAL_ROLE]]): optional
        GOAL_OBSERVATION (Optional[List[PPR_PC1_GOAL_OBSERVATION]]): optional
    """

    GOL: _GOL = Field(
        title="GOL",
        description="Goal Detail",
    )

    NTE: Optional[List[_NTE]] = Field(
        default=None,
        title="NTE",
        description="Notes and Comments",
    )

    VAR: Optional[List[_VAR]] = Field(
        default=None,
        title="VAR",
        description="Variance",
    )

    GOAL_ROLE: Optional[List[_PPR_PC1_GOAL_ROLE]] = Field(
        default=None,
        title="GOAL_ROLE",
    )

    GOAL_OBSERVATION: Optional[List[_PPR_PC1_GOAL_OBSERVATION]] = Field(
        default=None,
        title="GOAL_OBSERVATION",
    )

    model_config = {"populate_by_name": True}

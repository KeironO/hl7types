"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3
Class: PRR_PC5.GOAL
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import ConfigDict, Field
from hl7types.hl7 import HL7Model

from ..segments.GOL import GOL
from ..segments.NTE import NTE
from ..segments.VAR import VAR

from .PRR_PC5_GOAL_OBSERVATION import PRR_PC5_GOAL_OBSERVATION
from .PRR_PC5_GOAL_ROLE import PRR_PC5_GOAL_ROLE

_GOL = GOL
_NTE = NTE
_PRR_PC5_GOAL_OBSERVATION = PRR_PC5_GOAL_OBSERVATION
_PRR_PC5_GOAL_ROLE = PRR_PC5_GOAL_ROLE
_VAR = VAR


class PRR_PC5_GOAL(HL7Model):
    """HL7 v2 PRR_PC5.GOAL group.

    Attributes:
        GOL (GOL): Goal Detail, required
        NTE (Optional[List[NTE]]): Notes and comments segment, optional
        VAR (Optional[List[VAR]]): Variance, optional
        GOAL_ROLE (Optional[List[PRR_PC5_GOAL_ROLE]]): optional
        GOAL_OBSERVATION (Optional[List[PRR_PC5_GOAL_OBSERVATION]]): optional
    """

    GOL: _GOL = Field(
        title="GOL",
        description="Goal Detail",
    )

    NTE: Optional[List[_NTE]] = Field(
        default=None,
        title="NTE",
        description="Notes and comments segment",
    )

    VAR: Optional[List[_VAR]] = Field(
        default=None,
        title="VAR",
        description="Variance",
    )

    GOAL_ROLE: Optional[List[_PRR_PC5_GOAL_ROLE]] = Field(
        default=None,
        title="GOAL_ROLE",
    )

    GOAL_OBSERVATION: Optional[List[_PRR_PC5_GOAL_OBSERVATION]] = Field(
        default=None,
        title="GOAL_OBSERVATION",
    )

    model_config = ConfigDict(populate_by_name=True)

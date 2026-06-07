"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.1
Class: CCI_I22.GOAL
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.GOL import GOL
from ..segments.VAR import VAR

from .CCI_I22_GOAL_OBSERVATION import CCI_I22_GOAL_OBSERVATION
from .CCI_I22_ROLE_GOAL import CCI_I22_ROLE_GOAL

_CCI_I22_GOAL_OBSERVATION = CCI_I22_GOAL_OBSERVATION
_CCI_I22_ROLE_GOAL = CCI_I22_ROLE_GOAL
_GOL = GOL
_VAR = VAR


class CCI_I22_GOAL(HL7Model):
    """HL7 v2 CCI_I22.GOAL group.

    Attributes:
        GOL (GOL): required
        VAR (Optional[List[VAR]]): optional
        ROLE_GOAL (Optional[List[CCI_I22_ROLE_GOAL]]): optional
        GOAL_OBSERVATION (Optional[List[CCI_I22_GOAL_OBSERVATION]]): optional
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

    ROLE_GOAL: Optional[List[_CCI_I22_ROLE_GOAL]] = Field(
        default=None,
        title="ROLE_GOAL",
        description="Optional, repeating",
    )

    GOAL_OBSERVATION: Optional[List[_CCI_I22_GOAL_OBSERVATION]] = Field(
        default=None,
        title="GOAL_OBSERVATION",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}

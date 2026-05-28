"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5.1
Class: PPT_PCL.PATHWAY
Type: Group
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..segments.NTE import NTE
from ..segments.PTH import PTH
from ..segments.VAR import VAR
from .PPT_PCL_GOAL import PPT_PCL_GOAL
from .PPT_PCL_PATHWAY_ROLE import PPT_PCL_PATHWAY_ROLE

_NTE = NTE
_PPT_PCL_GOAL = PPT_PCL_GOAL
_PPT_PCL_PATHWAY_ROLE = PPT_PCL_PATHWAY_ROLE
_PTH = PTH
_VAR = VAR


class PPT_PCL_PATHWAY(BaseModel):
    """HL7 v2 PPT_PCL.PATHWAY group.

    Attributes:
        PTH (PTH): required
        NTE (Optional[List[NTE]]): optional
        VAR (Optional[List[VAR]]): optional
        PATHWAY_ROLE (Optional[List[PPT_PCL_PATHWAY_ROLE]]): optional
        GOAL (Optional[List[PPT_PCL_GOAL]]): optional
    """

    PTH: _PTH = Field(
        default=...,
        title="PTH",
        description="Required",
    )

    NTE: list[_NTE] | None = Field(
        default=None,
        title="NTE",
        description="Optional, repeating",
    )

    VAR: list[_VAR] | None = Field(
        default=None,
        title="VAR",
        description="Optional, repeating",
    )

    PATHWAY_ROLE: list[_PPT_PCL_PATHWAY_ROLE] | None = Field(
        default=None,
        title="PATHWAY_ROLE",
        description="Optional, repeating",
    )

    GOAL: list[_PPT_PCL_GOAL] | None = Field(
        default=None,
        title="GOAL",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}

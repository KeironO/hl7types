"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.4
Class: PPG_PCG.PATHWAY
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.NTE import NTE
from ..segments.PTH import PTH
from ..segments.VAR import VAR

from .PPG_PCG_GOAL import PPG_PCG_GOAL
from .PPG_PCG_PATHWAY_ROLE import PPG_PCG_PATHWAY_ROLE

_NTE = NTE
_PPG_PCG_GOAL = PPG_PCG_GOAL
_PPG_PCG_PATHWAY_ROLE = PPG_PCG_PATHWAY_ROLE
_PTH = PTH
_VAR = VAR


class PPG_PCG_PATHWAY(HL7Model):
    """HL7 v2 PPG_PCG.PATHWAY group.

    Attributes:
        PTH (PTH): Pathway, required
        NTE (Optional[List[NTE]]): Notes and Comments, optional
        VAR (Optional[List[VAR]]): Variance, optional
        PATHWAY_ROLE (Optional[List[PPG_PCG_PATHWAY_ROLE]]): optional
        GOAL (Optional[List[PPG_PCG_GOAL]]): optional
    """

    PTH: _PTH = Field(
        title="PTH",
        description="Pathway",
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

    PATHWAY_ROLE: Optional[List[_PPG_PCG_PATHWAY_ROLE]] = Field(
        default=None,
        title="PATHWAY_ROLE",
    )

    GOAL: Optional[List[_PPG_PCG_GOAL]] = Field(
        default=None,
        title="GOAL",
    )

    model_config = {"populate_by_name": True}

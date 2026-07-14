"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.1
Class: PPP_PCB.PATHWAY
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.NTE import NTE
from ..segments.PTH import PTH
from ..segments.VAR import VAR

from .PPP_PCB_PATHWAY_ROLE import PPP_PCB_PATHWAY_ROLE
from .PPP_PCB_PROBLEM import PPP_PCB_PROBLEM

_NTE = NTE
_PPP_PCB_PATHWAY_ROLE = PPP_PCB_PATHWAY_ROLE
_PPP_PCB_PROBLEM = PPP_PCB_PROBLEM
_PTH = PTH
_VAR = VAR


class PPP_PCB_PATHWAY(HL7Model):
    """HL7 v2 PPP_PCB.PATHWAY group.

    Attributes:
        PTH (PTH): Pathway, required
        NTE (Optional[List[NTE]]): Notes and Comments, optional
        VAR (Optional[List[VAR]]): Variance, optional
        PATHWAY_ROLE (Optional[List[PPP_PCB_PATHWAY_ROLE]]): optional
        PROBLEM (Optional[List[PPP_PCB_PROBLEM]]): optional
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

    PATHWAY_ROLE: Optional[List[_PPP_PCB_PATHWAY_ROLE]] = Field(
        default=None,
        title="PATHWAY_ROLE",
    )

    PROBLEM: Optional[List[_PPP_PCB_PROBLEM]] = Field(
        default=None,
        title="PROBLEM",
    )

    model_config = {"populate_by_name": True}

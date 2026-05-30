"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.4
Class: PTR_PCF.PATHWAY
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.NTE import NTE
from ..segments.PTH import PTH
from ..segments.VAR import VAR

from .PTR_PCF_PATHWAY_ROLE import PTR_PCF_PATHWAY_ROLE
from .PTR_PCF_PROBLEM import PTR_PCF_PROBLEM

_NTE = NTE
_PTH = PTH
_PTR_PCF_PATHWAY_ROLE = PTR_PCF_PATHWAY_ROLE
_PTR_PCF_PROBLEM = PTR_PCF_PROBLEM
_VAR = VAR


class PTR_PCF_PATHWAY(HL7Model):
    """HL7 v2 PTR_PCF.PATHWAY group.

    Attributes:
        PTH (PTH): required
        NTE (Optional[List[NTE]]): optional
        VAR (Optional[List[VAR]]): optional
        PATHWAY_ROLE (Optional[List[PTR_PCF_PATHWAY_ROLE]]): optional
        PROBLEM (Optional[List[PTR_PCF_PROBLEM]]): optional
    """

    PTH: _PTH = Field(
        default=...,
        title="PTH",
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

    PATHWAY_ROLE: Optional[List[_PTR_PCF_PATHWAY_ROLE]] = Field(
        default=None,
        title="PATHWAY_ROLE",
        description="Optional, repeating",
    )

    PROBLEM: Optional[List[_PTR_PCF_PROBLEM]] = Field(
        default=None,
        title="PROBLEM",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}

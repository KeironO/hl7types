"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3.1
Class: PTR_PCF.PATHWAY
Type: Group
"""

from __future__ import annotations

from pydantic import BaseModel, Field

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


class PTR_PCF_PATHWAY(BaseModel):
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

    PATHWAY_ROLE: list[_PTR_PCF_PATHWAY_ROLE] | None = Field(
        default=None,
        title="PATHWAY_ROLE",
        description="Optional, repeating",
    )

    PROBLEM: list[_PTR_PCF_PROBLEM] | None = Field(
        default=None,
        title="PROBLEM",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}

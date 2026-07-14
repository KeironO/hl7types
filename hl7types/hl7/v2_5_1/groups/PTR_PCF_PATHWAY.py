"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5.1
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
        PTH (PTH): Pathway, required
        NTE (Optional[List[NTE]]): Notes and Comments, optional
        VAR (Optional[List[VAR]]): Variance, optional
        PATHWAY_ROLE (Optional[List[PTR_PCF_PATHWAY_ROLE]]): optional
        PROBLEM (Optional[List[PTR_PCF_PROBLEM]]): optional
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

    PATHWAY_ROLE: Optional[List[_PTR_PCF_PATHWAY_ROLE]] = Field(
        default=None,
        title="PATHWAY_ROLE",
    )

    PROBLEM: Optional[List[_PTR_PCF_PROBLEM]] = Field(
        default=None,
        title="PROBLEM",
    )

    model_config = {"populate_by_name": True}

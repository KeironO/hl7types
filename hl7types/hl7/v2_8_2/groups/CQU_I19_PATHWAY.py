"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.2
Class: CQU_I19.PATHWAY
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.PTH import PTH
from ..segments.VAR import VAR

from .CQU_I19_PATHWAY_OBSERVATION import CQU_I19_PATHWAY_OBSERVATION
from .CQU_I19_ROLE_PATHWAY import CQU_I19_ROLE_PATHWAY

_CQU_I19_PATHWAY_OBSERVATION = CQU_I19_PATHWAY_OBSERVATION
_CQU_I19_ROLE_PATHWAY = CQU_I19_ROLE_PATHWAY
_PTH = PTH
_VAR = VAR


class CQU_I19_PATHWAY(HL7Model):
    """HL7 v2 CQU_I19.PATHWAY group.

    Attributes:
        PTH (PTH): required
        VAR (Optional[List[VAR]]): optional
        ROLE_PATHWAY (Optional[List[CQU_I19_ROLE_PATHWAY]]): optional
        PATHWAY_OBSERVATION (Optional[List[CQU_I19_PATHWAY_OBSERVATION]]): optional
    """

    PTH: _PTH = Field(
        default=...,
        title="PTH",
        description="Required",
    )

    VAR: Optional[List[_VAR]] = Field(
        default=None,
        title="VAR",
        description="Optional, repeating",
    )

    ROLE_PATHWAY: Optional[List[_CQU_I19_ROLE_PATHWAY]] = Field(
        default=None,
        title="ROLE_PATHWAY",
        description="Optional, repeating",
    )

    PATHWAY_OBSERVATION: Optional[List[_CQU_I19_PATHWAY_OBSERVATION]] = Field(
        default=None,
        title="PATHWAY_OBSERVATION",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}

"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.1
Class: CCI_I22.PATHWAY
Type: Group
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..segments.PTH import PTH
from ..segments.VAR import VAR
from .CCI_I22_PATHWAY_OBSERVATION import CCI_I22_PATHWAY_OBSERVATION
from .CCI_I22_ROLE_PATHWAY import CCI_I22_ROLE_PATHWAY

_CCI_I22_PATHWAY_OBSERVATION = CCI_I22_PATHWAY_OBSERVATION
_CCI_I22_ROLE_PATHWAY = CCI_I22_ROLE_PATHWAY
_PTH = PTH
_VAR = VAR


class CCI_I22_PATHWAY(BaseModel):
    """HL7 v2 CCI_I22.PATHWAY group.

    Attributes:
        PTH (PTH): required
        VAR (Optional[List[VAR]]): optional
        ROLE_PATHWAY (Optional[List[CCI_I22_ROLE_PATHWAY]]): optional
        PATHWAY_OBSERVATION (Optional[List[CCI_I22_PATHWAY_OBSERVATION]]): optional
    """

    PTH: _PTH = Field(
        default=...,
        title="PTH",
        description="Required",
    )

    VAR: list[_VAR] | None = Field(
        default=None,
        title="VAR",
        description="Optional, repeating",
    )

    ROLE_PATHWAY: list[_CCI_I22_ROLE_PATHWAY] | None = Field(
        default=None,
        title="ROLE_PATHWAY",
        description="Optional, repeating",
    )

    PATHWAY_OBSERVATION: list[_CCI_I22_PATHWAY_OBSERVATION] | None = Field(
        default=None,
        title="PATHWAY_OBSERVATION",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}

"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.1
Class: CCU_I20.PATHWAY
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.PTH import PTH
from ..segments.VAR import VAR

from .CCU_I20_PATHWAY_OBSERVATION import CCU_I20_PATHWAY_OBSERVATION
from .CCU_I20_ROLE_PATHWAY import CCU_I20_ROLE_PATHWAY

_CCU_I20_PATHWAY_OBSERVATION = CCU_I20_PATHWAY_OBSERVATION
_CCU_I20_ROLE_PATHWAY = CCU_I20_ROLE_PATHWAY
_PTH = PTH
_VAR = VAR


class CCU_I20_PATHWAY(HL7Model):
    """HL7 v2 CCU_I20.PATHWAY group.

    Attributes:
        PTH (PTH): required
        VAR (Optional[List[VAR]]): optional
        ROLE_PATHWAY (Optional[List[CCU_I20_ROLE_PATHWAY]]): optional
        PATHWAY_OBSERVATION (Optional[List[CCU_I20_PATHWAY_OBSERVATION]]): optional
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

    ROLE_PATHWAY: Optional[List[_CCU_I20_ROLE_PATHWAY]] = Field(
        default=None,
        title="ROLE_PATHWAY",
        description="Optional, repeating",
    )

    PATHWAY_OBSERVATION: Optional[List[_CCU_I20_PATHWAY_OBSERVATION]] = Field(
        default=None,
        title="PATHWAY_OBSERVATION",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}

"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8
Class: CCR_I16.PATHWAY
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.PTH import PTH
from ..segments.VAR import VAR

from .CCR_I16_PATHWAY_OBSERVATION import CCR_I16_PATHWAY_OBSERVATION
from .CCR_I16_ROLE_PATHWAY import CCR_I16_ROLE_PATHWAY

_CCR_I16_PATHWAY_OBSERVATION = CCR_I16_PATHWAY_OBSERVATION
_CCR_I16_ROLE_PATHWAY = CCR_I16_ROLE_PATHWAY
_PTH = PTH
_VAR = VAR


class CCR_I16_PATHWAY(HL7Model):
    """HL7 v2 CCR_I16.PATHWAY group.

    Attributes:
        PTH (PTH): Pathway, required
        VAR (Optional[List[VAR]]): Variance, optional
        ROLE_PATHWAY (Optional[List[CCR_I16_ROLE_PATHWAY]]): optional
        PATHWAY_OBSERVATION (Optional[List[CCR_I16_PATHWAY_OBSERVATION]]): optional
    """

    PTH: _PTH = Field(
        title="PTH",
        description="Pathway",
    )

    VAR: Optional[List[_VAR]] = Field(
        default=None,
        title="VAR",
        description="Variance",
    )

    ROLE_PATHWAY: Optional[List[_CCR_I16_ROLE_PATHWAY]] = Field(
        default=None,
        title="ROLE_PATHWAY",
    )

    PATHWAY_OBSERVATION: Optional[List[_CCR_I16_PATHWAY_OBSERVATION]] = Field(
        default=None,
        title="PATHWAY_OBSERVATION",
    )

    model_config = {"populate_by_name": True}

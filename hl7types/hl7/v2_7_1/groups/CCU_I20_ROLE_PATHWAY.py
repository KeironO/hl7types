"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7.1
Class: CCU_I20.ROLE_PATHWAY
Type: Group
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..segments.VAR import VAR
from .CCU_I20_ROLE_PATHWAY_OBJECT import CCU_I20_ROLE_PATHWAY_OBJECT

_CCU_I20_ROLE_PATHWAY_OBJECT = CCU_I20_ROLE_PATHWAY_OBJECT
_VAR = VAR


class CCU_I20_ROLE_PATHWAY(BaseModel):
    """HL7 v2 CCU_I20.ROLE_PATHWAY group.

    Attributes:
        ROLE_PATHWAY_OBJECT (CCU_I20_ROLE_PATHWAY_OBJECT): required
        VAR (Optional[List[VAR]]): optional
    """

    ROLE_PATHWAY_OBJECT: _CCU_I20_ROLE_PATHWAY_OBJECT = Field(
        default=...,
        title="ROLE_PATHWAY_OBJECT",
        description="Required",
    )

    VAR: list[_VAR] | None = Field(
        default=None,
        title="VAR",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}

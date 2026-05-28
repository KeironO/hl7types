"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7
Class: CCM_I21.ROLE_PATHWAY
Type: Group
"""
from _future__ import annotations

from typing import Optional, List
from pydantic import BaseModel, Field

from ..segments.VAR import VAR

from .CCM_I21_ROLE_PATHWAY_OBJECT import CCM_I21_ROLE_PATHWAY_OBJECT

_CCM_I21_ROLE_PATHWAY_OBJECT = CCM_I21_ROLE_PATHWAY_OBJECT
_VAR = VAR


class CCM_I21_ROLE_PATHWAY(BaseModel):
    """HL7 v2 CCM_I21.ROLE_PATHWAY group.

    Attributes:
        ROLE_PATHWAY_OBJECT (CCM_I21_ROLE_PATHWAY_OBJECT): required
        VAR (Optional[List[VAR]]): optional
    """

    ROLE_PATHWAY_OBJECT: _CCM_I21_ROLE_PATHWAY_OBJECT = Field(
        default=...,
        title="ROLE_PATHWAY_OBJECT",
        description="Required",
    )

    VAR: Optional[List[_VAR]] = Field(
        default=None,
        title="VAR",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}

"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7.1
Class: CCM_I21.PATHWAY
Type: Group
"""
from _future__ import annotations

from typing import Optional, List
from pydantic import BaseModel, Field

from ..segments.OBX import OBX
from ..segments.PTH import PTH
from ..segments.VAR import VAR

from .CCM_I21_ROLE_PATHWAY import CCM_I21_ROLE_PATHWAY

_CCM_I21_ROLE_PATHWAY = CCM_I21_ROLE_PATHWAY
_OBX = OBX
_PTH = PTH
_VAR = VAR


class CCM_I21_PATHWAY(BaseModel):
    """HL7 v2 CCM_I21.PATHWAY group.

    Attributes:
        PTH (PTH): required
        VAR (Optional[List[VAR]]): optional
        ROLE_PATHWAY (Optional[List[CCM_I21_ROLE_PATHWAY]]): optional
        OBX (Optional[List[OBX]]): optional
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

    ROLE_PATHWAY: Optional[List[_CCM_I21_ROLE_PATHWAY]] = Field(
        default=None,
        title="ROLE_PATHWAY",
        description="Optional, repeating",
    )

    OBX: Optional[List[_OBX]] = Field(
        default=None,
        title="OBX",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}

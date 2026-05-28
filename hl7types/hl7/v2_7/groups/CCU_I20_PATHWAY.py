"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7
Class: CCU_I20.PATHWAY
Type: Group
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..segments.OBX import OBX
from ..segments.PTH import PTH
from ..segments.VAR import VAR
from .CCU_I20_ROLE_PATHWAY import CCU_I20_ROLE_PATHWAY

_CCU_I20_ROLE_PATHWAY = CCU_I20_ROLE_PATHWAY
_OBX = OBX
_PTH = PTH
_VAR = VAR


class CCU_I20_PATHWAY(BaseModel):
    """HL7 v2 CCU_I20.PATHWAY group.

    Attributes:
        PTH (PTH): required
        VAR (Optional[List[VAR]]): optional
        ROLE_PATHWAY (Optional[List[CCU_I20_ROLE_PATHWAY]]): optional
        OBX (Optional[List[OBX]]): optional
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

    ROLE_PATHWAY: list[_CCU_I20_ROLE_PATHWAY] | None = Field(
        default=None,
        title="ROLE_PATHWAY",
        description="Optional, repeating",
    )

    OBX: list[_OBX] | None = Field(
        default=None,
        title="OBX",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}

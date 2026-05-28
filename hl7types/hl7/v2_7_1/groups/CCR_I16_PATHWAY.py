"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7.1
Class: CCR_I16.PATHWAY
Type: Group
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..segments.OBX import OBX
from ..segments.PTH import PTH
from ..segments.VAR import VAR
from .CCR_I16_ROLE_PATHWAY import CCR_I16_ROLE_PATHWAY

_CCR_I16_ROLE_PATHWAY = CCR_I16_ROLE_PATHWAY
_OBX = OBX
_PTH = PTH
_VAR = VAR


class CCR_I16_PATHWAY(BaseModel):
    """HL7 v2 CCR_I16.PATHWAY group.

    Attributes:
        PTH (PTH): required
        VAR (Optional[List[VAR]]): optional
        ROLE_PATHWAY (Optional[List[CCR_I16_ROLE_PATHWAY]]): optional
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

    ROLE_PATHWAY: list[_CCR_I16_ROLE_PATHWAY] | None = Field(
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

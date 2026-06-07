"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7
Class: CCR_I16.GOAL
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.GOL import GOL
from ..segments.OBX import OBX
from ..segments.VAR import VAR

from .CCR_I16_ROLE_GOAL import CCR_I16_ROLE_GOAL

_CCR_I16_ROLE_GOAL = CCR_I16_ROLE_GOAL
_GOL = GOL
_OBX = OBX
_VAR = VAR


class CCR_I16_GOAL(HL7Model):
    """HL7 v2 CCR_I16.GOAL group.

    Attributes:
        GOL (GOL): required
        VAR (Optional[List[VAR]]): optional
        ROLE_GOAL (Optional[List[CCR_I16_ROLE_GOAL]]): optional
        OBX (Optional[List[OBX]]): optional
    """

    GOL: _GOL = Field(
        title="GOL",
        description="Required",
    )

    VAR: Optional[List[_VAR]] = Field(
        default=None,
        title="VAR",
        description="Optional, repeating",
    )

    ROLE_GOAL: Optional[List[_CCR_I16_ROLE_GOAL]] = Field(
        default=None,
        title="ROLE_GOAL",
        description="Optional, repeating",
    )

    OBX: Optional[List[_OBX]] = Field(
        default=None,
        title="OBX",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}

"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7.1
Class: CCM_I21.GOAL
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.GOL import GOL
from ..segments.OBX import OBX
from ..segments.VAR import VAR

from .CCM_I21_ROLE_GOAL import CCM_I21_ROLE_GOAL

_CCM_I21_ROLE_GOAL = CCM_I21_ROLE_GOAL
_GOL = GOL
_OBX = OBX
_VAR = VAR


class CCM_I21_GOAL(HL7Model):
    """HL7 v2 CCM_I21.GOAL group.

    Attributes:
        GOL (GOL): required
        VAR (Optional[List[VAR]]): optional
        ROLE_GOAL (Optional[List[CCM_I21_ROLE_GOAL]]): optional
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

    ROLE_GOAL: Optional[List[_CCM_I21_ROLE_GOAL]] = Field(
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

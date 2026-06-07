"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.1
Class: CCM_I21.ROLE_PROBLEM
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.VAR import VAR

from .CCM_I21_ROLE_PROBLEM_OBJECT import CCM_I21_ROLE_PROBLEM_OBJECT

_CCM_I21_ROLE_PROBLEM_OBJECT = CCM_I21_ROLE_PROBLEM_OBJECT
_VAR = VAR


class CCM_I21_ROLE_PROBLEM(HL7Model):
    """HL7 v2 CCM_I21.ROLE_PROBLEM group.

    Attributes:
        ROLE_PROBLEM_OBJECT (CCM_I21_ROLE_PROBLEM_OBJECT): required
        VAR (Optional[List[VAR]]): optional
    """

    ROLE_PROBLEM_OBJECT: _CCM_I21_ROLE_PROBLEM_OBJECT = Field(
        title="ROLE_PROBLEM_OBJECT",
        description="Required",
    )

    VAR: Optional[List[_VAR]] = Field(
        default=None,
        title="VAR",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}

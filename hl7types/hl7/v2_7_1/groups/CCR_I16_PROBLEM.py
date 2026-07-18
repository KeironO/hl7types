"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7.1
Class: CCR_I16.PROBLEM
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import ConfigDict, Field
from hl7types.hl7 import HL7Model

from ..segments.OBX import OBX
from ..segments.PRB import PRB
from ..segments.VAR import VAR

from .CCR_I16_ROLE_PROBLEM import CCR_I16_ROLE_PROBLEM

_CCR_I16_ROLE_PROBLEM = CCR_I16_ROLE_PROBLEM
_OBX = OBX
_PRB = PRB
_VAR = VAR


class CCR_I16_PROBLEM(HL7Model):
    """HL7 v2 CCR_I16.PROBLEM group.

    Attributes:
        PRB (PRB): Problem Details, required
        VAR (Optional[List[VAR]]): Variance, optional
        ROLE_PROBLEM (Optional[List[CCR_I16_ROLE_PROBLEM]]): optional
        OBX (Optional[List[OBX]]): Observation/Result, optional
    """

    PRB: _PRB = Field(
        title="PRB",
        description="Problem Details",
    )

    VAR: Optional[List[_VAR]] = Field(
        default=None,
        title="VAR",
        description="Variance",
    )

    ROLE_PROBLEM: Optional[List[_CCR_I16_ROLE_PROBLEM]] = Field(
        default=None,
        title="ROLE_PROBLEM",
    )

    OBX: Optional[List[_OBX]] = Field(
        default=None,
        title="OBX",
        description="Observation/Result",
    )

    model_config = ConfigDict(populate_by_name=True)

"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.2
Class: CCI_I22.PROBLEM
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.PRB import PRB
from ..segments.VAR import VAR

from .CCI_I22_PROBLEM_OBSERVATION import CCI_I22_PROBLEM_OBSERVATION
from .CCI_I22_ROLE_PROBLEM import CCI_I22_ROLE_PROBLEM

_CCI_I22_PROBLEM_OBSERVATION = CCI_I22_PROBLEM_OBSERVATION
_CCI_I22_ROLE_PROBLEM = CCI_I22_ROLE_PROBLEM
_PRB = PRB
_VAR = VAR


class CCI_I22_PROBLEM(HL7Model):
    """HL7 v2 CCI_I22.PROBLEM group.

    Attributes:
        PRB (PRB): required
        VAR (Optional[List[VAR]]): optional
        ROLE_PROBLEM (Optional[List[CCI_I22_ROLE_PROBLEM]]): optional
        PROBLEM_OBSERVATION (Optional[List[CCI_I22_PROBLEM_OBSERVATION]]): optional
    """

    PRB: _PRB = Field(
        default=...,
        title="PRB",
        description="Required",
    )

    VAR: Optional[List[_VAR]] = Field(
        default=None,
        title="VAR",
        description="Optional, repeating",
    )

    ROLE_PROBLEM: Optional[List[_CCI_I22_ROLE_PROBLEM]] = Field(
        default=None,
        title="ROLE_PROBLEM",
        description="Optional, repeating",
    )

    PROBLEM_OBSERVATION: Optional[List[_CCI_I22_PROBLEM_OBSERVATION]] = Field(
        default=None,
        title="PROBLEM_OBSERVATION",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}

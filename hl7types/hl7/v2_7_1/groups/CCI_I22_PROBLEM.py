"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7.1
Class: CCI_I22.PROBLEM
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.OBX import OBX
from ..segments.PRB import PRB
from ..segments.VAR import VAR

from .CCI_I22_ROLE_PROBLEM import CCI_I22_ROLE_PROBLEM

_CCI_I22_ROLE_PROBLEM = CCI_I22_ROLE_PROBLEM
_OBX = OBX
_PRB = PRB
_VAR = VAR


class CCI_I22_PROBLEM(HL7Model):
    """HL7 v2 CCI_I22.PROBLEM group.

    Attributes:
        PRB (PRB): required
        VAR (Optional[List[VAR]]): optional
        ROLE_PROBLEM (Optional[List[CCI_I22_ROLE_PROBLEM]]): optional
        OBX (Optional[List[OBX]]): optional
    """

    PRB: _PRB = Field(
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

    OBX: Optional[List[_OBX]] = Field(
        default=None,
        title="OBX",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}

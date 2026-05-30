"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5
Class: PRR_PC5.PROBLEM_PATHWAY
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.PTH import PTH
from ..segments.VAR import VAR

_PTH = PTH
_VAR = VAR


class PRR_PC5_PROBLEM_PATHWAY(HL7Model):
    """HL7 v2 PRR_PC5.PROBLEM_PATHWAY group.

    Attributes:
        PTH (PTH): required
        VAR (Optional[List[VAR]]): optional
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

    model_config = {"populate_by_name": True}

"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7
Class: PRR_PC5.PROBLEM_PATHWAY
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import ConfigDict, Field
from hl7types.hl7 import HL7Model

from ..segments.PTH import PTH
from ..segments.VAR import VAR

_PTH = PTH
_VAR = VAR


class PRR_PC5_PROBLEM_PATHWAY(HL7Model):
    """HL7 v2 PRR_PC5.PROBLEM_PATHWAY group.

    Attributes:
        PTH (PTH): Pathway, required
        VAR (Optional[List[VAR]]): Variance, optional
    """

    PTH: _PTH = Field(
        title="PTH",
        description="Pathway",
    )

    VAR: Optional[List[_VAR]] = Field(
        default=None,
        title="VAR",
        description="Variance",
    )

    model_config = ConfigDict(populate_by_name=True)

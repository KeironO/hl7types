"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3.1
Class: PGL_PC6.PATHWAY
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


class PGL_PC6_PATHWAY(HL7Model):
    """HL7 v2 PGL_PC6.PATHWAY group.

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

    model_config = {"populate_by_name": True}

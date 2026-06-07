"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.2
Class: PPR_PC1.PATHWAY
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


class PPR_PC1_PATHWAY(HL7Model):
    """HL7 v2 PPR_PC1.PATHWAY group.

    Attributes:
        PTH (PTH): required
        VAR (Optional[List[VAR]]): optional
    """

    PTH: _PTH = Field(
        title="PTH",
        description="Required",
    )

    VAR: Optional[List[_VAR]] = Field(
        default=None,
        title="VAR",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}

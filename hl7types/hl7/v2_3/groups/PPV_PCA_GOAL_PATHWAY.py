"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3
Class: PPV_PCA.GOAL_PATHWAY
Type: Group
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..segments.PTH import PTH
from ..segments.VAR import VAR

_PTH = PTH
_VAR = VAR


class PPV_PCA_GOAL_PATHWAY(BaseModel):
    """HL7 v2 PPV_PCA.GOAL_PATHWAY group.

    Attributes:
        PTH (PTH): required
        VAR (Optional[List[VAR]]): optional
    """

    PTH: _PTH = Field(
        default=...,
        title="PTH",
        description="Required",
    )

    VAR: list[_VAR] | None = Field(
        default=None,
        title="VAR",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}

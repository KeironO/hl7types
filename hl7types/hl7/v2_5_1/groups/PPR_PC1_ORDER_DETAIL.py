"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5.1
Class: PPR_PC1.ORDER_DETAIL
Type: Group
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..segments.NTE import NTE
from ..segments.VAR import VAR
from .PPR_PC1_OBR_SUPPGRP import PPR_PC1_OBR_SUPPGRP
from .PPR_PC1_ORDER_OBSERVATION import PPR_PC1_ORDER_OBSERVATION

_NTE = NTE
_PPR_PC1_OBR_SUPPGRP = PPR_PC1_OBR_SUPPGRP
_PPR_PC1_ORDER_OBSERVATION = PPR_PC1_ORDER_OBSERVATION
_VAR = VAR


class PPR_PC1_ORDER_DETAIL(BaseModel):
    """HL7 v2 PPR_PC1.ORDER_DETAIL group.

    Attributes:
        OBR_SUPPGRP (PPR_PC1_OBR_SUPPGRP): required
        NTE (Optional[List[NTE]]): optional
        VAR (Optional[List[VAR]]): optional
        ORDER_OBSERVATION (Optional[List[PPR_PC1_ORDER_OBSERVATION]]): optional
    """

    OBR_SUPPGRP: _PPR_PC1_OBR_SUPPGRP = Field(
        default=...,
        title="OBR_SUPPGRP",
        description="Required",
    )

    NTE: list[_NTE] | None = Field(
        default=None,
        title="NTE",
        description="Optional, repeating",
    )

    VAR: list[_VAR] | None = Field(
        default=None,
        title="VAR",
        description="Optional, repeating",
    )

    ORDER_OBSERVATION: list[_PPR_PC1_ORDER_OBSERVATION] | None = Field(
        default=None,
        title="ORDER_OBSERVATION",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}

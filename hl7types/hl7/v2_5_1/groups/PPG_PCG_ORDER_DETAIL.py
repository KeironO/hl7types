"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5.1
Class: PPG_PCG.ORDER_DETAIL
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import BaseModel, Field

from ..segments.NTE import NTE
from ..segments.VAR import VAR

from .PPG_PCG_OBR_SUPPGRP import PPG_PCG_OBR_SUPPGRP
from .PPG_PCG_ORDER_OBSERVATION import PPG_PCG_ORDER_OBSERVATION

_NTE = NTE
_PPG_PCG_OBR_SUPPGRP = PPG_PCG_OBR_SUPPGRP
_PPG_PCG_ORDER_OBSERVATION = PPG_PCG_ORDER_OBSERVATION
_VAR = VAR


class PPG_PCG_ORDER_DETAIL(BaseModel):
    """HL7 v2 PPG_PCG.ORDER_DETAIL group.

    Attributes:
        OBR_SUPPGRP (PPG_PCG_OBR_SUPPGRP): required
        NTE (Optional[List[NTE]]): optional
        VAR (Optional[List[VAR]]): optional
        ORDER_OBSERVATION (Optional[List[PPG_PCG_ORDER_OBSERVATION]]): optional
    """

    OBR_SUPPGRP: _PPG_PCG_OBR_SUPPGRP = Field(
        default=...,
        title="OBR_SUPPGRP",
        description="Required",
    )

    NTE: Optional[List[_NTE]] = Field(
        default=None,
        title="NTE",
        description="Optional, repeating",
    )

    VAR: Optional[List[_VAR]] = Field(
        default=None,
        title="VAR",
        description="Optional, repeating",
    )

    ORDER_OBSERVATION: Optional[List[_PPG_PCG_ORDER_OBSERVATION]] = Field(
        default=None,
        title="ORDER_OBSERVATION",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}

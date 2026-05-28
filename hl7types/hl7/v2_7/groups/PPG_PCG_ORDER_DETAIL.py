"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7
Class: PPG_PCG.ORDER_DETAIL
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import BaseModel, Field

from ..segments.NTE import NTE
from ..segments.VAR import VAR

from .PPG_PCG_CHOICE import PPG_PCG_CHOICE
from .PPG_PCG_ORDER_OBSERVATION import PPG_PCG_ORDER_OBSERVATION

_NTE = NTE
_PPG_PCG_CHOICE = PPG_PCG_CHOICE
_PPG_PCG_ORDER_OBSERVATION = PPG_PCG_ORDER_OBSERVATION
_VAR = VAR


class PPG_PCG_ORDER_DETAIL(BaseModel):
    """HL7 v2 PPG_PCG.ORDER_DETAIL group.

    Attributes:
        CHOICE (PPG_PCG_CHOICE): required
        NTE (Optional[List[NTE]]): optional
        VAR (Optional[List[VAR]]): optional
        ORDER_OBSERVATION (Optional[List[PPG_PCG_ORDER_OBSERVATION]]): optional
    """

    CHOICE: _PPG_PCG_CHOICE = Field(
        default=...,
        title="CHOICE",
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

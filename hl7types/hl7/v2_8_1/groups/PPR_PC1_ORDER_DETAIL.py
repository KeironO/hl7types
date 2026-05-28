"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.1
Class: PPR_PC1.ORDER_DETAIL
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import BaseModel, Field

from ..segments.NTE import NTE
from ..segments.VAR import VAR

from .PPR_PC1_CHOICE import PPR_PC1_CHOICE
from .PPR_PC1_ORDER_OBSERVATION import PPR_PC1_ORDER_OBSERVATION

_NTE = NTE
_PPR_PC1_CHOICE = PPR_PC1_CHOICE
_PPR_PC1_ORDER_OBSERVATION = PPR_PC1_ORDER_OBSERVATION
_VAR = VAR


class PPR_PC1_ORDER_DETAIL(BaseModel):
    """HL7 v2 PPR_PC1.ORDER_DETAIL group.

    Attributes:
        CHOICE (PPR_PC1_CHOICE): required
        NTE (Optional[List[NTE]]): optional
        VAR (Optional[List[VAR]]): optional
        ORDER_OBSERVATION (Optional[List[PPR_PC1_ORDER_OBSERVATION]]): optional
    """

    CHOICE: _PPR_PC1_CHOICE = Field(
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

    ORDER_OBSERVATION: Optional[List[_PPR_PC1_ORDER_OBSERVATION]] = Field(
        default=None,
        title="ORDER_OBSERVATION",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}

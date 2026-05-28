"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7
Class: PTR_PCF.ORDER_DETAIL
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import BaseModel, Field

from ..segments.NTE import NTE
from ..segments.VAR import VAR

from .PTR_PCF_CHOICE import PTR_PCF_CHOICE
from .PTR_PCF_ORDER_OBSERVATION import PTR_PCF_ORDER_OBSERVATION

_NTE = NTE
_PTR_PCF_CHOICE = PTR_PCF_CHOICE
_PTR_PCF_ORDER_OBSERVATION = PTR_PCF_ORDER_OBSERVATION
_VAR = VAR


class PTR_PCF_ORDER_DETAIL(BaseModel):
    """HL7 v2 PTR_PCF.ORDER_DETAIL group.

    Attributes:
        CHOICE (PTR_PCF_CHOICE): required
        NTE (Optional[List[NTE]]): optional
        VAR (Optional[List[VAR]]): optional
        ORDER_OBSERVATION (Optional[List[PTR_PCF_ORDER_OBSERVATION]]): optional
    """

    CHOICE: _PTR_PCF_CHOICE = Field(
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

    ORDER_OBSERVATION: Optional[List[_PTR_PCF_ORDER_OBSERVATION]] = Field(
        default=None,
        title="ORDER_OBSERVATION",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}

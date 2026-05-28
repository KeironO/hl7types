"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7.1
Class: PPT_PCL.ORDER_DETAIL
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import BaseModel, Field

from ..segments.NTE import NTE
from ..segments.VAR import VAR

from .PPT_PCL_CHOICE import PPT_PCL_CHOICE
from .PPT_PCL_ORDER_OBSERVATION import PPT_PCL_ORDER_OBSERVATION

_NTE = NTE
_PPT_PCL_CHOICE = PPT_PCL_CHOICE
_PPT_PCL_ORDER_OBSERVATION = PPT_PCL_ORDER_OBSERVATION
_VAR = VAR


class PPT_PCL_ORDER_DETAIL(BaseModel):
    """HL7 v2 PPT_PCL.ORDER_DETAIL group.

    Attributes:
        CHOICE (PPT_PCL_CHOICE): required
        NTE (Optional[List[NTE]]): optional
        VAR (Optional[List[VAR]]): optional
        ORDER_OBSERVATION (Optional[List[PPT_PCL_ORDER_OBSERVATION]]): optional
    """

    CHOICE: _PPT_PCL_CHOICE = Field(
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

    ORDER_OBSERVATION: Optional[List[_PPT_PCL_ORDER_OBSERVATION]] = Field(
        default=None,
        title="ORDER_OBSERVATION",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}

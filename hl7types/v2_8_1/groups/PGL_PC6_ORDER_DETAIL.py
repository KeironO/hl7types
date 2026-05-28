"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.1
Class: PGL_PC6.ORDER_DETAIL
Type: Group
"""
from _future__ import annotations

from typing import Optional, List
from pydantic import BaseModel, Field

from ..segments.NTE import NTE
from ..segments.VAR import VAR

from .PGL_PC6_CHOICE import PGL_PC6_CHOICE
from .PGL_PC6_ORDER_OBSERVATION import PGL_PC6_ORDER_OBSERVATION

_NTE = NTE
_PGL_PC6_CHOICE = PGL_PC6_CHOICE
_PGL_PC6_ORDER_OBSERVATION = PGL_PC6_ORDER_OBSERVATION
_VAR = VAR


class PGL_PC6_ORDER_DETAIL(BaseModel):
    """HL7 v2 PGL_PC6.ORDER_DETAIL group.

    Attributes:
        CHOICE (PGL_PC6_CHOICE): required
        NTE (Optional[List[NTE]]): optional
        VAR (Optional[List[VAR]]): optional
        ORDER_OBSERVATION (Optional[List[PGL_PC6_ORDER_OBSERVATION]]): optional
    """

    CHOICE: _PGL_PC6_CHOICE = Field(
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

    ORDER_OBSERVATION: Optional[List[_PGL_PC6_ORDER_OBSERVATION]] = Field(
        default=None,
        title="ORDER_OBSERVATION",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}

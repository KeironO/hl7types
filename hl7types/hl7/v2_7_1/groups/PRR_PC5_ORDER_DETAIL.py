"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7.1
Class: PRR_PC5.ORDER_DETAIL
Type: Group
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..segments.NTE import NTE
from ..segments.VAR import VAR
from .PRR_PC5_CHOICE import PRR_PC5_CHOICE
from .PRR_PC5_ORDER_OBSERVATION import PRR_PC5_ORDER_OBSERVATION

_NTE = NTE
_PRR_PC5_CHOICE = PRR_PC5_CHOICE
_PRR_PC5_ORDER_OBSERVATION = PRR_PC5_ORDER_OBSERVATION
_VAR = VAR


class PRR_PC5_ORDER_DETAIL(BaseModel):
    """HL7 v2 PRR_PC5.ORDER_DETAIL group.

    Attributes:
        CHOICE (PRR_PC5_CHOICE): required
        NTE (Optional[List[NTE]]): optional
        VAR (Optional[List[VAR]]): optional
        ORDER_OBSERVATION (Optional[List[PRR_PC5_ORDER_OBSERVATION]]): optional
    """

    CHOICE: _PRR_PC5_CHOICE = Field(
        default=...,
        title="CHOICE",
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

    ORDER_OBSERVATION: list[_PRR_PC5_ORDER_OBSERVATION] | None = Field(
        default=None,
        title="ORDER_OBSERVATION",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}

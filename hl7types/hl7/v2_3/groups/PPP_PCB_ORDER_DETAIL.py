"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3
Class: PPP_PCB.ORDER_DETAIL
Type: Group
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..segments.NTE import NTE
from ..segments.OBR import OBR
from ..segments.VAR import VAR
from .PPP_PCB_ORDER_OBSERVATION import PPP_PCB_ORDER_OBSERVATION

_NTE = NTE
_OBR = OBR
_PPP_PCB_ORDER_OBSERVATION = PPP_PCB_ORDER_OBSERVATION
_VAR = VAR


class PPP_PCB_ORDER_DETAIL(BaseModel):
    """HL7 v2 PPP_PCB.ORDER_DETAIL group.

    Attributes:
        OBR (OBR): required
        NTE (Optional[List[NTE]]): optional
        VAR (Optional[List[VAR]]): optional
        ORDER_OBSERVATION (Optional[List[PPP_PCB_ORDER_OBSERVATION]]): optional
    """

    OBR: _OBR = Field(
        default=...,
        title="OBR",
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

    ORDER_OBSERVATION: list[_PPP_PCB_ORDER_OBSERVATION] | None = Field(
        default=None,
        title="ORDER_OBSERVATION",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}

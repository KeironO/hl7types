"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.6
Class: PPP_PCB.ORDER_DETAIL
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.NTE import NTE
from ..segments.VAR import VAR

from .PPP_PCB_CHOICE import PPP_PCB_CHOICE
from .PPP_PCB_ORDER_OBSERVATION import PPP_PCB_ORDER_OBSERVATION

_NTE = NTE
_PPP_PCB_CHOICE = PPP_PCB_CHOICE
_PPP_PCB_ORDER_OBSERVATION = PPP_PCB_ORDER_OBSERVATION
_VAR = VAR


class PPP_PCB_ORDER_DETAIL(HL7Model):
    """HL7 v2 PPP_PCB.ORDER_DETAIL group.

    Attributes:
        CHOICE (PPP_PCB_CHOICE): required
        NTE (Optional[List[NTE]]): optional
        VAR (Optional[List[VAR]]): optional
        ORDER_OBSERVATION (Optional[List[PPP_PCB_ORDER_OBSERVATION]]): optional
    """

    CHOICE: _PPP_PCB_CHOICE = Field(
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

    ORDER_OBSERVATION: Optional[List[_PPP_PCB_ORDER_OBSERVATION]] = Field(
        default=None,
        title="ORDER_OBSERVATION",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}

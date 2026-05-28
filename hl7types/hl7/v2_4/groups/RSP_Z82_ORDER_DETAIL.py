"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.4
Class: RSP_Z82.ORDER_DETAIL
Type: Group
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..segments.NTE import NTE
from ..segments.RXO import RXO
from ..segments.RXR import RXR
from .RSP_Z82_TREATMENT import RSP_Z82_TREATMENT

_NTE = NTE
_RSP_Z82_TREATMENT = RSP_Z82_TREATMENT
_RXO = RXO
_RXR = RXR


class RSP_Z82_ORDER_DETAIL(BaseModel):
    """HL7 v2 RSP_Z82.ORDER_DETAIL group.

    Attributes:
        RXO (RXO): required
        NTE (Optional[List[NTE]]): optional
        RXR (List[RXR]): required
        TREATMENT (Optional[RSP_Z82_TREATMENT]): optional
    """

    RXO: _RXO = Field(
        default=...,
        title="RXO",
        description="Required",
    )

    NTE: list[_NTE] | None = Field(
        default=None,
        title="NTE",
        description="Optional, repeating",
    )

    RXR: list[_RXR] = Field(
        default=...,
        title="RXR",
        description="Required, repeating",
    )

    TREATMENT: _RSP_Z82_TREATMENT | None = Field(
        default=None,
        title="TREATMENT",
        description="Optional",
    )

    model_config = {"populate_by_name": True}

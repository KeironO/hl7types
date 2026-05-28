"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3
Class: OMN_O01.ORDER_DETAIL
Type: Group
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..segments.NTE import NTE
from ..segments.RQ1 import RQ1
from ..segments.RQD import RQD
from .OMN_O01_OBSERVATION import OMN_O01_OBSERVATION

_NTE = NTE
_OMN_O01_OBSERVATION = OMN_O01_OBSERVATION
_RQ1 = RQ1
_RQD = RQD


class OMN_O01_ORDER_DETAIL(BaseModel):
    """HL7 v2 OMN_O01.ORDER_DETAIL group.

    Attributes:
        RQD (RQD): required
        RQ1 (Optional[RQ1]): optional
        NTE (Optional[List[NTE]]): optional
        OBSERVATION (Optional[List[OMN_O01_OBSERVATION]]): optional
    """

    RQD: _RQD = Field(
        default=...,
        title="RQD",
        description="Required",
    )

    RQ1: _RQ1 | None = Field(
        default=None,
        title="RQ1",
        description="Optional",
    )

    NTE: list[_NTE] | None = Field(
        default=None,
        title="NTE",
        description="Optional, repeating",
    )

    OBSERVATION: list[_OMN_O01_OBSERVATION] | None = Field(
        default=None,
        title="OBSERVATION",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}

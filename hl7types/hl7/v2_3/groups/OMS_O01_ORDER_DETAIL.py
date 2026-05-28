"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3
Class: OMS_O01.ORDER_DETAIL
Type: Group
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..segments.NTE import NTE
from ..segments.RQD import RQD
from .OMS_O01_OBSERVATION import OMS_O01_OBSERVATION

_NTE = NTE
_OMS_O01_OBSERVATION = OMS_O01_OBSERVATION
_RQD = RQD


class OMS_O01_ORDER_DETAIL(BaseModel):
    """HL7 v2 OMS_O01.ORDER_DETAIL group.

    Attributes:
        RQD (RQD): required
        NTE (Optional[List[NTE]]): optional
        OBSERVATION (Optional[List[OMS_O01_OBSERVATION]]): optional
    """

    RQD: _RQD = Field(
        default=...,
        title="RQD",
        description="Required",
    )

    NTE: list[_NTE] | None = Field(
        default=None,
        title="NTE",
        description="Optional, repeating",
    )

    OBSERVATION: list[_OMS_O01_OBSERVATION] | None = Field(
        default=None,
        title="OBSERVATION",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}

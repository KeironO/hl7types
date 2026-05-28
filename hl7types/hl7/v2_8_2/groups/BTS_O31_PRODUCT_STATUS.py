"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.2
Class: BTS_O31.PRODUCT_STATUS
Type: Group
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..segments.BTX import BTX
from ..segments.NTE import NTE

_BTX = BTX
_NTE = NTE


class BTS_O31_PRODUCT_STATUS(BaseModel):
    """HL7 v2 BTS_O31.PRODUCT_STATUS group.

    Attributes:
        BTX (BTX): required
        NTE (Optional[List[NTE]]): optional
    """

    BTX: _BTX = Field(
        default=...,
        title="BTX",
        description="Required",
    )

    NTE: list[_NTE] | None = Field(
        default=None,
        title="NTE",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}

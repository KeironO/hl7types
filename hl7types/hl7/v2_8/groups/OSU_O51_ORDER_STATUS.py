"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8
Class: OSU_O51.ORDER_STATUS
Type: Group
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..segments.ORC import ORC
from ..segments.PRT import PRT

_ORC = ORC
_PRT = PRT


class OSU_O51_ORDER_STATUS(BaseModel):
    """HL7 v2 OSU_O51.ORDER_STATUS group.

    Attributes:
        ORC (ORC): required
        PRT (Optional[List[PRT]]): optional
    """

    ORC: _ORC = Field(
        default=...,
        title="ORC",
        description="Required",
    )

    PRT: list[_PRT] | None = Field(
        default=None,
        title="PRT",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}

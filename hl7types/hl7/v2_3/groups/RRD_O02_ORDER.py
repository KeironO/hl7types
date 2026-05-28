"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3
Class: RRD_O02.ORDER
Type: Group
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..segments.ORC import ORC
from .RRD_O02_DISPENSE import RRD_O02_DISPENSE

_ORC = ORC
_RRD_O02_DISPENSE = RRD_O02_DISPENSE


class RRD_O02_ORDER(BaseModel):
    """HL7 v2 RRD_O02.ORDER group.

    Attributes:
        ORC (ORC): required
        DISPENSE (Optional[RRD_O02_DISPENSE]): optional
    """

    ORC: _ORC = Field(
        default=...,
        title="ORC",
        description="Required",
    )

    DISPENSE: _RRD_O02_DISPENSE | None = Field(
        default=None,
        title="DISPENSE",
        description="Optional",
    )

    model_config = {"populate_by_name": True}

"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.4
Class: RRD_O14.ORDER
Type: Group
"""
from _future__ import annotations

from typing import Optional
from pydantic import BaseModel, Field

from ..segments.ORC import ORC

from .RRD_O14_DISPENSE import RRD_O14_DISPENSE

_ORC = ORC
_RRD_O14_DISPENSE = RRD_O14_DISPENSE


class RRD_O14_ORDER(BaseModel):
    """HL7 v2 RRD_O14.ORDER group.

    Attributes:
        ORC (ORC): required
        DISPENSE (Optional[RRD_O14_DISPENSE]): optional
    """

    ORC: _ORC = Field(
        default=...,
        title="ORC",
        description="Required",
    )

    DISPENSE: Optional[_RRD_O14_DISPENSE] = Field(
        default=None,
        title="DISPENSE",
        description="Optional",
    )

    model_config = {"populate_by_name": True}

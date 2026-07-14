"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3.1
Class: RRO_O02.ORDER
Type: Group
"""
from __future__ import annotations

from typing import Optional
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.ORC import ORC

from .RRO_O02_ORDER_DETAIL import RRO_O02_ORDER_DETAIL

_ORC = ORC
_RRO_O02_ORDER_DETAIL = RRO_O02_ORDER_DETAIL


class RRO_O02_ORDER(HL7Model):
    """HL7 v2 RRO_O02.ORDER group.

    Attributes:
        ORC (ORC): ORC - common order segment, required
        ORDER_DETAIL (Optional[RRO_O02_ORDER_DETAIL]): optional
    """

    ORC: _ORC = Field(
        title="ORC",
        description="ORC - common order segment",
    )

    ORDER_DETAIL: Optional[_RRO_O02_ORDER_DETAIL] = Field(
        default=None,
        title="ORDER_DETAIL",
    )

    model_config = {"populate_by_name": True}

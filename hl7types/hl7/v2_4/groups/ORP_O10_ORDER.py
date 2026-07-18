"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.4
Class: ORP_O10.ORDER
Type: Group
"""
from __future__ import annotations

from typing import Optional
from pydantic import ConfigDict, Field
from hl7types.hl7 import HL7Model

from ..segments.ORC import ORC

from .ORP_O10_ORDER_DETAIL import ORP_O10_ORDER_DETAIL

_ORC = ORC
_ORP_O10_ORDER_DETAIL = ORP_O10_ORDER_DETAIL


class ORP_O10_ORDER(HL7Model):
    """HL7 v2 ORP_O10.ORDER group.

    Attributes:
        ORC (ORC): Common Order, required
        ORDER_DETAIL (Optional[ORP_O10_ORDER_DETAIL]): optional
    """

    ORC: _ORC = Field(
        title="ORC",
        description="Common Order",
    )

    ORDER_DETAIL: Optional[_ORP_O10_ORDER_DETAIL] = Field(
        default=None,
        title="ORDER_DETAIL",
    )

    model_config = ConfigDict(populate_by_name=True)

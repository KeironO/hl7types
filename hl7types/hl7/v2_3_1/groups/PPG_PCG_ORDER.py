"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3.1
Class: PPG_PCG.ORDER
Type: Group
"""
from __future__ import annotations

from typing import Optional
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.ORC import ORC

from .PPG_PCG_ORDER_DETAIL import PPG_PCG_ORDER_DETAIL

_ORC = ORC
_PPG_PCG_ORDER_DETAIL = PPG_PCG_ORDER_DETAIL


class PPG_PCG_ORDER(HL7Model):
    """HL7 v2 PPG_PCG.ORDER group.

    Attributes:
        ORC (ORC): required
        ORDER_DETAIL (Optional[PPG_PCG_ORDER_DETAIL]): optional
    """

    ORC: _ORC = Field(
        default=...,
        title="ORC",
        description="Required",
    )

    ORDER_DETAIL: Optional[_PPG_PCG_ORDER_DETAIL] = Field(
        default=None,
        title="ORDER_DETAIL",
        description="Optional",
    )

    model_config = {"populate_by_name": True}

"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3.1
Class: PTR_PCF.ORDER
Type: Group
"""
from __future__ import annotations

from typing import Optional
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.ORC import ORC

from .PTR_PCF_ORDER_DETAIL import PTR_PCF_ORDER_DETAIL

_ORC = ORC
_PTR_PCF_ORDER_DETAIL = PTR_PCF_ORDER_DETAIL


class PTR_PCF_ORDER(HL7Model):
    """HL7 v2 PTR_PCF.ORDER group.

    Attributes:
        ORC (ORC): required
        ORDER_DETAIL (Optional[PTR_PCF_ORDER_DETAIL]): optional
    """

    ORC: _ORC = Field(
        default=...,
        title="ORC",
        description="Required",
    )

    ORDER_DETAIL: Optional[_PTR_PCF_ORDER_DETAIL] = Field(
        default=None,
        title="ORDER_DETAIL",
        description="Optional",
    )

    model_config = {"populate_by_name": True}

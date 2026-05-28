"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.1
Class: ORR_O02.ORDER
Type: Group
"""
from _future__ import annotations

from typing import Optional, List
from pydantic import BaseModel, Field

from ..segments.NTE import NTE
from ..segments.ORC import ORC

from .ORR_O02_ORDER_DETAIL import ORR_O02_ORDER_DETAIL

_NTE = NTE
_ORC = ORC
_ORR_O02_ORDER_DETAIL = ORR_O02_ORDER_DETAIL


class ORR_O02_ORDER(BaseModel):
    """HL7 v2 ORR_O02.ORDER group.

    Attributes:
        ORC (ORC): required
        ORDER_DETAIL (Optional[ORR_O02_ORDER_DETAIL]): optional
        NTE (Optional[List[NTE]]): optional
    """

    ORC: _ORC = Field(
        default=...,
        title="ORC",
        description="Required",
    )

    ORDER_DETAIL: Optional[_ORR_O02_ORDER_DETAIL] = Field(
        default=None,
        title="ORDER_DETAIL",
        description="Optional",
    )

    NTE: Optional[List[_NTE]] = Field(
        default=None,
        title="NTE",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}

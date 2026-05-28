"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.4
Class: ORR_O02.ORDER
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import BaseModel, Field

from ..segments.CTI import CTI
from ..segments.NTE import NTE
from ..segments.ORC import ORC

from .ORR_O02_ORDER_DETAIL import ORR_O02_ORDER_DETAIL

_CTI = CTI
_NTE = NTE
_ORC = ORC
_ORR_O02_ORDER_DETAIL = ORR_O02_ORDER_DETAIL


class ORR_O02_ORDER(BaseModel):
    """HL7 v2 ORR_O02.ORDER group.

    Attributes:
        ORC (ORC): required
        ORDER_DETAIL (ORR_O02_ORDER_DETAIL): required
        NTE (Optional[List[NTE]]): optional
        CTI (Optional[List[CTI]]): optional
    """

    ORC: _ORC = Field(
        default=...,
        title="ORC",
        description="Required",
    )

    ORDER_DETAIL: _ORR_O02_ORDER_DETAIL = Field(
        default=...,
        title="ORDER_DETAIL",
        description="Required",
    )

    NTE: Optional[List[_NTE]] = Field(
        default=None,
        title="NTE",
        description="Optional, repeating",
    )

    CTI: Optional[List[_CTI]] = Field(
        default=None,
        title="CTI",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}

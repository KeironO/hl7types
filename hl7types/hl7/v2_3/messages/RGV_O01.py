"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3
Class: RGV_O01
Type: Message
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import BaseModel, Field

from ..segments.MSH import MSH
from ..segments.NTE import NTE

from ..groups.RGV_O01_ORDER import RGV_O01_ORDER
from ..groups.RGV_O01_PATIENT import RGV_O01_PATIENT

_MSH = MSH
_NTE = NTE
_RGV_O01_ORDER = RGV_O01_ORDER
_RGV_O01_PATIENT = RGV_O01_PATIENT


class RGV_O01(BaseModel):
    """HL7 v2 RGV_O01 message.

    Attributes:
        MSH (MSH): required
        NTE (Optional[List[NTE]]): optional
        PATIENT (Optional[RGV_O01_PATIENT]): optional
        ORDER (List[RGV_O01_ORDER]): required
    """

    MSH: _MSH = Field(
        default=...,
        title="MSH",
        description="Required",
    )

    NTE: Optional[List[_NTE]] = Field(
        default=None,
        title="NTE",
        description="Optional, repeating",
    )

    PATIENT: Optional[_RGV_O01_PATIENT] = Field(
        default=None,
        title="PATIENT",
        description="Optional",
    )

    ORDER: List[_RGV_O01_ORDER] = Field(
        default=...,
        title="ORDER",
        description="Required, repeating",
    )

    model_config = {"populate_by_name": True}

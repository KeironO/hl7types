"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3.1
Class: OMS_O01
Type: Message
"""
from _future__ import annotations

from typing import Optional, List
from pydantic import BaseModel, Field

from ..segments.MSH import MSH
from ..segments.NTE import NTE

from ..groups.OMS_O01_ORDER import OMS_O01_ORDER
from ..groups.OMS_O01_PATIENT import OMS_O01_PATIENT

_MSH = MSH
_NTE = NTE
_OMS_O01_ORDER = OMS_O01_ORDER
_OMS_O01_PATIENT = OMS_O01_PATIENT


class OMS_O01(BaseModel):
    """HL7 v2 OMS_O01 message.

    Attributes:
        MSH (MSH): required
        NTE (Optional[List[NTE]]): optional
        PATIENT (Optional[OMS_O01_PATIENT]): optional
        ORDER (List[OMS_O01_ORDER]): required
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

    PATIENT: Optional[_OMS_O01_PATIENT] = Field(
        default=None,
        title="PATIENT",
        description="Optional",
    )

    ORDER: List[_OMS_O01_ORDER] = Field(
        default=...,
        title="ORDER",
        description="Required, repeating",
    )

    model_config = {"populate_by_name": True}

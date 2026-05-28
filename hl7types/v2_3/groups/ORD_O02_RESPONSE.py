"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3
Class: ORD_O02.RESPONSE
Type: Group
"""
from _future__ import annotations

from typing import Optional, List
from pydantic import BaseModel, Field

from .ORD_O02_ORDER_DIET import ORD_O02_ORDER_DIET
from .ORD_O02_ORDER_TRAY import ORD_O02_ORDER_TRAY
from .ORD_O02_PATIENT import ORD_O02_PATIENT

_ORD_O02_ORDER_DIET = ORD_O02_ORDER_DIET
_ORD_O02_ORDER_TRAY = ORD_O02_ORDER_TRAY
_ORD_O02_PATIENT = ORD_O02_PATIENT


class ORD_O02_RESPONSE(BaseModel):
    """HL7 v2 ORD_O02.RESPONSE group.

    Attributes:
        PATIENT (Optional[ORD_O02_PATIENT]): optional
        ORDER_DIET (List[ORD_O02_ORDER_DIET]): required
        ORDER_TRAY (Optional[List[ORD_O02_ORDER_TRAY]]): optional
    """

    PATIENT: Optional[_ORD_O02_PATIENT] = Field(
        default=None,
        title="PATIENT",
        description="Optional",
    )

    ORDER_DIET: List[_ORD_O02_ORDER_DIET] = Field(
        default=...,
        title="ORDER_DIET",
        description="Required, repeating",
    )

    ORDER_TRAY: Optional[List[_ORD_O02_ORDER_TRAY]] = Field(
        default=None,
        title="ORDER_TRAY",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}

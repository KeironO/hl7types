"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7
Class: ORD_O04.RESPONSE
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import ConfigDict, Field
from hl7types.hl7 import HL7Model

from .ORD_O04_ORDER_DIET import ORD_O04_ORDER_DIET
from .ORD_O04_ORDER_TRAY import ORD_O04_ORDER_TRAY
from .ORD_O04_PATIENT import ORD_O04_PATIENT

_ORD_O04_ORDER_DIET = ORD_O04_ORDER_DIET
_ORD_O04_ORDER_TRAY = ORD_O04_ORDER_TRAY
_ORD_O04_PATIENT = ORD_O04_PATIENT


class ORD_O04_RESPONSE(HL7Model):
    """HL7 v2 ORD_O04.RESPONSE group.

    Attributes:
        PATIENT (Optional[ORD_O04_PATIENT]): optional
        ORDER_DIET (List[ORD_O04_ORDER_DIET]): required
        ORDER_TRAY (Optional[List[ORD_O04_ORDER_TRAY]]): optional
    """

    PATIENT: Optional[_ORD_O04_PATIENT] = Field(
        default=None,
        title="PATIENT",
    )

    ORDER_DIET: List[_ORD_O04_ORDER_DIET] = Field(
        min_length=1,
        title="ORDER_DIET",
    )

    ORDER_TRAY: Optional[List[_ORD_O04_ORDER_TRAY]] = Field(
        default=None,
        title="ORDER_TRAY",
    )

    model_config = ConfigDict(populate_by_name=True)

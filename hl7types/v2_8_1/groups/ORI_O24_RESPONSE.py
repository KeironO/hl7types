"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.1
Class: ORI_O24.RESPONSE
Type: Group
"""
from _future__ import annotations

from typing import Optional, List
from pydantic import BaseModel, Field

from .ORI_O24_ORDER import ORI_O24_ORDER
from .ORI_O24_PATIENT import ORI_O24_PATIENT

_ORI_O24_ORDER = ORI_O24_ORDER
_ORI_O24_PATIENT = ORI_O24_PATIENT


class ORI_O24_RESPONSE(BaseModel):
    """HL7 v2 ORI_O24.RESPONSE group.

    Attributes:
        PATIENT (Optional[ORI_O24_PATIENT]): optional
        ORDER (List[ORI_O24_ORDER]): required
    """

    PATIENT: Optional[_ORI_O24_PATIENT] = Field(
        default=None,
        title="PATIENT",
        description="Optional",
    )

    ORDER: List[_ORI_O24_ORDER] = Field(
        default=...,
        title="ORDER",
        description="Required, repeating",
    )

    model_config = {"populate_by_name": True}

"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.1
Class: ORM_O01
Type: Message
"""
from _future__ import annotations

from typing import Optional, List
from pydantic import BaseModel, Field

from ..segments.MSH import MSH
from ..segments.NTE import NTE

from ..groups.ORM_O01_ORDER import ORM_O01_ORDER
from ..groups.ORM_O01_PATIENT import ORM_O01_PATIENT

_MSH = MSH
_NTE = NTE
_ORM_O01_ORDER = ORM_O01_ORDER
_ORM_O01_PATIENT = ORM_O01_PATIENT


class ORM_O01(BaseModel):
    """HL7 v2 ORM_O01 message.

    Attributes:
        MSH (MSH): required
        NTE (Optional[List[NTE]]): optional
        PATIENT (Optional[ORM_O01_PATIENT]): optional
        ORDER (List[ORM_O01_ORDER]): required
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

    PATIENT: Optional[_ORM_O01_PATIENT] = Field(
        default=None,
        title="PATIENT",
        description="Optional",
    )

    ORDER: List[_ORM_O01_ORDER] = Field(
        default=...,
        title="ORDER",
        description="Required, repeating",
    )

    model_config = {"populate_by_name": True}

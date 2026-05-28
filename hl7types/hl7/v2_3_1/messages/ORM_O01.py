"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3.1
Class: ORM_O01
Type: Message
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..groups.ORM_O01_ORDER import ORM_O01_ORDER
from ..groups.ORM_O01_PATIENT import ORM_O01_PATIENT
from ..segments.MSH import MSH
from ..segments.NTE import NTE

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

    NTE: list[_NTE] | None = Field(
        default=None,
        title="NTE",
        description="Optional, repeating",
    )

    PATIENT: _ORM_O01_PATIENT | None = Field(
        default=None,
        title="PATIENT",
        description="Optional",
    )

    ORDER: list[_ORM_O01_ORDER] = Field(
        default=...,
        title="ORDER",
        description="Required, repeating",
    )

    model_config = {"populate_by_name": True}

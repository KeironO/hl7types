"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3
Class: OMN_O01
Type: Message
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..groups.OMN_O01_ORDER import OMN_O01_ORDER
from ..groups.OMN_O01_PATIENT import OMN_O01_PATIENT
from ..segments.MSH import MSH
from ..segments.NTE import NTE

_MSH = MSH
_NTE = NTE
_OMN_O01_ORDER = OMN_O01_ORDER
_OMN_O01_PATIENT = OMN_O01_PATIENT


class OMN_O01(BaseModel):
    """HL7 v2 OMN_O01 message.

    Attributes:
        MSH (MSH): required
        NTE (Optional[List[NTE]]): optional
        PATIENT (Optional[OMN_O01_PATIENT]): optional
        ORDER (List[OMN_O01_ORDER]): required
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

    PATIENT: _OMN_O01_PATIENT | None = Field(
        default=None,
        title="PATIENT",
        description="Optional",
    )

    ORDER: list[_OMN_O01_ORDER] = Field(
        default=...,
        title="ORDER",
        description="Required, repeating",
    )

    model_config = {"populate_by_name": True}

"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3.1
Class: RDO_O01
Type: Message
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..groups.RDO_O01_ORDER import RDO_O01_ORDER
from ..groups.RDO_O01_PATIENT import RDO_O01_PATIENT
from ..segments.MSH import MSH
from ..segments.NTE import NTE

_MSH = MSH
_NTE = NTE
_RDO_O01_ORDER = RDO_O01_ORDER
_RDO_O01_PATIENT = RDO_O01_PATIENT


class RDO_O01(BaseModel):
    """HL7 v2 RDO_O01 message.

    Attributes:
        MSH (MSH): required
        NTE (Optional[List[NTE]]): optional
        PATIENT (Optional[RDO_O01_PATIENT]): optional
        ORDER (List[RDO_O01_ORDER]): required
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

    PATIENT: _RDO_O01_PATIENT | None = Field(
        default=None,
        title="PATIENT",
        description="Optional",
    )

    ORDER: list[_RDO_O01_ORDER] = Field(
        default=...,
        title="ORDER",
        description="Required, repeating",
    )

    model_config = {"populate_by_name": True}

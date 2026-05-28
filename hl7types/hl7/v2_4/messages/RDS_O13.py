"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.4
Class: RDS_O13
Type: Message
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..groups.RDS_O13_ORDER import RDS_O13_ORDER
from ..groups.RDS_O13_PATIENT import RDS_O13_PATIENT
from ..segments.MSH import MSH
from ..segments.NTE import NTE

_MSH = MSH
_NTE = NTE
_RDS_O13_ORDER = RDS_O13_ORDER
_RDS_O13_PATIENT = RDS_O13_PATIENT


class RDS_O13(BaseModel):
    """HL7 v2 RDS_O13 message.

    Attributes:
        MSH (MSH): required
        NTE (Optional[List[NTE]]): optional
        PATIENT (Optional[RDS_O13_PATIENT]): optional
        ORDER (List[RDS_O13_ORDER]): required
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

    PATIENT: _RDS_O13_PATIENT | None = Field(
        default=None,
        title="PATIENT",
        description="Optional",
    )

    ORDER: list[_RDS_O13_ORDER] = Field(
        default=...,
        title="ORDER",
        description="Required, repeating",
    )

    model_config = {"populate_by_name": True}

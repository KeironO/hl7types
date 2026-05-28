"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.4
Class: OMG_O19
Type: Message
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..groups.OMG_O19_ORDER import OMG_O19_ORDER
from ..groups.OMG_O19_PATIENT import OMG_O19_PATIENT
from ..segments.MSH import MSH
from ..segments.NTE import NTE

_MSH = MSH
_NTE = NTE
_OMG_O19_ORDER = OMG_O19_ORDER
_OMG_O19_PATIENT = OMG_O19_PATIENT


class OMG_O19(BaseModel):
    """HL7 v2 OMG_O19 message.

    Attributes:
        MSH (MSH): required
        NTE (Optional[List[NTE]]): optional
        PATIENT (Optional[OMG_O19_PATIENT]): optional
        ORDER (List[OMG_O19_ORDER]): required
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

    PATIENT: _OMG_O19_PATIENT | None = Field(
        default=None,
        title="PATIENT",
        description="Optional",
    )

    ORDER: list[_OMG_O19_ORDER] = Field(
        default=...,
        title="ORDER",
        description="Required, repeating",
    )

    model_config = {"populate_by_name": True}

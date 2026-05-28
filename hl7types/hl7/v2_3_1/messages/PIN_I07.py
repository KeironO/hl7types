"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3.1
Class: PIN_I07
Type: Message
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..groups.PIN_I07_GUARANTOR_INSURANCE import PIN_I07_GUARANTOR_INSURANCE
from ..groups.PIN_I07_PROVIDER import PIN_I07_PROVIDER
from ..segments.MSH import MSH
from ..segments.NK1 import NK1
from ..segments.NTE import NTE
from ..segments.PID import PID

_MSH = MSH
_NK1 = NK1
_NTE = NTE
_PID = PID
_PIN_I07_GUARANTOR_INSURANCE = PIN_I07_GUARANTOR_INSURANCE
_PIN_I07_PROVIDER = PIN_I07_PROVIDER


class PIN_I07(BaseModel):
    """HL7 v2 PIN_I07 message.

    Attributes:
        MSH (MSH): required
        PROVIDER (List[PIN_I07_PROVIDER]): required
        PID (PID): required
        NK1 (Optional[List[NK1]]): optional
        GUARANTOR_INSURANCE (Optional[PIN_I07_GUARANTOR_INSURANCE]): optional
        NTE (Optional[List[NTE]]): optional
    """

    MSH: _MSH = Field(
        default=...,
        title="MSH",
        description="Required",
    )

    PROVIDER: list[_PIN_I07_PROVIDER] = Field(
        default=...,
        title="PROVIDER",
        description="Required, repeating",
    )

    PID: _PID = Field(
        default=...,
        title="PID",
        description="Required",
    )

    NK1: list[_NK1] | None = Field(
        default=None,
        title="NK1",
        description="Optional, repeating",
    )

    GUARANTOR_INSURANCE: _PIN_I07_GUARANTOR_INSURANCE | None = Field(
        default=None,
        title="GUARANTOR_INSURANCE",
        description="Optional",
    )

    NTE: list[_NTE] | None = Field(
        default=None,
        title="NTE",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}

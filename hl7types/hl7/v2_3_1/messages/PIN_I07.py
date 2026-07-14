"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3.1
Class: PIN_I07
Type: Message
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.MSH import MSH
from ..segments.NK1 import NK1
from ..segments.NTE import NTE
from ..segments.PID import PID

from ..groups.PIN_I07_GUARANTOR_INSURANCE import PIN_I07_GUARANTOR_INSURANCE
from ..groups.PIN_I07_PROVIDER import PIN_I07_PROVIDER

_MSH = MSH
_NK1 = NK1
_NTE = NTE
_PID = PID
_PIN_I07_GUARANTOR_INSURANCE = PIN_I07_GUARANTOR_INSURANCE
_PIN_I07_PROVIDER = PIN_I07_PROVIDER


class PIN_I07(HL7Model):
    """PIN/ACK - Unsolicited insurance information.

    Attributes:
        MSH (MSH): MSH - message header segment, required
        PROVIDER (List[PIN_I07_PROVIDER]): required
        PID (PID): PID - patient identification segment, required
        NK1 (Optional[List[NK1]]): NK1 - next of kin / associated parties segment-, optional
        GUARANTOR_INSURANCE (Optional[PIN_I07_GUARANTOR_INSURANCE]): optional
        NTE (Optional[List[NTE]]): NTE - notes and comments segment, optional
    """

    MSH: _MSH = Field(
        title="MSH",
        description="MSH - message header segment",
    )

    PROVIDER: List[_PIN_I07_PROVIDER] = Field(
        min_length=1,
        title="PROVIDER",
    )

    PID: _PID = Field(
        title="PID",
        description="PID - patient identification segment",
    )

    NK1: Optional[List[_NK1]] = Field(
        default=None,
        title="NK1",
        description="NK1 - next of kin / associated parties segment-",
    )

    GUARANTOR_INSURANCE: Optional[_PIN_I07_GUARANTOR_INSURANCE] = Field(
        default=None,
        title="GUARANTOR_INSURANCE",
    )

    NTE: Optional[List[_NTE]] = Field(
        default=None,
        title="NTE",
        description="NTE - notes and comments segment",
    )

    model_config = {"populate_by_name": True}

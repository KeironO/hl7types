"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.4
Class: RQP_I04
Type: Message
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.GT1 import GT1
from ..segments.MSH import MSH
from ..segments.NK1 import NK1
from ..segments.NTE import NTE
from ..segments.PID import PID

from ..groups.RQP_I04_PROVIDER import RQP_I04_PROVIDER

_GT1 = GT1
_MSH = MSH
_NK1 = NK1
_NTE = NTE
_PID = PID
_RQP_I04_PROVIDER = RQP_I04_PROVIDER


class RQP_I04(HL7Model):
    """RQD/RPI - Request for patient demographic data (S11).

    Attributes:
        MSH (MSH): Message Header, required
        PROVIDER (List[RQP_I04_PROVIDER]): required
        PID (PID): Patient identification, required
        NK1 (Optional[List[NK1]]): Next of kin / associated parties, optional
        GT1 (Optional[List[GT1]]): Guarantor, optional
        NTE (Optional[List[NTE]]): Notes and Comments, optional
    """

    MSH: _MSH = Field(
        title="MSH",
        description="Message Header",
    )

    PROVIDER: List[_RQP_I04_PROVIDER] = Field(
        min_length=1,
        title="PROVIDER",
    )

    PID: _PID = Field(
        title="PID",
        description="Patient identification",
    )

    NK1: Optional[List[_NK1]] = Field(
        default=None,
        title="NK1",
        description="Next of kin / associated parties",
    )

    GT1: Optional[List[_GT1]] = Field(
        default=None,
        title="GT1",
        description="Guarantor",
    )

    NTE: Optional[List[_NTE]] = Field(
        default=None,
        title="NTE",
        description="Notes and Comments",
    )

    model_config = {"populate_by_name": True}

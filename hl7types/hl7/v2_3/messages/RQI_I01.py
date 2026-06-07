"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3
Class: RQI_I01
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

from ..groups.RQI_I01_GUARANTOR_INSURANCE import RQI_I01_GUARANTOR_INSURANCE
from ..groups.RQI_I01_PROVIDER import RQI_I01_PROVIDER

_MSH = MSH
_NK1 = NK1
_NTE = NTE
_PID = PID
_RQI_I01_GUARANTOR_INSURANCE = RQI_I01_GUARANTOR_INSURANCE
_RQI_I01_PROVIDER = RQI_I01_PROVIDER


class RQI_I01(HL7Model):
    """HL7 v2 RQI_I01 message.

    Attributes:
        MSH (MSH): required
        PROVIDER (List[RQI_I01_PROVIDER]): required
        PID (PID): required
        NK1 (Optional[List[NK1]]): optional
        GUARANTOR_INSURANCE (Optional[RQI_I01_GUARANTOR_INSURANCE]): optional
        NTE (Optional[List[NTE]]): optional
    """

    MSH: _MSH = Field(
        title="MSH",
        description="Required",
    )

    PROVIDER: List[_RQI_I01_PROVIDER] = Field(
        min_length=1,
        title="PROVIDER",
        description="Required, repeating",
    )

    PID: _PID = Field(
        title="PID",
        description="Required",
    )

    NK1: Optional[List[_NK1]] = Field(
        default=None,
        title="NK1",
        description="Optional, repeating",
    )

    GUARANTOR_INSURANCE: Optional[_RQI_I01_GUARANTOR_INSURANCE] = Field(
        default=None,
        title="GUARANTOR_INSURANCE",
        description="Optional",
    )

    NTE: Optional[List[_NTE]] = Field(
        default=None,
        title="NTE",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}

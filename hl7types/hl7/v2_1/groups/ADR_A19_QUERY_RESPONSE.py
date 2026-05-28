"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.1
Class: ADR_A19.QUERY_RESPONSE
Type: Group
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..segments.EVN import EVN
from ..segments.PID import PID
from ..segments.PV1 import PV1

_EVN = EVN
_PID = PID
_PV1 = PV1


class ADR_A19_QUERY_RESPONSE(BaseModel):
    """HL7 v2 ADR_A19.QUERY_RESPONSE group.

    Attributes:
        EVN (Optional[EVN]): optional
        PID (PID): required
        PV1 (PV1): required
    """

    EVN: _EVN | None = Field(
        default=None,
        title="EVN",
        description="Optional",
    )

    PID: _PID = Field(
        default=...,
        title="PID",
        description="Required",
    )

    PV1: _PV1 = Field(
        default=...,
        title="PV1",
        description="Required",
    )

    model_config = {"populate_by_name": True}

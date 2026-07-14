"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.1
Class: ADR_A19.QUERY_RESPONSE
Type: Group
"""
from __future__ import annotations

from typing import Optional
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.EVN import EVN
from ..segments.PID import PID
from ..segments.PV1 import PV1

_EVN = EVN
_PID = PID
_PV1 = PV1


class ADR_A19_QUERY_RESPONSE(HL7Model):
    """HL7 v2 ADR_A19.QUERY_RESPONSE group.

    Attributes:
        EVN (Optional[EVN]): EVENT TYPE, optional
        PID (PID): PATIENT IDENTIFICATION, required
        PV1 (PV1): PATIENT VISIT, required
    """

    EVN: Optional[_EVN] = Field(
        default=None,
        title="EVN",
        description="EVENT TYPE",
    )

    PID: _PID = Field(
        title="PID",
        description="PATIENT IDENTIFICATION",
    )

    PV1: _PV1 = Field(
        title="PV1",
        description="PATIENT VISIT",
    )

    model_config = {"populate_by_name": True}

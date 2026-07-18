"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3
Class: SQR_S25.SERVICE
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import ConfigDict, Field
from hl7types.hl7 import HL7Model

from ..segments.AIS import AIS
from ..segments.NTE import NTE

_AIS = AIS
_NTE = NTE


class SQR_S25_SERVICE(HL7Model):
    """HL7 v2 SQR_S25.SERVICE group.

    Attributes:
        AIS (AIS): Appointment Information - Service, required
        NTE (Optional[List[NTE]]): Notes and comments segment, optional
    """

    AIS: _AIS = Field(
        title="AIS",
        description="Appointment Information - Service",
    )

    NTE: Optional[List[_NTE]] = Field(
        default=None,
        title="NTE",
        description="Notes and comments segment",
    )

    model_config = ConfigDict(populate_by_name=True)

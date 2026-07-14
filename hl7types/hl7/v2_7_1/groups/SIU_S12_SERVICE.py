"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7.1
Class: SIU_S12.SERVICE
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.AIS import AIS
from ..segments.NTE import NTE

_AIS = AIS
_NTE = NTE


class SIU_S12_SERVICE(HL7Model):
    """HL7 v2 SIU_S12.SERVICE group.

    Attributes:
        AIS (AIS): Appointment Information, required
        NTE (Optional[List[NTE]]): Notes and Comments, optional
    """

    AIS: _AIS = Field(
        title="AIS",
        description="Appointment Information",
    )

    NTE: Optional[List[_NTE]] = Field(
        default=None,
        title="NTE",
        description="Notes and Comments",
    )

    model_config = {"populate_by_name": True}

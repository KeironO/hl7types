"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3.1
Class: SQR_S25.SERVICE
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


class SQR_S25_SERVICE(HL7Model):
    """HL7 v2 SQR_S25.SERVICE group.

    Attributes:
        AIS (AIS): AIS - appointment information - service segment, required
        NTE (Optional[List[NTE]]): NTE - notes and comments segment, optional
    """

    AIS: _AIS = Field(
        title="AIS",
        description="AIS - appointment information - service segment",
    )

    NTE: Optional[List[_NTE]] = Field(
        default=None,
        title="NTE",
        description="NTE - notes and comments segment",
    )

    model_config = {"populate_by_name": True}

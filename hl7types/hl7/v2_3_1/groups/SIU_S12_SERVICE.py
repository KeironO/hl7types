"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3.1
Class: SIU_S12.SERVICE
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


class SIU_S12_SERVICE(HL7Model):
    """HL7 v2 SIU_S12.SERVICE group.

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

    model_config = ConfigDict(populate_by_name=True)

"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3.1
Class: SIU_S12.PERSONNEL_RESOURCE
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.AIP import AIP
from ..segments.NTE import NTE

_AIP = AIP
_NTE = NTE


class SIU_S12_PERSONNEL_RESOURCE(HL7Model):
    """HL7 v2 SIU_S12.PERSONNEL_RESOURCE group.

    Attributes:
        AIP (AIP): AIP - appointment information - personnel resource segment, required
        NTE (Optional[List[NTE]]): NTE - notes and comments segment, optional
    """

    AIP: _AIP = Field(
        title="AIP",
        description=(
            "AIP - appointment information - personnel resource segment"
        ),
    )

    NTE: Optional[List[_NTE]] = Field(
        default=None,
        title="NTE",
        description="NTE - notes and comments segment",
    )

    model_config = {"populate_by_name": True}

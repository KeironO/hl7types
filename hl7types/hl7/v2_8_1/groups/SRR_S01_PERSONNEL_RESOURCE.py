"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.1
Class: SRR_S01.PERSONNEL_RESOURCE
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import ConfigDict, Field
from hl7types.hl7 import HL7Model

from ..segments.AIP import AIP
from ..segments.NTE import NTE

_AIP = AIP
_NTE = NTE


class SRR_S01_PERSONNEL_RESOURCE(HL7Model):
    """HL7 v2 SRR_S01.PERSONNEL_RESOURCE group.

    Attributes:
        AIP (AIP): Appointment Information - Personnel Resource, required
        NTE (Optional[List[NTE]]): Notes and Comments, optional
    """

    AIP: _AIP = Field(
        title="AIP",
        description="Appointment Information - Personnel Resource",
    )

    NTE: Optional[List[_NTE]] = Field(
        default=None,
        title="NTE",
        description="Notes and Comments",
    )

    model_config = ConfigDict(populate_by_name=True)

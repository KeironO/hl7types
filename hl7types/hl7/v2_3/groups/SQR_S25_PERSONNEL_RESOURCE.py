"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3
Class: SQR_S25.PERSONNEL_RESOURCE
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


class SQR_S25_PERSONNEL_RESOURCE(HL7Model):
    """HL7 v2 SQR_S25.PERSONNEL_RESOURCE group.

    Attributes:
        AIP (AIP): Appointment Information - Personnel Resource, required
        NTE (Optional[List[NTE]]): Notes and comments segment, optional
    """

    AIP: _AIP = Field(
        title="AIP",
        description="Appointment Information - Personnel Resource",
    )

    NTE: Optional[List[_NTE]] = Field(
        default=None,
        title="NTE",
        description="Notes and comments segment",
    )

    model_config = ConfigDict(populate_by_name=True)

"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5
Class: SRM_S01.SERVICE
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.AIS import AIS
from ..segments.APR import APR
from ..segments.NTE import NTE

_AIS = AIS
_APR = APR
_NTE = NTE


class SRM_S01_SERVICE(HL7Model):
    """HL7 v2 SRM_S01.SERVICE group.

    Attributes:
        AIS (AIS): Appointment Information, required
        APR (Optional[APR]): Appointment Preferences, optional
        NTE (Optional[List[NTE]]): Notes and Comments, optional
    """

    AIS: _AIS = Field(
        title="AIS",
        description="Appointment Information",
    )

    APR: Optional[_APR] = Field(
        default=None,
        title="APR",
        description="Appointment Preferences",
    )

    NTE: Optional[List[_NTE]] = Field(
        default=None,
        title="NTE",
        description="Notes and Comments",
    )

    model_config = {"populate_by_name": True}

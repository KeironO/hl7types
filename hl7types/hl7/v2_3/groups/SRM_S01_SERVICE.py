"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3
Class: SRM_S01.SERVICE
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import ConfigDict, Field
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
        AIS (AIS): Appointment Information - Service, required
        APR (Optional[APR]): Appointment Preferences, optional
        NTE (Optional[List[NTE]]): Notes and comments segment, optional
    """

    AIS: _AIS = Field(
        title="AIS",
        description="Appointment Information - Service",
    )

    APR: Optional[_APR] = Field(
        default=None,
        title="APR",
        description="Appointment Preferences",
    )

    NTE: Optional[List[_NTE]] = Field(
        default=None,
        title="NTE",
        description="Notes and comments segment",
    )

    model_config = ConfigDict(populate_by_name=True)

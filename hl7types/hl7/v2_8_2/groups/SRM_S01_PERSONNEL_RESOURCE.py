"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.2
Class: SRM_S01.PERSONNEL_RESOURCE
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.AIP import AIP
from ..segments.APR import APR
from ..segments.NTE import NTE

_AIP = AIP
_APR = APR
_NTE = NTE


class SRM_S01_PERSONNEL_RESOURCE(HL7Model):
    """HL7 v2 SRM_S01.PERSONNEL_RESOURCE group.

    Attributes:
        AIP (AIP): Appointment Information - Personnel Resource, required
        APR (Optional[APR]): Appointment Preferences, optional
        NTE (Optional[List[NTE]]): Notes and Comments, optional
    """

    AIP: _AIP = Field(
        title="AIP",
        description="Appointment Information - Personnel Resource",
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

"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8
Class: SRM_S01.LOCATION_RESOURCE
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.AIL import AIL
from ..segments.APR import APR
from ..segments.NTE import NTE

_AIL = AIL
_APR = APR
_NTE = NTE


class SRM_S01_LOCATION_RESOURCE(HL7Model):
    """HL7 v2 SRM_S01.LOCATION_RESOURCE group.

    Attributes:
        AIL (AIL): Appointment Information - Location Resource, required
        APR (Optional[APR]): Appointment Preferences, optional
        NTE (Optional[List[NTE]]): Notes and Comments, optional
    """

    AIL: _AIL = Field(
        title="AIL",
        description="Appointment Information - Location Resource",
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

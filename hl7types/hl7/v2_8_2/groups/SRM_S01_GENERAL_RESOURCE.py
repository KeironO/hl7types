"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.2
Class: SRM_S01.GENERAL_RESOURCE
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import ConfigDict, Field
from hl7types.hl7 import HL7Model

from ..segments.AIG import AIG
from ..segments.APR import APR
from ..segments.NTE import NTE

_AIG = AIG
_APR = APR
_NTE = NTE


class SRM_S01_GENERAL_RESOURCE(HL7Model):
    """HL7 v2 SRM_S01.GENERAL_RESOURCE group.

    Attributes:
        AIG (AIG): Appointment Information - General Resource, required
        APR (Optional[APR]): Appointment Preferences, optional
        NTE (Optional[List[NTE]]): Notes and Comments, optional
    """

    AIG: _AIG = Field(
        title="AIG",
        description="Appointment Information - General Resource",
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

    model_config = ConfigDict(populate_by_name=True)

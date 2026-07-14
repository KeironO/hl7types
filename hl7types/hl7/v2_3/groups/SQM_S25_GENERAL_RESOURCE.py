"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3
Class: SQM_S25.GENERAL_RESOURCE
Type: Group
"""
from __future__ import annotations

from typing import Optional
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.AIG import AIG
from ..segments.APR import APR

_AIG = AIG
_APR = APR


class SQM_S25_GENERAL_RESOURCE(HL7Model):
    """HL7 v2 SQM_S25.GENERAL_RESOURCE group.

    Attributes:
        AIG (AIG): Appointment Information - General Resource, required
        APR (Optional[APR]): Appointment Preferences, optional
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

    model_config = {"populate_by_name": True}

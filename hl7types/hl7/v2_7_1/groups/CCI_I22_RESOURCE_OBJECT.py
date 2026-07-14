"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7.1
Class: CCI_I22.RESOURCE_OBJECT
Type: Group
"""
from __future__ import annotations

from typing import Optional
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.AIG import AIG
from ..segments.AIL import AIL
from ..segments.AIP import AIP
from ..segments.AIS import AIS

_AIG = AIG
_AIL = AIL
_AIP = AIP
_AIS = AIS


class CCI_I22_RESOURCE_OBJECT(HL7Model):
    """HL7 v2 CCI_I22.RESOURCE_OBJECT group.

    Attributes:
        AIS (Optional[AIS]): Appointment Information, optional
        AIG (Optional[AIG]): Appointment Information - General Resource, optional
        AIL (Optional[AIL]): Appointment Information - Location Resource, optional
        AIP (Optional[AIP]): Appointment Information - Personnel Resource, optional
    """

    AIS: Optional[_AIS] = Field(
        default=None,
        title="AIS",
        description="Appointment Information",
    )

    AIG: Optional[_AIG] = Field(
        default=None,
        title="AIG",
        description="Appointment Information - General Resource",
    )

    AIL: Optional[_AIL] = Field(
        default=None,
        title="AIL",
        description="Appointment Information - Location Resource",
    )

    AIP: Optional[_AIP] = Field(
        default=None,
        title="AIP",
        description="Appointment Information - Personnel Resource",
    )

    model_config = {"populate_by_name": True}

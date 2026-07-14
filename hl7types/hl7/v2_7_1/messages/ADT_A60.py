"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7.1
Class: ADT_A60
Type: Message
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.ARV import ARV
from ..segments.EVN import EVN
from ..segments.MSH import MSH
from ..segments.PID import PID
from ..segments.SFT import SFT
from ..segments.UAC import UAC

from ..groups.ADT_A60_ADVERSE_REACTION_GROUP import ADT_A60_ADVERSE_REACTION_GROUP
from ..groups.ADT_A60_VISIT import ADT_A60_VISIT

_ADT_A60_ADVERSE_REACTION_GROUP = ADT_A60_ADVERSE_REACTION_GROUP
_ADT_A60_VISIT = ADT_A60_VISIT
_ARV = ARV
_EVN = EVN
_MSH = MSH
_PID = PID
_SFT = SFT
_UAC = UAC


class ADT_A60(HL7Model):
    """ADT/ACK - Update allergy information (S3.3.1).

    Attributes:
        MSH (MSH): Message Header, required
        SFT (Optional[List[SFT]]): Software Segment, optional
        UAC (Optional[UAC]): User Authentication Credential Segment, optional
        EVN (EVN): Event Type, required
        PID (PID): Patient Identification, required
        ARV (Optional[List[ARV]]): Access Restriction, optional
        VISIT (Optional[ADT_A60_VISIT]): optional
        ADVERSE_REACTION_GROUP (Optional[List[ADT_A60_ADVERSE_REACTION_GROUP]]): optional
    """

    MSH: _MSH = Field(
        title="MSH",
        description="Message Header",
    )

    SFT: Optional[List[_SFT]] = Field(
        default=None,
        title="SFT",
        description="Software Segment",
    )

    UAC: Optional[_UAC] = Field(
        default=None,
        title="UAC",
        description="User Authentication Credential Segment",
    )

    EVN: _EVN = Field(
        title="EVN",
        description="Event Type",
    )

    PID: _PID = Field(
        title="PID",
        description="Patient Identification",
    )

    ARV: Optional[List[_ARV]] = Field(
        default=None,
        title="ARV",
        description="Access Restriction",
    )

    VISIT: Optional[_ADT_A60_VISIT] = Field(
        default=None,
        title="VISIT",
    )

    ADVERSE_REACTION_GROUP: Optional[List[_ADT_A60_ADVERSE_REACTION_GROUP]] = Field(
        default=None,
        title="ADVERSE_REACTION_GROUP",
    )

    model_config = {"populate_by_name": True}

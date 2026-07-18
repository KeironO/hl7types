"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.6
Class: ADT_A60
Type: Message
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import ConfigDict, Field
from hl7types.hl7 import HL7Model

from ..segments.ARV import ARV
from ..segments.EVN import EVN
from ..segments.IAM import IAM
from ..segments.MSH import MSH
from ..segments.PID import PID
from ..segments.SFT import SFT
from ..segments.UAC import UAC

from ..groups.ADT_A60_VISIT import ADT_A60_VISIT

_ADT_A60_VISIT = ADT_A60_VISIT
_ARV = ARV
_EVN = EVN
_IAM = IAM
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
        IAM (Optional[List[IAM]]): Patient Adverse Reaction Information, optional
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

    IAM: Optional[List[_IAM]] = Field(
        default=None,
        title="IAM",
        description="Patient Adverse Reaction Information",
    )

    model_config = ConfigDict(populate_by_name=True)

"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.4
Class: ADT_A60
Type: Message
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import ConfigDict, Field
from hl7types.hl7 import HL7Model

from ..segments.EVN import EVN
from ..segments.IAM import IAM
from ..segments.MSH import MSH
from ..segments.PID import PID
from ..segments.PV1 import PV1
from ..segments.PV2 import PV2

_EVN = EVN
_IAM = IAM
_MSH = MSH
_PID = PID
_PV1 = PV1
_PV2 = PV2


class ADT_A60(HL7Model):
    """ADT/ACK -  Update allergy information (S3).

    Attributes:
        MSH (MSH): Message Header, required
        EVN (EVN): Event Type, required
        PID (PID): Patient identification, required
        PV1 (Optional[PV1]): Patient visit, optional
        PV2 (Optional[PV2]): Patient visit - additional information, optional
        IAM (Optional[List[IAM]]): Patient adverse reaction information - unique iden, optional
    """

    MSH: _MSH = Field(
        title="MSH",
        description="Message Header",
    )

    EVN: _EVN = Field(
        title="EVN",
        description="Event Type",
    )

    PID: _PID = Field(
        title="PID",
        description="Patient identification",
    )

    PV1: Optional[_PV1] = Field(
        default=None,
        title="PV1",
        description="Patient visit",
    )

    PV2: Optional[_PV2] = Field(
        default=None,
        title="PV2",
        description="Patient visit - additional information",
    )

    IAM: Optional[List[_IAM]] = Field(
        default=None,
        title="IAM",
        description="Patient adverse reaction information - unique iden",
    )

    model_config = ConfigDict(populate_by_name=True)

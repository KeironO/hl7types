"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8
Class: MDM_T01
Type: Message
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import ConfigDict, Field
from hl7types.hl7 import HL7Model

from ..segments.CON import CON
from ..segments.EVN import EVN
from ..segments.MSH import MSH
from ..segments.PID import PID
from ..segments.PV1 import PV1
from ..segments.SFT import SFT
from ..segments.TXA import TXA
from ..segments.UAC import UAC

from ..groups.MDM_T01_COMMON_ORDER import MDM_T01_COMMON_ORDER

_CON = CON
_EVN = EVN
_MDM_T01_COMMON_ORDER = MDM_T01_COMMON_ORDER
_MSH = MSH
_PID = PID
_PV1 = PV1
_SFT = SFT
_TXA = TXA
_UAC = UAC


class MDM_T01(HL7Model):
    """MDM/ACK - Original document notification (S9.6.1).

    Attributes:
        MSH (MSH): Message Header, required
        SFT (Optional[List[SFT]]): Software Segment, optional
        UAC (Optional[UAC]): User Authentication Credential Segment, optional
        EVN (EVN): Event Type, required
        PID (PID): Patient Identification, required
        PV1 (PV1): Patient Visit, required
        COMMON_ORDER (Optional[List[MDM_T01_COMMON_ORDER]]): optional
        TXA (TXA): Transcription Document Header, required
        CON (Optional[List[CON]]): Consent Segment, optional
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

    PV1: _PV1 = Field(
        title="PV1",
        description="Patient Visit",
    )

    COMMON_ORDER: Optional[List[_MDM_T01_COMMON_ORDER]] = Field(
        default=None,
        title="COMMON_ORDER",
    )

    TXA: _TXA = Field(
        title="TXA",
        description="Transcription Document Header",
    )

    CON: Optional[List[_CON]] = Field(
        default=None,
        title="CON",
        description="Consent Segment",
    )

    model_config = ConfigDict(populate_by_name=True)

"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.1
Class: MDM_T02
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

from ..groups.MDM_T02_COMMON_ORDER import MDM_T02_COMMON_ORDER
from ..groups.MDM_T02_OBSERVATION import MDM_T02_OBSERVATION

_CON = CON
_EVN = EVN
_MDM_T02_COMMON_ORDER = MDM_T02_COMMON_ORDER
_MDM_T02_OBSERVATION = MDM_T02_OBSERVATION
_MSH = MSH
_PID = PID
_PV1 = PV1
_SFT = SFT
_TXA = TXA
_UAC = UAC


class MDM_T02(HL7Model):
    """MDM/ACK - Original document notification and content (S9.6.1).

    Attributes:
        MSH (MSH): Message Header, required
        SFT (Optional[List[SFT]]): Software Segment, optional
        UAC (Optional[UAC]): User Authentication Credential Segment, optional
        EVN (EVN): Event Type, required
        PID (PID): Patient Identification, required
        PV1 (PV1): Patient Visit, required
        COMMON_ORDER (Optional[List[MDM_T02_COMMON_ORDER]]): optional
        TXA (TXA): Transcription Document Header, required
        CON (Optional[List[CON]]): Consent Segment, optional
        OBSERVATION (List[MDM_T02_OBSERVATION]): required
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

    COMMON_ORDER: Optional[List[_MDM_T02_COMMON_ORDER]] = Field(
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

    OBSERVATION: List[_MDM_T02_OBSERVATION] = Field(
        min_length=1,
        title="OBSERVATION",
    )

    model_config = ConfigDict(populate_by_name=True)

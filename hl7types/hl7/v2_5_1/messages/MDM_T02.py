"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5.1
Class: MDM_T02
Type: Message
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import ConfigDict, Field
from hl7types.hl7 import HL7Model

from ..segments.EVN import EVN
from ..segments.MSH import MSH
from ..segments.PID import PID
from ..segments.PV1 import PV1
from ..segments.SFT import SFT
from ..segments.TXA import TXA

from ..groups.MDM_T02_COMMON_ORDER import MDM_T02_COMMON_ORDER
from ..groups.MDM_T02_OBXNTE_SUPPGRP import MDM_T02_OBXNTE_SUPPGRP

_EVN = EVN
_MDM_T02_COMMON_ORDER = MDM_T02_COMMON_ORDER
_MDM_T02_OBXNTE_SUPPGRP = MDM_T02_OBXNTE_SUPPGRP
_MSH = MSH
_PID = PID
_PV1 = PV1
_SFT = SFT
_TXA = TXA


class MDM_T02(HL7Model):
    """MDM/ACK - Original document notification and content (S9.5.1).

    Attributes:
        MSH (MSH): Message Header, required
        SFT (Optional[List[SFT]]): Software Segment, optional
        EVN (EVN): Event Type, required
        PID (PID): Patient Identification, required
        PV1 (PV1): Patient Visit, required
        COMMON_ORDER (Optional[List[MDM_T02_COMMON_ORDER]]): optional
        TXA (TXA): Transcription Document Header, required
        OBXNTE_SUPPGRP (List[MDM_T02_OBXNTE_SUPPGRP]): required
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

    OBXNTE_SUPPGRP: List[_MDM_T02_OBXNTE_SUPPGRP] = Field(
        min_length=1,
        title="OBXNTE_SUPPGRP",
    )

    model_config = ConfigDict(populate_by_name=True)

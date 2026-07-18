"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.6
Class: PMU_B01
Type: Message
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import ConfigDict, Field
from hl7types.hl7 import HL7Model

from ..segments.AFF import AFF
from ..segments.CER import CER
from ..segments.EDU import EDU
from ..segments.EVN import EVN
from ..segments.LAN import LAN
from ..segments.MSH import MSH
from ..segments.ORG import ORG
from ..segments.PRA import PRA
from ..segments.SFT import SFT
from ..segments.STF import STF
from ..segments.UAC import UAC

_AFF = AFF
_CER = CER
_EDU = EDU
_EVN = EVN
_LAN = LAN
_MSH = MSH
_ORG = ORG
_PRA = PRA
_SFT = SFT
_STF = STF
_UAC = UAC


class PMU_B01(HL7Model):
    """PMU/ACK - Add personnel record (S15.3.1).

    Attributes:
        MSH (MSH): Message Header, required
        SFT (Optional[List[SFT]]): Software Segment, optional
        UAC (Optional[UAC]): User Authentication Credential Segment, optional
        EVN (EVN): Event Type, required
        STF (STF): Staff Identification, required
        PRA (Optional[List[PRA]]): Practitioner Detail, optional
        ORG (Optional[List[ORG]]): Practitioner Organization Unit, optional
        AFF (Optional[List[AFF]]): Professional Affiliation, optional
        LAN (Optional[List[LAN]]): Language Detail, optional
        EDU (Optional[List[EDU]]): Educational Detail, optional
        CER (Optional[List[CER]]): Certificate Detail, optional
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

    STF: _STF = Field(
        title="STF",
        description="Staff Identification",
    )

    PRA: Optional[List[_PRA]] = Field(
        default=None,
        title="PRA",
        description="Practitioner Detail",
    )

    ORG: Optional[List[_ORG]] = Field(
        default=None,
        title="ORG",
        description="Practitioner Organization Unit",
    )

    AFF: Optional[List[_AFF]] = Field(
        default=None,
        title="AFF",
        description="Professional Affiliation",
    )

    LAN: Optional[List[_LAN]] = Field(
        default=None,
        title="LAN",
        description="Language Detail",
    )

    EDU: Optional[List[_EDU]] = Field(
        default=None,
        title="EDU",
        description="Educational Detail",
    )

    CER: Optional[List[_CER]] = Field(
        default=None,
        title="CER",
        description="Certificate Detail",
    )

    model_config = ConfigDict(populate_by_name=True)

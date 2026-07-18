"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8
Class: PMU_B08
Type: Message
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import ConfigDict, Field
from hl7types.hl7 import HL7Model

from ..segments.CER import CER
from ..segments.EVN import EVN
from ..segments.MSH import MSH
from ..segments.PRA import PRA
from ..segments.SFT import SFT
from ..segments.STF import STF
from ..segments.UAC import UAC

_CER = CER
_EVN = EVN
_MSH = MSH
_PRA = PRA
_SFT = SFT
_STF = STF
_UAC = UAC


class PMU_B08(HL7Model):
    """PMU/ACK - Revoke Certificate/Permission (S15.3.1).

    Attributes:
        MSH (MSH): Message Header, required
        SFT (Optional[List[SFT]]): Software Segment, optional
        UAC (Optional[UAC]): User Authentication Credential Segment, optional
        EVN (EVN): Event Type, required
        STF (STF): Staff Identification, required
        PRA (Optional[PRA]): Practitioner Detail, optional
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

    PRA: Optional[_PRA] = Field(
        default=None,
        title="PRA",
        description="Practitioner Detail",
    )

    CER: Optional[List[_CER]] = Field(
        default=None,
        title="CER",
        description="Certificate Detail",
    )

    model_config = ConfigDict(populate_by_name=True)

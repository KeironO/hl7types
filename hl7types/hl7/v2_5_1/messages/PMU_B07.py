"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5.1
Class: PMU_B07
Type: Message
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.EVN import EVN
from ..segments.MSH import MSH
from ..segments.PRA import PRA
from ..segments.SFT import SFT
from ..segments.STF import STF

from ..groups.PMU_B07_CERTIFICATE import PMU_B07_CERTIFICATE

_EVN = EVN
_MSH = MSH
_PMU_B07_CERTIFICATE = PMU_B07_CERTIFICATE
_PRA = PRA
_SFT = SFT
_STF = STF


class PMU_B07(HL7Model):
    """PMU/ACK - Grant Certificate/Permission (S15.3.1).

    Attributes:
        MSH (MSH): Message Header, required
        SFT (Optional[List[SFT]]): Software Segment, optional
        EVN (EVN): Event Type, required
        STF (STF): Staff Identification, required
        PRA (Optional[PRA]): Practitioner Detail, optional
        CERTIFICATE (Optional[List[PMU_B07_CERTIFICATE]]): optional
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

    STF: _STF = Field(
        title="STF",
        description="Staff Identification",
    )

    PRA: Optional[_PRA] = Field(
        default=None,
        title="PRA",
        description="Practitioner Detail",
    )

    CERTIFICATE: Optional[List[_PMU_B07_CERTIFICATE]] = Field(
        default=None,
        title="CERTIFICATE",
    )

    model_config = {"populate_by_name": True}

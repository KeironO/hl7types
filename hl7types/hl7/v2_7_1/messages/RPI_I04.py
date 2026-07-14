"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7.1
Class: RPI_I04
Type: Message
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.MSA import MSA
from ..segments.MSH import MSH
from ..segments.NK1 import NK1
from ..segments.NTE import NTE
from ..segments.PID import PID
from ..segments.SFT import SFT
from ..segments.UAC import UAC

from ..groups.RPI_I04_GUARANTOR_INSURANCE import RPI_I04_GUARANTOR_INSURANCE
from ..groups.RPI_I04_PROVIDER import RPI_I04_PROVIDER

_MSA = MSA
_MSH = MSH
_NK1 = NK1
_NTE = NTE
_PID = PID
_RPI_I04_GUARANTOR_INSURANCE = RPI_I04_GUARANTOR_INSURANCE
_RPI_I04_PROVIDER = RPI_I04_PROVIDER
_SFT = SFT
_UAC = UAC


class RPI_I04(HL7Model):
    """RQD/RPI - Request for patient demographic data (S11.2.1).

    Attributes:
        MSH (MSH): Message Header, required
        SFT (Optional[List[SFT]]): Software Segment, optional
        UAC (Optional[UAC]): User Authentication Credential Segment, optional
        MSA (MSA): Message Acknowledgment, required
        PROVIDER (List[RPI_I04_PROVIDER]): required
        PID (PID): Patient Identification, required
        NK1 (Optional[List[NK1]]): Next of Kin / Associated Parties, optional
        GUARANTOR_INSURANCE (Optional[RPI_I04_GUARANTOR_INSURANCE]): optional
        NTE (Optional[List[NTE]]): Notes and Comments, optional
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

    MSA: _MSA = Field(
        title="MSA",
        description="Message Acknowledgment",
    )

    PROVIDER: List[_RPI_I04_PROVIDER] = Field(
        min_length=1,
        title="PROVIDER",
    )

    PID: _PID = Field(
        title="PID",
        description="Patient Identification",
    )

    NK1: Optional[List[_NK1]] = Field(
        default=None,
        title="NK1",
        description="Next of Kin / Associated Parties",
    )

    GUARANTOR_INSURANCE: Optional[_RPI_I04_GUARANTOR_INSURANCE] = Field(
        default=None,
        title="GUARANTOR_INSURANCE",
    )

    NTE: Optional[List[_NTE]] = Field(
        default=None,
        title="NTE",
        description="Notes and Comments",
    )

    model_config = {"populate_by_name": True}

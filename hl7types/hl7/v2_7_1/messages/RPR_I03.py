"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7.1
Class: RPR_I03
Type: Message
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.MSA import MSA
from ..segments.MSH import MSH
from ..segments.NTE import NTE
from ..segments.PID import PID
from ..segments.SFT import SFT
from ..segments.UAC import UAC

from ..groups.RPR_I03_PROVIDER import RPR_I03_PROVIDER

_MSA = MSA
_MSH = MSH
_NTE = NTE
_PID = PID
_RPR_I03_PROVIDER = RPR_I03_PROVIDER
_SFT = SFT
_UAC = UAC


class RPR_I03(HL7Model):
    """RQI/RPR - Request/receipt of patient selection list (S11.2.3).

    Attributes:
        MSH (MSH): Message Header, required
        SFT (Optional[List[SFT]]): Software Segment, optional
        UAC (Optional[UAC]): User Authentication Credential Segment, optional
        MSA (MSA): Message Acknowledgment, required
        PROVIDER (List[RPR_I03_PROVIDER]): required
        PID (Optional[List[PID]]): Patient Identification, optional
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

    PROVIDER: List[_RPR_I03_PROVIDER] = Field(
        min_length=1,
        title="PROVIDER",
    )

    PID: Optional[List[_PID]] = Field(
        default=None,
        title="PID",
        description="Patient Identification",
    )

    NTE: Optional[List[_NTE]] = Field(
        default=None,
        title="NTE",
        description="Notes and Comments",
    )

    model_config = {"populate_by_name": True}

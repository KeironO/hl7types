"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8
Class: OSU_O51
Type: Message
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.ARV import ARV
from ..segments.ERR import ERR
from ..segments.MSA import MSA
from ..segments.MSH import MSH
from ..segments.NTE import NTE
from ..segments.PID import PID
from ..segments.SFT import SFT
from ..segments.UAC import UAC

from ..groups.OSU_O51_ORDER_STATUS import OSU_O51_ORDER_STATUS

_ARV = ARV
_ERR = ERR
_MSA = MSA
_MSH = MSH
_NTE = NTE
_OSU_O51_ORDER_STATUS = OSU_O51_ORDER_STATUS
_PID = PID
_SFT = SFT
_UAC = UAC


class OSU_O51(HL7Model):
    """HL7 v2 OSU_O51 message.

    Attributes:
        MSH (MSH): Message Header, required
        MSA (MSA): Message Acknowledgment, required
        ERR (Optional[List[ERR]]): Error, optional
        SFT (Optional[List[SFT]]): Software Segment, optional
        UAC (Optional[UAC]): User Authentication Credential Segment, optional
        NTE (Optional[List[NTE]]): Notes and Comments, optional
        PID (Optional[PID]): Patient Identification, optional
        ARV (Optional[List[ARV]]): Access Restriction, optional
        ORDER_STATUS (List[OSU_O51_ORDER_STATUS]): required
    """

    MSH: _MSH = Field(
        title="MSH",
        description="Message Header",
    )

    MSA: _MSA = Field(
        title="MSA",
        description="Message Acknowledgment",
    )

    ERR: Optional[List[_ERR]] = Field(
        default=None,
        title="ERR",
        description="Error",
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

    NTE: Optional[List[_NTE]] = Field(
        default=None,
        title="NTE",
        description="Notes and Comments",
    )

    PID: Optional[_PID] = Field(
        default=None,
        title="PID",
        description="Patient Identification",
    )

    ARV: Optional[List[_ARV]] = Field(
        default=None,
        title="ARV",
        description="Access Restriction",
    )

    ORDER_STATUS: List[_OSU_O51_ORDER_STATUS] = Field(
        min_length=1,
        title="ORDER_STATUS",
    )

    model_config = {"populate_by_name": True}

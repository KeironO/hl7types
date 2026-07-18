"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.2
Class: INU_U05
Type: Message
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import ConfigDict, Field
from hl7types.hl7 import HL7Model

from ..segments.EQU import EQU
from ..segments.INV import INV
from ..segments.MSH import MSH
from ..segments.SFT import SFT
from ..segments.UAC import UAC

_EQU = EQU
_INV = INV
_MSH = MSH
_SFT = SFT
_UAC = UAC


class INU_U05(HL7Model):
    """INU/ACK  - Automated equipment inventory update (S13.3.5).

    Attributes:
        MSH (MSH): Message Header, required
        SFT (Optional[List[SFT]]): Software Segment, optional
        UAC (Optional[UAC]): User Authentication Credential Segment, optional
        EQU (EQU): Equipment Detail, required
        INV (List[INV]): Inventory Detail, required
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

    EQU: _EQU = Field(
        title="EQU",
        description="Equipment Detail",
    )

    INV: List[_INV] = Field(
        min_length=1,
        title="INV",
        description="Inventory Detail",
    )

    model_config = ConfigDict(populate_by_name=True)

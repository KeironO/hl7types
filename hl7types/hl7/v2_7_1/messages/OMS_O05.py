"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7.1
Class: OMS_O05
Type: Message
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import ConfigDict, Field
from hl7types.hl7 import HL7Model

from ..segments.MSH import MSH
from ..segments.NTE import NTE
from ..segments.SFT import SFT
from ..segments.UAC import UAC

from ..groups.OMS_O05_ORDER import OMS_O05_ORDER
from ..groups.OMS_O05_PATIENT import OMS_O05_PATIENT

_MSH = MSH
_NTE = NTE
_OMS_O05_ORDER = OMS_O05_ORDER
_OMS_O05_PATIENT = OMS_O05_PATIENT
_SFT = SFT
_UAC = UAC


class OMS_O05(HL7Model):
    """OMS - Stock requisition order (S4.9.1).

    Attributes:
        MSH (MSH): Message Header, required
        SFT (Optional[List[SFT]]): Software Segment, optional
        UAC (Optional[UAC]): User Authentication Credential Segment, optional
        NTE (Optional[List[NTE]]): Notes and Comments, optional
        PATIENT (Optional[OMS_O05_PATIENT]): optional
        ORDER (List[OMS_O05_ORDER]): required
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

    NTE: Optional[List[_NTE]] = Field(
        default=None,
        title="NTE",
        description="Notes and Comments",
    )

    PATIENT: Optional[_OMS_O05_PATIENT] = Field(
        default=None,
        title="PATIENT",
    )

    ORDER: List[_OMS_O05_ORDER] = Field(
        min_length=1,
        title="ORDER",
    )

    model_config = ConfigDict(populate_by_name=True)

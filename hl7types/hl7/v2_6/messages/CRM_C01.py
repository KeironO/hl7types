"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.6
Class: CRM_C01
Type: Message
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.MSH import MSH
from ..segments.SFT import SFT
from ..segments.UAC import UAC

from ..groups.CRM_C01_PATIENT import CRM_C01_PATIENT

_CRM_C01_PATIENT = CRM_C01_PATIENT
_MSH = MSH
_SFT = SFT
_UAC = UAC


class CRM_C01(HL7Model):
    """CRM - Register a patient on a clinical trial (S7.7.1).

    Attributes:
        MSH (MSH): Message Header, required
        SFT (Optional[List[SFT]]): Software Segment, optional
        UAC (Optional[UAC]): User Authentication Credential Segment, optional
        PATIENT (List[CRM_C01_PATIENT]): required
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

    PATIENT: List[_CRM_C01_PATIENT] = Field(
        min_length=1,
        title="PATIENT",
    )

    model_config = {"populate_by_name": True}

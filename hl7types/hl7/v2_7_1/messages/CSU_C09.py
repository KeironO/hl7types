"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7.1
Class: CSU_C09
Type: Message
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import ConfigDict, Field
from hl7types.hl7 import HL7Model

from ..segments.MSH import MSH
from ..segments.SFT import SFT
from ..segments.UAC import UAC

from ..groups.CSU_C09_PATIENT import CSU_C09_PATIENT

_CSU_C09_PATIENT = CSU_C09_PATIENT
_MSH = MSH
_SFT = SFT
_UAC = UAC


class CSU_C09(HL7Model):
    """CSU - Automated time intervals for reporting, like monthly (S7.7.2).

    Attributes:
        MSH (MSH): Message Header, required
        SFT (Optional[List[SFT]]): Software Segment, optional
        UAC (Optional[UAC]): User Authentication Credential Segment, optional
        PATIENT (List[CSU_C09_PATIENT]): required
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

    PATIENT: List[_CSU_C09_PATIENT] = Field(
        min_length=1,
        title="PATIENT",
    )

    model_config = ConfigDict(populate_by_name=True)

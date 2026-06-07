"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7
Class: CSU_C09
Type: Message
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
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
    """HL7 v2 CSU_C09 message.

    Attributes:
        MSH (MSH): required
        SFT (Optional[List[SFT]]): optional
        UAC (Optional[UAC]): optional
        PATIENT (List[CSU_C09_PATIENT]): required
    """

    MSH: _MSH = Field(
        title="MSH",
        description="Required",
    )

    SFT: Optional[List[_SFT]] = Field(
        default=None,
        title="SFT",
        description="Optional, repeating",
    )

    UAC: Optional[_UAC] = Field(
        default=None,
        title="UAC",
        description="Optional",
    )

    PATIENT: List[_CSU_C09_PATIENT] = Field(
        min_length=1,
        title="PATIENT",
        description="Required, repeating",
    )

    model_config = {"populate_by_name": True}

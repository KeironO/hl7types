"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5.1
Class: ADT_A39
Type: Message
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import ConfigDict, Field
from hl7types.hl7 import HL7Model

from ..segments.EVN import EVN
from ..segments.MSH import MSH
from ..segments.SFT import SFT

from ..groups.ADT_A39_PATIENT import ADT_A39_PATIENT

_ADT_A39_PATIENT = ADT_A39_PATIENT
_EVN = EVN
_MSH = MSH
_SFT = SFT


class ADT_A39(HL7Model):
    """ADT/ACK - Merge person - patient ID (for backward compatibility only) (S3.3.1).

    Attributes:
        MSH (MSH): Message Header, required
        SFT (Optional[List[SFT]]): Software Segment, optional
        EVN (EVN): Event Type, required
        PATIENT (List[ADT_A39_PATIENT]): required
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

    PATIENT: List[_ADT_A39_PATIENT] = Field(
        min_length=1,
        title="PATIENT",
    )

    model_config = ConfigDict(populate_by_name=True)

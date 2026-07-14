"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3
Class: ADT_A39
Type: Message
"""
from __future__ import annotations

from typing import List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.EVN import EVN
from ..segments.MSH import MSH

from ..groups.ADT_A39_PATIENT import ADT_A39_PATIENT

_ADT_A39_PATIENT = ADT_A39_PATIENT
_EVN = EVN
_MSH = MSH


class ADT_A39(HL7Model):
    """ADT/ACK - Merge person - external ID.

    Attributes:
        MSH (MSH): Message header segment, required
        EVN (EVN): Event type, required
        PATIENT (List[ADT_A39_PATIENT]): required
    """

    MSH: _MSH = Field(
        title="MSH",
        description="Message header segment",
    )

    EVN: _EVN = Field(
        title="EVN",
        description="Event type",
    )

    PATIENT: List[_ADT_A39_PATIENT] = Field(
        min_length=1,
        title="PATIENT",
    )

    model_config = {"populate_by_name": True}

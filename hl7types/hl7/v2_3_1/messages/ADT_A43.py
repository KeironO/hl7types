"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3.1
Class: ADT_A43
Type: Message
"""
from __future__ import annotations

from typing import List
from pydantic import ConfigDict, Field
from hl7types.hl7 import HL7Model

from ..segments.EVN import EVN
from ..segments.MSH import MSH

from ..groups.ADT_A43_PATIENT import ADT_A43_PATIENT

_ADT_A43_PATIENT = ADT_A43_PATIENT
_EVN = EVN
_MSH = MSH


class ADT_A43(HL7Model):
    """ADT/ACK - Move patient information - internal ID.

    Attributes:
        MSH (MSH): MSH - message header segment, required
        EVN (EVN): EVN - event type segment, required
        PATIENT (List[ADT_A43_PATIENT]): required
    """

    MSH: _MSH = Field(
        title="MSH",
        description="MSH - message header segment",
    )

    EVN: _EVN = Field(
        title="EVN",
        description="EVN - event type segment",
    )

    PATIENT: List[_ADT_A43_PATIENT] = Field(
        min_length=1,
        title="PATIENT",
    )

    model_config = ConfigDict(populate_by_name=True)

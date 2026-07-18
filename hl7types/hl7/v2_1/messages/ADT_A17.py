"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.1
Class: ADT_A17
Type: Message
"""
from __future__ import annotations

from typing import List
from pydantic import ConfigDict, Field
from hl7types.hl7 import HL7Model

from ..segments.EVN import EVN
from ..segments.MSH import MSH

from ..groups.ADT_A17_PATIENT import ADT_A17_PATIENT

_ADT_A17_PATIENT = ADT_A17_PATIENT
_EVN = EVN
_MSH = MSH


class ADT_A17(HL7Model):
    """HL7 v2 ADT_A17 message.

    Attributes:
        MSH (MSH): MESSAGE HEADER, required
        EVN (EVN): EVENT TYPE, required
        PATIENT (List[ADT_A17_PATIENT]): required
    """

    MSH: _MSH = Field(
        title="MSH",
        description="MESSAGE HEADER",
    )

    EVN: _EVN = Field(
        title="EVN",
        description="EVENT TYPE",
    )

    PATIENT: List[_ADT_A17_PATIENT] = Field(
        min_length=1,
        title="PATIENT",
    )

    model_config = ConfigDict(populate_by_name=True)

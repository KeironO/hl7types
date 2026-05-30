"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3
Class: ADT_A39
Type: Message
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.EVN import EVN
from ..segments.MSH import MSH

from ..groups.ADT_A39_PATIENT import ADT_A39_PATIENT

_ADT_A39_PATIENT = ADT_A39_PATIENT
_EVN = EVN
_MSH = MSH


class ADT_A39(HL7Model):
    """HL7 v2 ADT_A39 message.

    Attributes:
        MSH (MSH): required
        EVN (EVN): required
        PATIENT (List[ADT_A39_PATIENT]): required
    """

    MSH: _MSH = Field(
        default=...,
        title="MSH",
        description="Required",
    )

    EVN: _EVN = Field(
        default=...,
        title="EVN",
        description="Required",
    )

    PATIENT: List[_ADT_A39_PATIENT] = Field(
        default=...,
        title="PATIENT",
        description="Required, repeating",
    )

    model_config = {"populate_by_name": True}

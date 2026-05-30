"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3
Class: BAR_P02
Type: Message
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.EVN import EVN
from ..segments.MSH import MSH

from ..groups.BAR_P02_PATIENT import BAR_P02_PATIENT

_BAR_P02_PATIENT = BAR_P02_PATIENT
_EVN = EVN
_MSH = MSH


class BAR_P02(HL7Model):
    """HL7 v2 BAR_P02 message.

    Attributes:
        MSH (MSH): required
        EVN (EVN): required
        PATIENT (List[BAR_P02_PATIENT]): required
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

    PATIENT: List[_BAR_P02_PATIENT] = Field(
        default=...,
        title="PATIENT",
        description="Required, repeating",
    )

    model_config = {"populate_by_name": True}

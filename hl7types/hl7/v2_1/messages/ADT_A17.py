"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.1
Class: ADT_A17
Type: Message
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..groups.ADT_A17_PATIENT import ADT_A17_PATIENT
from ..segments.EVN import EVN
from ..segments.MSH import MSH

_ADT_A17_PATIENT = ADT_A17_PATIENT
_EVN = EVN
_MSH = MSH


class ADT_A17(BaseModel):
    """HL7 v2 ADT_A17 message.

    Attributes:
        MSH (MSH): required
        EVN (EVN): required
        PATIENT (List[ADT_A17_PATIENT]): required
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

    PATIENT: list[_ADT_A17_PATIENT] = Field(
        default=...,
        title="PATIENT",
        description="Required, repeating",
    )

    model_config = {"populate_by_name": True}

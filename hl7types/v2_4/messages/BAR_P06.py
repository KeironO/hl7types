"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.4
Class: BAR_P06
Type: Message
"""
from _future__ import annotations

from typing import Optional, List
from pydantic import BaseModel, Field

from ..segments.EVN import EVN
from ..segments.MSH import MSH

from ..groups.BAR_P06_PATIENT import BAR_P06_PATIENT

_BAR_P06_PATIENT = BAR_P06_PATIENT
_EVN = EVN
_MSH = MSH


class BAR_P06(BaseModel):
    """HL7 v2 BAR_P06 message.

    Attributes:
        MSH (MSH): required
        EVN (EVN): required
        PATIENT (List[BAR_P06_PATIENT]): required
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

    PATIENT: List[_BAR_P06_PATIENT] = Field(
        default=...,
        title="PATIENT",
        description="Required, repeating",
    )

    model_config = {"populate_by_name": True}

"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5.1
Class: ADT_A45
Type: Message
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..groups.ADT_A45_MERGE_INFO import ADT_A45_MERGE_INFO
from ..segments.EVN import EVN
from ..segments.MSH import MSH
from ..segments.PD1 import PD1
from ..segments.PID import PID
from ..segments.SFT import SFT

_ADT_A45_MERGE_INFO = ADT_A45_MERGE_INFO
_EVN = EVN
_MSH = MSH
_PD1 = PD1
_PID = PID
_SFT = SFT


class ADT_A45(BaseModel):
    """HL7 v2 ADT_A45 message.

    Attributes:
        MSH (MSH): required
        SFT (Optional[List[SFT]]): optional
        EVN (EVN): required
        PID (PID): required
        PD1 (Optional[PD1]): optional
        MERGE_INFO (List[ADT_A45_MERGE_INFO]): required
    """

    MSH: _MSH = Field(
        default=...,
        title="MSH",
        description="Required",
    )

    SFT: list[_SFT] | None = Field(
        default=None,
        title="SFT",
        description="Optional, repeating",
    )

    EVN: _EVN = Field(
        default=...,
        title="EVN",
        description="Required",
    )

    PID: _PID = Field(
        default=...,
        title="PID",
        description="Required",
    )

    PD1: _PD1 | None = Field(
        default=None,
        title="PD1",
        description="Optional",
    )

    MERGE_INFO: list[_ADT_A45_MERGE_INFO] = Field(
        default=...,
        title="MERGE_INFO",
        description="Required, repeating",
    )

    model_config = {"populate_by_name": True}

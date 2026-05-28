"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.2
Class: ADT_A60
Type: Message
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..groups.ADT_A60_ADVERSE_REACTION_GROUP import ADT_A60_ADVERSE_REACTION_GROUP
from ..groups.ADT_A60_VISIT import ADT_A60_VISIT
from ..segments.ARV import ARV
from ..segments.EVN import EVN
from ..segments.MSH import MSH
from ..segments.PID import PID
from ..segments.SFT import SFT
from ..segments.UAC import UAC

_ADT_A60_ADVERSE_REACTION_GROUP = ADT_A60_ADVERSE_REACTION_GROUP
_ADT_A60_VISIT = ADT_A60_VISIT
_ARV = ARV
_EVN = EVN
_MSH = MSH
_PID = PID
_SFT = SFT
_UAC = UAC


class ADT_A60(BaseModel):
    """HL7 v2 ADT_A60 message.

    Attributes:
        MSH (MSH): required
        SFT (Optional[List[SFT]]): optional
        UAC (Optional[UAC]): optional
        EVN (EVN): required
        PID (PID): required
        ARV (Optional[List[ARV]]): optional
        VISIT (Optional[ADT_A60_VISIT]): optional
        ADVERSE_REACTION_GROUP (Optional[List[ADT_A60_ADVERSE_REACTION_GROUP]]): optional
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

    UAC: _UAC | None = Field(
        default=None,
        title="UAC",
        description="Optional",
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

    ARV: list[_ARV] | None = Field(
        default=None,
        title="ARV",
        description="Optional, repeating",
    )

    VISIT: _ADT_A60_VISIT | None = Field(
        default=None,
        title="VISIT",
        description="Optional",
    )

    ADVERSE_REACTION_GROUP: list[_ADT_A60_ADVERSE_REACTION_GROUP] | None = Field(
        default=None,
        title="ADVERSE_REACTION_GROUP",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}

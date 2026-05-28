"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.2
Class: OSM_R26
Type: Message
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..groups.OSM_R26_SHIPMENT import OSM_R26_SHIPMENT
from ..segments.MSH import MSH
from ..segments.SFT import SFT
from ..segments.UAC import UAC

_MSH = MSH
_OSM_R26_SHIPMENT = OSM_R26_SHIPMENT
_SFT = SFT
_UAC = UAC


class OSM_R26(BaseModel):
    """HL7 v2 OSM_R26 message.

    Attributes:
        MSH (MSH): required
        SFT (Optional[List[SFT]]): optional
        UAC (Optional[UAC]): optional
        SHIPMENT (List[OSM_R26_SHIPMENT]): required
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

    SHIPMENT: list[_OSM_R26_SHIPMENT] = Field(
        default=...,
        title="SHIPMENT",
        description="Required, repeating",
    )

    model_config = {"populate_by_name": True}

"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7.1
Class: OSM_R26
Type: Message
"""
from _future__ import annotations

from typing import Optional, List
from pydantic import BaseModel, Field

from ..segments.MSH import MSH
from ..segments.SFT import SFT
from ..segments.UAC import UAC

from ..groups.OSM_R26_SHIPMENT import OSM_R26_SHIPMENT

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

    SFT: Optional[List[_SFT]] = Field(
        default=None,
        title="SFT",
        description="Optional, repeating",
    )

    UAC: Optional[_UAC] = Field(
        default=None,
        title="UAC",
        description="Optional",
    )

    SHIPMENT: List[_OSM_R26_SHIPMENT] = Field(
        default=...,
        title="SHIPMENT",
        description="Required, repeating",
    )

    model_config = {"populate_by_name": True}

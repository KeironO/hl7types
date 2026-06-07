"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7.1
Class: OSM_R26.SHIPMENT
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.PRT import PRT
from ..segments.SHP import SHP

from .OSM_R26_PACKAGE import OSM_R26_PACKAGE
from .OSM_R26_SHIPPING_OBSERVATION import OSM_R26_SHIPPING_OBSERVATION

_OSM_R26_PACKAGE = OSM_R26_PACKAGE
_OSM_R26_SHIPPING_OBSERVATION = OSM_R26_SHIPPING_OBSERVATION
_PRT = PRT
_SHP = SHP


class OSM_R26_SHIPMENT(HL7Model):
    """HL7 v2 OSM_R26.SHIPMENT group.

    Attributes:
        SHP (SHP): required
        PRT (List[PRT]): required
        SHIPPING_OBSERVATION (Optional[List[OSM_R26_SHIPPING_OBSERVATION]]): optional
        PACKAGE (List[OSM_R26_PACKAGE]): required
    """

    SHP: _SHP = Field(
        title="SHP",
        description="Required",
    )

    PRT: List[_PRT] = Field(
        min_length=1,
        title="PRT",
        description="Required, repeating",
    )

    SHIPPING_OBSERVATION: Optional[List[_OSM_R26_SHIPPING_OBSERVATION]] = Field(
        default=None,
        title="SHIPPING_OBSERVATION",
        description="Optional, repeating",
    )

    PACKAGE: List[_OSM_R26_PACKAGE] = Field(
        min_length=1,
        title="PACKAGE",
        description="Required, repeating",
    )

    model_config = {"populate_by_name": True}

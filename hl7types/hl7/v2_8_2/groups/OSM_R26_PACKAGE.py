"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.2
Class: OSM_R26.PACKAGE
Type: Group
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..segments.PAC import PAC
from ..segments.PRT import PRT
from .OSM_R26_SPECIMEN import OSM_R26_SPECIMEN

_OSM_R26_SPECIMEN = OSM_R26_SPECIMEN
_PAC = PAC
_PRT = PRT


class OSM_R26_PACKAGE(BaseModel):
    """HL7 v2 OSM_R26.PACKAGE group.

    Attributes:
        PAC (PAC): required
        PRT (Optional[List[PRT]]): optional
        SPECIMEN (Optional[List[OSM_R26_SPECIMEN]]): optional
    """

    PAC: _PAC = Field(
        default=...,
        title="PAC",
        description="Required",
    )

    PRT: list[_PRT] | None = Field(
        default=None,
        title="PRT",
        description="Optional, repeating",
    )

    SPECIMEN: list[_OSM_R26_SPECIMEN] | None = Field(
        default=None,
        title="SPECIMEN",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}

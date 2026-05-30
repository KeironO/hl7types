"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7.1
Class: OSM_R26.PACKAGE
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.PAC import PAC
from ..segments.PRT import PRT

from .OSM_R26_SPECIMEN import OSM_R26_SPECIMEN

_OSM_R26_SPECIMEN = OSM_R26_SPECIMEN
_PAC = PAC
_PRT = PRT


class OSM_R26_PACKAGE(HL7Model):
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

    PRT: Optional[List[_PRT]] = Field(
        default=None,
        title="PRT",
        description="Optional, repeating",
    )

    SPECIMEN: Optional[List[_OSM_R26_SPECIMEN]] = Field(
        default=None,
        title="SPECIMEN",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}

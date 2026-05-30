"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7
Class: SIU_S12.RESOURCES
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.RGS import RGS

from .SIU_S12_GENERAL_RESOURCE import SIU_S12_GENERAL_RESOURCE
from .SIU_S12_LOCATION_RESOURCE import SIU_S12_LOCATION_RESOURCE
from .SIU_S12_PERSONNEL_RESOURCE import SIU_S12_PERSONNEL_RESOURCE
from .SIU_S12_SERVICE import SIU_S12_SERVICE

_RGS = RGS
_SIU_S12_GENERAL_RESOURCE = SIU_S12_GENERAL_RESOURCE
_SIU_S12_LOCATION_RESOURCE = SIU_S12_LOCATION_RESOURCE
_SIU_S12_PERSONNEL_RESOURCE = SIU_S12_PERSONNEL_RESOURCE
_SIU_S12_SERVICE = SIU_S12_SERVICE


class SIU_S12_RESOURCES(HL7Model):
    """HL7 v2 SIU_S12.RESOURCES group.

    Attributes:
        RGS (RGS): required
        SERVICE (Optional[List[SIU_S12_SERVICE]]): optional
        GENERAL_RESOURCE (Optional[List[SIU_S12_GENERAL_RESOURCE]]): optional
        LOCATION_RESOURCE (Optional[List[SIU_S12_LOCATION_RESOURCE]]): optional
        PERSONNEL_RESOURCE (Optional[List[SIU_S12_PERSONNEL_RESOURCE]]): optional
    """

    RGS: _RGS = Field(
        default=...,
        title="RGS",
        description="Required",
    )

    SERVICE: Optional[List[_SIU_S12_SERVICE]] = Field(
        default=None,
        title="SERVICE",
        description="Optional, repeating",
    )

    GENERAL_RESOURCE: Optional[List[_SIU_S12_GENERAL_RESOURCE]] = Field(
        default=None,
        title="GENERAL_RESOURCE",
        description="Optional, repeating",
    )

    LOCATION_RESOURCE: Optional[List[_SIU_S12_LOCATION_RESOURCE]] = Field(
        default=None,
        title="LOCATION_RESOURCE",
        description="Optional, repeating",
    )

    PERSONNEL_RESOURCE: Optional[List[_SIU_S12_PERSONNEL_RESOURCE]] = Field(
        default=None,
        title="PERSONNEL_RESOURCE",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}

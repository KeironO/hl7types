"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3.1
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
        RGS (RGS): RGS - resource group segment, required
        SERVICE (Optional[List[SIU_S12_SERVICE]]): optional
        GENERAL_RESOURCE (Optional[List[SIU_S12_GENERAL_RESOURCE]]): optional
        LOCATION_RESOURCE (Optional[List[SIU_S12_LOCATION_RESOURCE]]): optional
        PERSONNEL_RESOURCE (Optional[List[SIU_S12_PERSONNEL_RESOURCE]]): optional
    """

    RGS: _RGS = Field(
        title="RGS",
        description="RGS - resource group segment",
    )

    SERVICE: Optional[List[_SIU_S12_SERVICE]] = Field(
        default=None,
        title="SERVICE",
    )

    GENERAL_RESOURCE: Optional[List[_SIU_S12_GENERAL_RESOURCE]] = Field(
        default=None,
        title="GENERAL_RESOURCE",
    )

    LOCATION_RESOURCE: Optional[List[_SIU_S12_LOCATION_RESOURCE]] = Field(
        default=None,
        title="LOCATION_RESOURCE",
    )

    PERSONNEL_RESOURCE: Optional[List[_SIU_S12_PERSONNEL_RESOURCE]] = Field(
        default=None,
        title="PERSONNEL_RESOURCE",
    )

    model_config = {"populate_by_name": True}

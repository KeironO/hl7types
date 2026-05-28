"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8
Class: SRM_S01.RESOURCES
Type: Group
"""
from _future__ import annotations

from typing import Optional, List
from pydantic import BaseModel, Field

from ..segments.RGS import RGS

from .SRM_S01_GENERAL_RESOURCE import SRM_S01_GENERAL_RESOURCE
from .SRM_S01_LOCATION_RESOURCE import SRM_S01_LOCATION_RESOURCE
from .SRM_S01_PERSONNEL_RESOURCE import SRM_S01_PERSONNEL_RESOURCE
from .SRM_S01_SERVICE import SRM_S01_SERVICE

_RGS = RGS
_SRM_S01_GENERAL_RESOURCE = SRM_S01_GENERAL_RESOURCE
_SRM_S01_LOCATION_RESOURCE = SRM_S01_LOCATION_RESOURCE
_SRM_S01_PERSONNEL_RESOURCE = SRM_S01_PERSONNEL_RESOURCE
_SRM_S01_SERVICE = SRM_S01_SERVICE


class SRM_S01_RESOURCES(BaseModel):
    """HL7 v2 SRM_S01.RESOURCES group.

    Attributes:
        RGS (RGS): required
        SERVICE (Optional[List[SRM_S01_SERVICE]]): optional
        GENERAL_RESOURCE (Optional[List[SRM_S01_GENERAL_RESOURCE]]): optional
        LOCATION_RESOURCE (Optional[List[SRM_S01_LOCATION_RESOURCE]]): optional
        PERSONNEL_RESOURCE (Optional[List[SRM_S01_PERSONNEL_RESOURCE]]): optional
    """

    RGS: _RGS = Field(
        default=...,
        title="RGS",
        description="Required",
    )

    SERVICE: Optional[List[_SRM_S01_SERVICE]] = Field(
        default=None,
        title="SERVICE",
        description="Optional, repeating",
    )

    GENERAL_RESOURCE: Optional[List[_SRM_S01_GENERAL_RESOURCE]] = Field(
        default=None,
        title="GENERAL_RESOURCE",
        description="Optional, repeating",
    )

    LOCATION_RESOURCE: Optional[List[_SRM_S01_LOCATION_RESOURCE]] = Field(
        default=None,
        title="LOCATION_RESOURCE",
        description="Optional, repeating",
    )

    PERSONNEL_RESOURCE: Optional[List[_SRM_S01_PERSONNEL_RESOURCE]] = Field(
        default=None,
        title="PERSONNEL_RESOURCE",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}

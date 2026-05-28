"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7
Class: SRR_S01.RESOURCES
Type: Group
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..segments.RGS import RGS
from .SRR_S01_GENERAL_RESOURCE import SRR_S01_GENERAL_RESOURCE
from .SRR_S01_LOCATION_RESOURCE import SRR_S01_LOCATION_RESOURCE
from .SRR_S01_PERSONNEL_RESOURCE import SRR_S01_PERSONNEL_RESOURCE
from .SRR_S01_SERVICE import SRR_S01_SERVICE

_RGS = RGS
_SRR_S01_GENERAL_RESOURCE = SRR_S01_GENERAL_RESOURCE
_SRR_S01_LOCATION_RESOURCE = SRR_S01_LOCATION_RESOURCE
_SRR_S01_PERSONNEL_RESOURCE = SRR_S01_PERSONNEL_RESOURCE
_SRR_S01_SERVICE = SRR_S01_SERVICE


class SRR_S01_RESOURCES(BaseModel):
    """HL7 v2 SRR_S01.RESOURCES group.

    Attributes:
        RGS (RGS): required
        SERVICE (Optional[List[SRR_S01_SERVICE]]): optional
        GENERAL_RESOURCE (Optional[List[SRR_S01_GENERAL_RESOURCE]]): optional
        LOCATION_RESOURCE (Optional[List[SRR_S01_LOCATION_RESOURCE]]): optional
        PERSONNEL_RESOURCE (Optional[List[SRR_S01_PERSONNEL_RESOURCE]]): optional
    """

    RGS: _RGS = Field(
        default=...,
        title="RGS",
        description="Required",
    )

    SERVICE: list[_SRR_S01_SERVICE] | None = Field(
        default=None,
        title="SERVICE",
        description="Optional, repeating",
    )

    GENERAL_RESOURCE: list[_SRR_S01_GENERAL_RESOURCE] | None = Field(
        default=None,
        title="GENERAL_RESOURCE",
        description="Optional, repeating",
    )

    LOCATION_RESOURCE: list[_SRR_S01_LOCATION_RESOURCE] | None = Field(
        default=None,
        title="LOCATION_RESOURCE",
        description="Optional, repeating",
    )

    PERSONNEL_RESOURCE: list[_SRR_S01_PERSONNEL_RESOURCE] | None = Field(
        default=None,
        title="PERSONNEL_RESOURCE",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}

"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.6
Class: SQR_S25.RESOURCES
Type: Group
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..segments.RGS import RGS
from .SQR_S25_GENERAL_RESOURCE import SQR_S25_GENERAL_RESOURCE
from .SQR_S25_LOCATION_RESOURCE import SQR_S25_LOCATION_RESOURCE
from .SQR_S25_PERSONNEL_RESOURCE import SQR_S25_PERSONNEL_RESOURCE
from .SQR_S25_SERVICE import SQR_S25_SERVICE

_RGS = RGS
_SQR_S25_GENERAL_RESOURCE = SQR_S25_GENERAL_RESOURCE
_SQR_S25_LOCATION_RESOURCE = SQR_S25_LOCATION_RESOURCE
_SQR_S25_PERSONNEL_RESOURCE = SQR_S25_PERSONNEL_RESOURCE
_SQR_S25_SERVICE = SQR_S25_SERVICE


class SQR_S25_RESOURCES(BaseModel):
    """HL7 v2 SQR_S25.RESOURCES group.

    Attributes:
        RGS (RGS): required
        SERVICE (Optional[List[SQR_S25_SERVICE]]): optional
        GENERAL_RESOURCE (Optional[List[SQR_S25_GENERAL_RESOURCE]]): optional
        PERSONNEL_RESOURCE (Optional[List[SQR_S25_PERSONNEL_RESOURCE]]): optional
        LOCATION_RESOURCE (Optional[List[SQR_S25_LOCATION_RESOURCE]]): optional
    """

    RGS: _RGS = Field(
        default=...,
        title="RGS",
        description="Required",
    )

    SERVICE: list[_SQR_S25_SERVICE] | None = Field(
        default=None,
        title="SERVICE",
        description="Optional, repeating",
    )

    GENERAL_RESOURCE: list[_SQR_S25_GENERAL_RESOURCE] | None = Field(
        default=None,
        title="GENERAL_RESOURCE",
        description="Optional, repeating",
    )

    PERSONNEL_RESOURCE: list[_SQR_S25_PERSONNEL_RESOURCE] | None = Field(
        default=None,
        title="PERSONNEL_RESOURCE",
        description="Optional, repeating",
    )

    LOCATION_RESOURCE: list[_SQR_S25_LOCATION_RESOURCE] | None = Field(
        default=None,
        title="LOCATION_RESOURCE",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}

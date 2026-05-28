"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5
Class: SQM_S25.RESOURCES
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import BaseModel, Field

from ..segments.RGS import RGS

from .SQM_S25_GENERAL_RESOURCE import SQM_S25_GENERAL_RESOURCE
from .SQM_S25_LOCATION_RESOURCE import SQM_S25_LOCATION_RESOURCE
from .SQM_S25_PERSONNEL_RESOURCE import SQM_S25_PERSONNEL_RESOURCE
from .SQM_S25_SERVICE import SQM_S25_SERVICE

_RGS = RGS
_SQM_S25_GENERAL_RESOURCE = SQM_S25_GENERAL_RESOURCE
_SQM_S25_LOCATION_RESOURCE = SQM_S25_LOCATION_RESOURCE
_SQM_S25_PERSONNEL_RESOURCE = SQM_S25_PERSONNEL_RESOURCE
_SQM_S25_SERVICE = SQM_S25_SERVICE


class SQM_S25_RESOURCES(BaseModel):
    """HL7 v2 SQM_S25.RESOURCES group.

    Attributes:
        RGS (RGS): required
        SERVICE (Optional[List[SQM_S25_SERVICE]]): optional
        GENERAL_RESOURCE (Optional[List[SQM_S25_GENERAL_RESOURCE]]): optional
        PERSONNEL_RESOURCE (Optional[List[SQM_S25_PERSONNEL_RESOURCE]]): optional
        LOCATION_RESOURCE (Optional[List[SQM_S25_LOCATION_RESOURCE]]): optional
    """

    RGS: _RGS = Field(
        default=...,
        title="RGS",
        description="Required",
    )

    SERVICE: Optional[List[_SQM_S25_SERVICE]] = Field(
        default=None,
        title="SERVICE",
        description="Optional, repeating",
    )

    GENERAL_RESOURCE: Optional[List[_SQM_S25_GENERAL_RESOURCE]] = Field(
        default=None,
        title="GENERAL_RESOURCE",
        description="Optional, repeating",
    )

    PERSONNEL_RESOURCE: Optional[List[_SQM_S25_PERSONNEL_RESOURCE]] = Field(
        default=None,
        title="PERSONNEL_RESOURCE",
        description="Optional, repeating",
    )

    LOCATION_RESOURCE: Optional[List[_SQM_S25_LOCATION_RESOURCE]] = Field(
        default=None,
        title="LOCATION_RESOURCE",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}

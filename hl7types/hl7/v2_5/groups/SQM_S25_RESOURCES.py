"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5
Class: SQM_S25.RESOURCES
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import ConfigDict, Field
from hl7types.hl7 import HL7Model

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


class SQM_S25_RESOURCES(HL7Model):
    """HL7 v2 SQM_S25.RESOURCES group.

    Attributes:
        RGS (RGS): Resource Group, required
        SERVICE (Optional[List[SQM_S25_SERVICE]]): optional
        GENERAL_RESOURCE (Optional[List[SQM_S25_GENERAL_RESOURCE]]): optional
        PERSONNEL_RESOURCE (Optional[List[SQM_S25_PERSONNEL_RESOURCE]]): optional
        LOCATION_RESOURCE (Optional[List[SQM_S25_LOCATION_RESOURCE]]): optional
    """

    RGS: _RGS = Field(
        title="RGS",
        description="Resource Group",
    )

    SERVICE: Optional[List[_SQM_S25_SERVICE]] = Field(
        default=None,
        title="SERVICE",
    )

    GENERAL_RESOURCE: Optional[List[_SQM_S25_GENERAL_RESOURCE]] = Field(
        default=None,
        title="GENERAL_RESOURCE",
    )

    PERSONNEL_RESOURCE: Optional[List[_SQM_S25_PERSONNEL_RESOURCE]] = Field(
        default=None,
        title="PERSONNEL_RESOURCE",
    )

    LOCATION_RESOURCE: Optional[List[_SQM_S25_LOCATION_RESOURCE]] = Field(
        default=None,
        title="LOCATION_RESOURCE",
    )

    model_config = ConfigDict(populate_by_name=True)

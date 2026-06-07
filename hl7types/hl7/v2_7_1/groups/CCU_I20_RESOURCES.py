"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7.1
Class: CCU_I20.RESOURCES
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.RGS import RGS

from .CCU_I20_RESOURCE_DETAIL import CCU_I20_RESOURCE_DETAIL

_CCU_I20_RESOURCE_DETAIL = CCU_I20_RESOURCE_DETAIL
_RGS = RGS


class CCU_I20_RESOURCES(HL7Model):
    """HL7 v2 CCU_I20.RESOURCES group.

    Attributes:
        RGS (RGS): required
        RESOURCE_DETAIL (Optional[List[CCU_I20_RESOURCE_DETAIL]]): optional
    """

    RGS: _RGS = Field(
        title="RGS",
        description="Required",
    )

    RESOURCE_DETAIL: Optional[List[_CCU_I20_RESOURCE_DETAIL]] = Field(
        default=None,
        title="RESOURCE_DETAIL",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}

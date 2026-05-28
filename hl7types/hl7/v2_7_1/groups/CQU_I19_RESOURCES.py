"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7.1
Class: CQU_I19.RESOURCES
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import BaseModel, Field

from ..segments.RGS import RGS

from .CQU_I19_RESOURCE_DETAIL import CQU_I19_RESOURCE_DETAIL

_CQU_I19_RESOURCE_DETAIL = CQU_I19_RESOURCE_DETAIL
_RGS = RGS


class CQU_I19_RESOURCES(BaseModel):
    """HL7 v2 CQU_I19.RESOURCES group.

    Attributes:
        RGS (RGS): required
        RESOURCE_DETAIL (Optional[List[CQU_I19_RESOURCE_DETAIL]]): optional
    """

    RGS: _RGS = Field(
        default=...,
        title="RGS",
        description="Required",
    )

    RESOURCE_DETAIL: Optional[List[_CQU_I19_RESOURCE_DETAIL]] = Field(
        default=None,
        title="RESOURCE_DETAIL",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}

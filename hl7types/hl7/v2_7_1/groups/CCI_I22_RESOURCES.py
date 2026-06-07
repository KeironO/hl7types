"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7.1
Class: CCI_I22.RESOURCES
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.RGS import RGS

from .CCI_I22_RESOURCE_DETAIL import CCI_I22_RESOURCE_DETAIL

_CCI_I22_RESOURCE_DETAIL = CCI_I22_RESOURCE_DETAIL
_RGS = RGS


class CCI_I22_RESOURCES(HL7Model):
    """HL7 v2 CCI_I22.RESOURCES group.

    Attributes:
        RGS (RGS): required
        RESOURCE_DETAIL (Optional[List[CCI_I22_RESOURCE_DETAIL]]): optional
    """

    RGS: _RGS = Field(
        title="RGS",
        description="Required",
    )

    RESOURCE_DETAIL: Optional[List[_CCI_I22_RESOURCE_DETAIL]] = Field(
        default=None,
        title="RESOURCE_DETAIL",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}

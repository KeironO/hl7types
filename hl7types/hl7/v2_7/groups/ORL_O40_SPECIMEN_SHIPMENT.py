"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7
Class: ORL_O40.SPECIMEN_SHIPMENT
Type: Group
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..segments.SHP import SHP
from .ORL_O40_PACKAGE import ORL_O40_PACKAGE

_ORL_O40_PACKAGE = ORL_O40_PACKAGE
_SHP = SHP


class ORL_O40_SPECIMEN_SHIPMENT(BaseModel):
    """HL7 v2 ORL_O40.SPECIMEN_SHIPMENT group.

    Attributes:
        SHP (SHP): required
        PACKAGE (List[ORL_O40_PACKAGE]): required
    """

    SHP: _SHP = Field(
        default=...,
        title="SHP",
        description="Required",
    )

    PACKAGE: list[_ORL_O40_PACKAGE] = Field(
        default=...,
        title="PACKAGE",
        description="Required, repeating",
    )

    model_config = {"populate_by_name": True}

"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.2
Class: OML_O39.PACKAGE
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import BaseModel, Field

from ..segments.PAC import PAC

from .OML_O39_SPECIMEN_IN_PACKAGE import OML_O39_SPECIMEN_IN_PACKAGE

_OML_O39_SPECIMEN_IN_PACKAGE = OML_O39_SPECIMEN_IN_PACKAGE
_PAC = PAC


class OML_O39_PACKAGE(BaseModel):
    """HL7 v2 OML_O39.PACKAGE group.

    Attributes:
        PAC (PAC): required
        SPECIMEN_IN_PACKAGE (Optional[List[OML_O39_SPECIMEN_IN_PACKAGE]]): optional
    """

    PAC: _PAC = Field(
        default=...,
        title="PAC",
        description="Required",
    )

    SPECIMEN_IN_PACKAGE: Optional[List[_OML_O39_SPECIMEN_IN_PACKAGE]] = Field(
        default=None,
        title="SPECIMEN_IN_PACKAGE",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}

"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.2
Class: ORL_O44.PACKAGE
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import BaseModel, Field

from ..segments.PAC import PAC

from .ORL_O44_SPECIMEN_IN_PACKAGE import ORL_O44_SPECIMEN_IN_PACKAGE

_ORL_O44_SPECIMEN_IN_PACKAGE = ORL_O44_SPECIMEN_IN_PACKAGE
_PAC = PAC


class ORL_O44_PACKAGE(BaseModel):
    """HL7 v2 ORL_O44.PACKAGE group.

    Attributes:
        PAC (PAC): required
        SPECIMEN_IN_PACKAGE (Optional[List[ORL_O44_SPECIMEN_IN_PACKAGE]]): optional
    """

    PAC: _PAC = Field(
        default=...,
        title="PAC",
        description="Required",
    )

    SPECIMEN_IN_PACKAGE: Optional[List[_ORL_O44_SPECIMEN_IN_PACKAGE]] = Field(
        default=None,
        title="SPECIMEN_IN_PACKAGE",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}

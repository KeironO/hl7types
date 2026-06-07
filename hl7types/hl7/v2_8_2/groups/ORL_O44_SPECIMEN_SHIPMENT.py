"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.2
Class: ORL_O44.SPECIMEN_SHIPMENT
Type: Group
"""
from __future__ import annotations

from typing import List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.SHP import SHP

from .ORL_O44_PACKAGE import ORL_O44_PACKAGE

_ORL_O44_PACKAGE = ORL_O44_PACKAGE
_SHP = SHP


class ORL_O44_SPECIMEN_SHIPMENT(HL7Model):
    """HL7 v2 ORL_O44.SPECIMEN_SHIPMENT group.

    Attributes:
        SHP (SHP): required
        PACKAGE (List[ORL_O44_PACKAGE]): required
    """

    SHP: _SHP = Field(
        title="SHP",
        description="Required",
    )

    PACKAGE: List[_ORL_O44_PACKAGE] = Field(
        min_length=1,
        title="PACKAGE",
        description="Required, repeating",
    )

    model_config = {"populate_by_name": True}

"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8
Class: OML_O39.SPECIMEN_SHIPMENT
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.SHP import SHP

from .OML_O39_PACKAGE import OML_O39_PACKAGE
from .OML_O39_SHIPMENT_OBSERVATION import OML_O39_SHIPMENT_OBSERVATION

_OML_O39_PACKAGE = OML_O39_PACKAGE
_OML_O39_SHIPMENT_OBSERVATION = OML_O39_SHIPMENT_OBSERVATION
_SHP = SHP


class OML_O39_SPECIMEN_SHIPMENT(HL7Model):
    """HL7 v2 OML_O39.SPECIMEN_SHIPMENT group.

    Attributes:
        SHP (SHP): required
        SHIPMENT_OBSERVATION (Optional[List[OML_O39_SHIPMENT_OBSERVATION]]): optional
        PACKAGE (List[OML_O39_PACKAGE]): required
    """

    SHP: _SHP = Field(
        title="SHP",
        description="Required",
    )

    SHIPMENT_OBSERVATION: Optional[List[_OML_O39_SHIPMENT_OBSERVATION]] = Field(
        default=None,
        title="SHIPMENT_OBSERVATION",
        description="Optional, repeating",
    )

    PACKAGE: List[_OML_O39_PACKAGE] = Field(
        min_length=1,
        title="PACKAGE",
        description="Required, repeating",
    )

    model_config = {"populate_by_name": True}

"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7
Class: ORL_O40.SPECIMEN_CONTAINER_IN_PACKAGE
Type: Group
"""
from __future__ import annotations

from pydantic import ConfigDict, Field
from hl7types.hl7 import HL7Model

from ..segments.SAC import SAC

_SAC = SAC


class ORL_O40_SPECIMEN_CONTAINER_IN_PACKAGE(HL7Model):
    """HL7 v2 ORL_O40.SPECIMEN_CONTAINER_IN_PACKAGE group.

    Attributes:
        SAC (SAC): Specimen Container detail, required
    """

    SAC: _SAC = Field(
        title="SAC",
        description="Specimen Container detail",
    )

    model_config = ConfigDict(populate_by_name=True)

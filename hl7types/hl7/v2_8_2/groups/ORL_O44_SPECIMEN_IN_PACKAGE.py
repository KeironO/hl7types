"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.2
Class: ORL_O44.SPECIMEN_IN_PACKAGE
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import ConfigDict, Field
from hl7types.hl7 import HL7Model

from ..segments.SPM import SPM

from .ORL_O44_SPECIMEN_CONTAINER_IN_PACKAGE import ORL_O44_SPECIMEN_CONTAINER_IN_PACKAGE

_ORL_O44_SPECIMEN_CONTAINER_IN_PACKAGE = ORL_O44_SPECIMEN_CONTAINER_IN_PACKAGE
_SPM = SPM


class ORL_O44_SPECIMEN_IN_PACKAGE(HL7Model):
    """HL7 v2 ORL_O44.SPECIMEN_IN_PACKAGE group.

    Attributes:
        SPM (SPM): Specimen, required
        SPECIMEN_CONTAINER_IN_PACKAGE (Optional[List[ORL_O44_SPECIMEN_CONTAINER_IN_PACKAGE]]): optional
    """

    SPM: _SPM = Field(
        title="SPM",
        description="Specimen",
    )

    SPECIMEN_CONTAINER_IN_PACKAGE: Optional[List[_ORL_O44_SPECIMEN_CONTAINER_IN_PACKAGE]] = Field(
        default=None,
        title="SPECIMEN_CONTAINER_IN_PACKAGE",
    )

    model_config = ConfigDict(populate_by_name=True)

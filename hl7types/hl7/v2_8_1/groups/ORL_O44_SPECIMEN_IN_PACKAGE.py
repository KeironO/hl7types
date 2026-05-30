"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.1
Class: ORL_O44.SPECIMEN_IN_PACKAGE
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.SPM import SPM

from .ORL_O44_SPECIMEN_CONTAINER_IN_PACKAGE import ORL_O44_SPECIMEN_CONTAINER_IN_PACKAGE

_ORL_O44_SPECIMEN_CONTAINER_IN_PACKAGE = ORL_O44_SPECIMEN_CONTAINER_IN_PACKAGE
_SPM = SPM


class ORL_O44_SPECIMEN_IN_PACKAGE(HL7Model):
    """HL7 v2 ORL_O44.SPECIMEN_IN_PACKAGE group.

    Attributes:
        SPM (SPM): required
        SPECIMEN_CONTAINER_IN_PACKAGE (Optional[List[ORL_O44_SPECIMEN_CONTAINER_IN_PACKAGE]]): optional
    """

    SPM: _SPM = Field(
        default=...,
        title="SPM",
        description="Required",
    )

    SPECIMEN_CONTAINER_IN_PACKAGE: Optional[List[_ORL_O44_SPECIMEN_CONTAINER_IN_PACKAGE]] = Field(
        default=None,
        title="SPECIMEN_CONTAINER_IN_PACKAGE",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}

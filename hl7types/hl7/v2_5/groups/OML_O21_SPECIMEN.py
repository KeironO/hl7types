"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5
Class: OML_O21.SPECIMEN
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.OBX import OBX
from ..segments.SPM import SPM

from .OML_O21_CONTAINER import OML_O21_CONTAINER

_OBX = OBX
_OML_O21_CONTAINER = OML_O21_CONTAINER
_SPM = SPM


class OML_O21_SPECIMEN(HL7Model):
    """HL7 v2 OML_O21.SPECIMEN group.

    Attributes:
        SPM (SPM): required
        OBX (Optional[List[OBX]]): optional
        CONTAINER (Optional[List[OML_O21_CONTAINER]]): optional
    """

    SPM: _SPM = Field(
        default=...,
        title="SPM",
        description="Required",
    )

    OBX: Optional[List[_OBX]] = Field(
        default=None,
        title="OBX",
        description="Optional, repeating",
    )

    CONTAINER: Optional[List[_OML_O21_CONTAINER]] = Field(
        default=None,
        title="CONTAINER",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}

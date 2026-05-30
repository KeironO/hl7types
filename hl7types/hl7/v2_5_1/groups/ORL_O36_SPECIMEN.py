"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5.1
Class: ORL_O36.SPECIMEN
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.OBX import OBX
from ..segments.SPM import SPM

from .ORL_O36_SPECIMEN_CONTAINER import ORL_O36_SPECIMEN_CONTAINER

_OBX = OBX
_ORL_O36_SPECIMEN_CONTAINER = ORL_O36_SPECIMEN_CONTAINER
_SPM = SPM


class ORL_O36_SPECIMEN(HL7Model):
    """HL7 v2 ORL_O36.SPECIMEN group.

    Attributes:
        SPM (SPM): required
        OBX (Optional[List[OBX]]): optional
        SPECIMEN_CONTAINER (List[ORL_O36_SPECIMEN_CONTAINER]): required
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

    SPECIMEN_CONTAINER: List[_ORL_O36_SPECIMEN_CONTAINER] = Field(
        default=...,
        title="SPECIMEN_CONTAINER",
        description="Required, repeating",
    )

    model_config = {"populate_by_name": True}

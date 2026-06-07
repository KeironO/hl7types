"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5.1
Class: OMG_O19.SPECIMEN
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.OBX import OBX
from ..segments.SPM import SPM

from .OMG_O19_CONTAINER import OMG_O19_CONTAINER

_OBX = OBX
_OMG_O19_CONTAINER = OMG_O19_CONTAINER
_SPM = SPM


class OMG_O19_SPECIMEN(HL7Model):
    """HL7 v2 OMG_O19.SPECIMEN group.

    Attributes:
        SPM (SPM): required
        OBX (Optional[List[OBX]]): optional
        CONTAINER (Optional[List[OMG_O19_CONTAINER]]): optional
    """

    SPM: _SPM = Field(
        title="SPM",
        description="Required",
    )

    OBX: Optional[List[_OBX]] = Field(
        default=None,
        title="OBX",
        description="Optional, repeating",
    )

    CONTAINER: Optional[List[_OMG_O19_CONTAINER]] = Field(
        default=None,
        title="CONTAINER",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}

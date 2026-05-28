"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.6
Class: ORL_O36.SPECIMEN
Type: Group
"""
from _future__ import annotations

from typing import Optional, List
from pydantic import BaseModel, Field

from ..segments.NTE import NTE
from ..segments.OBX import OBX
from ..segments.SPM import SPM

from .ORL_O36_SPECIMEN_CONTAINER import ORL_O36_SPECIMEN_CONTAINER

_NTE = NTE
_OBX = OBX
_ORL_O36_SPECIMEN_CONTAINER = ORL_O36_SPECIMEN_CONTAINER
_SPM = SPM


class ORL_O36_SPECIMEN(BaseModel):
    """HL7 v2 ORL_O36.SPECIMEN group.

    Attributes:
        SPM (SPM): required
        OBX (Optional[List[OBX]]): optional
        NTE (Optional[List[NTE]]): optional
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

    NTE: Optional[List[_NTE]] = Field(
        default=None,
        title="NTE",
        description="Optional, repeating",
    )

    SPECIMEN_CONTAINER: List[_ORL_O36_SPECIMEN_CONTAINER] = Field(
        default=...,
        title="SPECIMEN_CONTAINER",
        description="Required, repeating",
    )

    model_config = {"populate_by_name": True}

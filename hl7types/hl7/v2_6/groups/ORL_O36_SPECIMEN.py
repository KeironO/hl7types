"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.6
Class: ORL_O36.SPECIMEN
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.NTE import NTE
from ..segments.OBX import OBX
from ..segments.SPM import SPM

from .ORL_O36_SPECIMEN_CONTAINER import ORL_O36_SPECIMEN_CONTAINER

_NTE = NTE
_OBX = OBX
_ORL_O36_SPECIMEN_CONTAINER = ORL_O36_SPECIMEN_CONTAINER
_SPM = SPM


class ORL_O36_SPECIMEN(HL7Model):
    """HL7 v2 ORL_O36.SPECIMEN group.

    Attributes:
        SPM (SPM): Specimen, required
        OBX (Optional[List[OBX]]): Observation/Result, optional
        NTE (Optional[List[NTE]]): Notes and Comments, optional
        SPECIMEN_CONTAINER (List[ORL_O36_SPECIMEN_CONTAINER]): required
    """

    SPM: _SPM = Field(
        title="SPM",
        description="Specimen",
    )

    OBX: Optional[List[_OBX]] = Field(
        default=None,
        title="OBX",
        description="Observation/Result",
    )

    NTE: Optional[List[_NTE]] = Field(
        default=None,
        title="NTE",
        description="Notes and Comments",
    )

    SPECIMEN_CONTAINER: List[_ORL_O36_SPECIMEN_CONTAINER] = Field(
        min_length=1,
        title="SPECIMEN_CONTAINER",
    )

    model_config = {"populate_by_name": True}

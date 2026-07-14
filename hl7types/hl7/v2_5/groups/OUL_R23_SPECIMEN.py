"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5
Class: OUL_R23.SPECIMEN
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.OBX import OBX
from ..segments.SPM import SPM

from .OUL_R23_CONTAINER import OUL_R23_CONTAINER

_OBX = OBX
_OUL_R23_CONTAINER = OUL_R23_CONTAINER
_SPM = SPM


class OUL_R23_SPECIMEN(HL7Model):
    """HL7 v2 OUL_R23.SPECIMEN group.

    Attributes:
        SPM (SPM): Specimen, required
        OBX (Optional[List[OBX]]): Observation/Result, optional
        CONTAINER (List[OUL_R23_CONTAINER]): required
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

    CONTAINER: List[_OUL_R23_CONTAINER] = Field(
        min_length=1,
        title="CONTAINER",
    )

    model_config = {"populate_by_name": True}

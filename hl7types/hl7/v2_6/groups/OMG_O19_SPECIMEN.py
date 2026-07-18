"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.6
Class: OMG_O19.SPECIMEN
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import ConfigDict, Field
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
        SPM (SPM): Specimen, required
        OBX (Optional[List[OBX]]): Observation/Result, optional
        CONTAINER (Optional[List[OMG_O19_CONTAINER]]): optional
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

    CONTAINER: Optional[List[_OMG_O19_CONTAINER]] = Field(
        default=None,
        title="CONTAINER",
    )

    model_config = ConfigDict(populate_by_name=True)

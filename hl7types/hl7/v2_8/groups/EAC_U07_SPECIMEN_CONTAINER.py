"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8
Class: EAC_U07.SPECIMEN_CONTAINER
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.OBR import OBR
from ..segments.SAC import SAC
from ..segments.SPM import SPM

_OBR = OBR
_SAC = SAC
_SPM = SPM


class EAC_U07_SPECIMEN_CONTAINER(HL7Model):
    """HL7 v2 EAC_U07.SPECIMEN_CONTAINER group.

    Attributes:
        SAC (SAC): Specimen Container detail, required
        OBR (Optional[List[OBR]]): Observation Request, optional
        SPM (Optional[List[SPM]]): Specimen, optional
    """

    SAC: _SAC = Field(
        title="SAC",
        description="Specimen Container detail",
    )

    OBR: Optional[List[_OBR]] = Field(
        default=None,
        title="OBR",
        description="Observation Request",
    )

    SPM: Optional[List[_SPM]] = Field(
        default=None,
        title="SPM",
        description="Specimen",
    )

    model_config = {"populate_by_name": True}

"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.1
Class: SSU_U03.SPECIMEN_CONTAINER
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.NTE import NTE
from ..segments.OBX import OBX
from ..segments.SAC import SAC

from .SSU_U03_SPECIMEN import SSU_U03_SPECIMEN

_NTE = NTE
_OBX = OBX
_SAC = SAC
_SSU_U03_SPECIMEN = SSU_U03_SPECIMEN


class SSU_U03_SPECIMEN_CONTAINER(HL7Model):
    """HL7 v2 SSU_U03.SPECIMEN_CONTAINER group.

    Attributes:
        SAC (SAC): required
        OBX (Optional[List[OBX]]): optional
        NTE (Optional[List[NTE]]): optional
        SPECIMEN (Optional[List[SSU_U03_SPECIMEN]]): optional
    """

    SAC: _SAC = Field(
        default=...,
        title="SAC",
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

    SPECIMEN: Optional[List[_SSU_U03_SPECIMEN]] = Field(
        default=None,
        title="SPECIMEN",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}

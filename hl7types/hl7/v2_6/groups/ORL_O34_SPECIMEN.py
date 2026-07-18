"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.6
Class: ORL_O34.SPECIMEN
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import ConfigDict, Field
from hl7types.hl7 import HL7Model

from ..segments.OBX import OBX
from ..segments.SAC import SAC
from ..segments.SPM import SPM

from .ORL_O34_ORDER import ORL_O34_ORDER

_OBX = OBX
_ORL_O34_ORDER = ORL_O34_ORDER
_SAC = SAC
_SPM = SPM


class ORL_O34_SPECIMEN(HL7Model):
    """HL7 v2 ORL_O34.SPECIMEN group.

    Attributes:
        SPM (SPM): Specimen, required
        OBX (Optional[List[OBX]]): Observation/Result, optional
        SAC (Optional[List[SAC]]): Specimen Container detail, optional
        ORDER (Optional[List[ORL_O34_ORDER]]): optional
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

    SAC: Optional[List[_SAC]] = Field(
        default=None,
        title="SAC",
        description="Specimen Container detail",
    )

    ORDER: Optional[List[_ORL_O34_ORDER]] = Field(
        default=None,
        title="ORDER",
    )

    model_config = ConfigDict(populate_by_name=True)

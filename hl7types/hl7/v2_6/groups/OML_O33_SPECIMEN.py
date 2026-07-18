"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.6
Class: OML_O33.SPECIMEN
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import ConfigDict, Field
from hl7types.hl7 import HL7Model

from ..segments.OBX import OBX
from ..segments.SAC import SAC
from ..segments.SPM import SPM

from .OML_O33_ORDER import OML_O33_ORDER

_OBX = OBX
_OML_O33_ORDER = OML_O33_ORDER
_SAC = SAC
_SPM = SPM


class OML_O33_SPECIMEN(HL7Model):
    """HL7 v2 OML_O33.SPECIMEN group.

    Attributes:
        SPM (SPM): Specimen, required
        OBX (Optional[List[OBX]]): Observation/Result, optional
        SAC (Optional[List[SAC]]): Specimen Container detail, optional
        ORDER (List[OML_O33_ORDER]): required
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

    ORDER: List[_OML_O33_ORDER] = Field(
        min_length=1,
        title="ORDER",
    )

    model_config = ConfigDict(populate_by_name=True)

"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5
Class: OUL_R22.SPECIMEN
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import ConfigDict, Field
from hl7types.hl7 import HL7Model

from ..segments.OBX import OBX
from ..segments.SPM import SPM

from .OUL_R22_CONTAINER import OUL_R22_CONTAINER
from .OUL_R22_ORDER import OUL_R22_ORDER

_OBX = OBX
_OUL_R22_CONTAINER = OUL_R22_CONTAINER
_OUL_R22_ORDER = OUL_R22_ORDER
_SPM = SPM


class OUL_R22_SPECIMEN(HL7Model):
    """HL7 v2 OUL_R22.SPECIMEN group.

    Attributes:
        SPM (SPM): Specimen, required
        OBX (Optional[List[OBX]]): Observation/Result, optional
        CONTAINER (Optional[List[OUL_R22_CONTAINER]]): optional
        ORDER (List[OUL_R22_ORDER]): required
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

    CONTAINER: Optional[List[_OUL_R22_CONTAINER]] = Field(
        default=None,
        title="CONTAINER",
    )

    ORDER: List[_OUL_R22_ORDER] = Field(
        min_length=1,
        title="ORDER",
    )

    model_config = ConfigDict(populate_by_name=True)

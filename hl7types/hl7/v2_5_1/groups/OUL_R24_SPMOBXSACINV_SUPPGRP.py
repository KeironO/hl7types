"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5.1
Class: OUL_R24.SPMOBXSACINV_SUPPGRP
Type: Group
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..segments.OBX import OBX
from ..segments.SPM import SPM
from .OUL_R24_CONTAINER import OUL_R24_CONTAINER

_OBX = OBX
_OUL_R24_CONTAINER = OUL_R24_CONTAINER
_SPM = SPM


class OUL_R24_SPMOBXSACINV_SUPPGRP(BaseModel):
    """HL7 v2 OUL_R24.SPMOBXSACINV_SUPPGRP group.

    Attributes:
        SPM (SPM): required
        OBX (Optional[List[OBX]]): optional
        CONTAINER (Optional[List[OUL_R24_CONTAINER]]): optional
    """

    SPM: _SPM = Field(
        default=...,
        title="SPM",
        description="Required",
    )

    OBX: list[_OBX] | None = Field(
        default=None,
        title="OBX",
        description="Optional, repeating",
    )

    CONTAINER: list[_OUL_R24_CONTAINER] | None = Field(
        default=None,
        title="CONTAINER",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}

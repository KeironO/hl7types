"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5
Class: OUL_R22.SPECIMEN
Type: Group
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..segments.OBX import OBX
from ..segments.SPM import SPM
from .OUL_R22_CONTAINER import OUL_R22_CONTAINER
from .OUL_R22_ORDER import OUL_R22_ORDER

_OBX = OBX
_OUL_R22_CONTAINER = OUL_R22_CONTAINER
_OUL_R22_ORDER = OUL_R22_ORDER
_SPM = SPM


class OUL_R22_SPECIMEN(BaseModel):
    """HL7 v2 OUL_R22.SPECIMEN group.

    Attributes:
        SPM (SPM): required
        OBX (Optional[List[OBX]]): optional
        CONTAINER (Optional[List[OUL_R22_CONTAINER]]): optional
        ORDER (List[OUL_R22_ORDER]): required
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

    CONTAINER: list[_OUL_R22_CONTAINER] | None = Field(
        default=None,
        title="CONTAINER",
        description="Optional, repeating",
    )

    ORDER: list[_OUL_R22_ORDER] = Field(
        default=...,
        title="ORDER",
        description="Required, repeating",
    )

    model_config = {"populate_by_name": True}

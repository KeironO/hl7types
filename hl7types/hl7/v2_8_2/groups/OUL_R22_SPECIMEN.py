"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.2
Class: OUL_R22.SPECIMEN
Type: Group
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..segments.SPM import SPM
from .OUL_R22_CONTAINER import OUL_R22_CONTAINER
from .OUL_R22_ORDER import OUL_R22_ORDER
from .OUL_R22_SPECIMEN_OBSERVATION import OUL_R22_SPECIMEN_OBSERVATION

_OUL_R22_CONTAINER = OUL_R22_CONTAINER
_OUL_R22_ORDER = OUL_R22_ORDER
_OUL_R22_SPECIMEN_OBSERVATION = OUL_R22_SPECIMEN_OBSERVATION
_SPM = SPM


class OUL_R22_SPECIMEN(BaseModel):
    """HL7 v2 OUL_R22.SPECIMEN group.

    Attributes:
        SPM (SPM): required
        SPECIMEN_OBSERVATION (Optional[List[OUL_R22_SPECIMEN_OBSERVATION]]): optional
        CONTAINER (Optional[List[OUL_R22_CONTAINER]]): optional
        ORDER (List[OUL_R22_ORDER]): required
    """

    SPM: _SPM = Field(
        default=...,
        title="SPM",
        description="Required",
    )

    SPECIMEN_OBSERVATION: list[_OUL_R22_SPECIMEN_OBSERVATION] | None = Field(
        default=None,
        title="SPECIMEN_OBSERVATION",
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

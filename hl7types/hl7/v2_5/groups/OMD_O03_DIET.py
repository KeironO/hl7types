"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5
Class: OMD_O03.DIET
Type: Group
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..segments.NTE import NTE
from ..segments.ODS import ODS
from .OMD_O03_OBSERVATION import OMD_O03_OBSERVATION

_NTE = NTE
_ODS = ODS
_OMD_O03_OBSERVATION = OMD_O03_OBSERVATION


class OMD_O03_DIET(BaseModel):
    """HL7 v2 OMD_O03.DIET group.

    Attributes:
        ODS (List[ODS]): required
        NTE (Optional[List[NTE]]): optional
        OBSERVATION (Optional[List[OMD_O03_OBSERVATION]]): optional
    """

    ODS: list[_ODS] = Field(
        default=...,
        title="ODS",
        description="Required, repeating",
    )

    NTE: list[_NTE] | None = Field(
        default=None,
        title="NTE",
        description="Optional, repeating",
    )

    OBSERVATION: list[_OMD_O03_OBSERVATION] | None = Field(
        default=None,
        title="OBSERVATION",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}

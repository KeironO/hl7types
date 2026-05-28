"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.6
Class: OMD_O03.DIET
Type: Group
"""
from _future__ import annotations

from typing import Optional, List
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

    ODS: List[_ODS] = Field(
        default=...,
        title="ODS",
        description="Required, repeating",
    )

    NTE: Optional[List[_NTE]] = Field(
        default=None,
        title="NTE",
        description="Optional, repeating",
    )

    OBSERVATION: Optional[List[_OMD_O03_OBSERVATION]] = Field(
        default=None,
        title="OBSERVATION",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}

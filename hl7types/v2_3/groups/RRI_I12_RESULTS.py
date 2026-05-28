"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3
Class: RRI_I12.RESULTS
Type: Group
"""
from _future__ import annotations

from typing import Optional, List
from pydantic import BaseModel, Field

from ..segments.NTE import NTE
from ..segments.OBR import OBR

from .RRI_I12_OBSERVATION import RRI_I12_OBSERVATION

_NTE = NTE
_OBR = OBR
_RRI_I12_OBSERVATION = RRI_I12_OBSERVATION


class RRI_I12_RESULTS(BaseModel):
    """HL7 v2 RRI_I12.RESULTS group.

    Attributes:
        OBR (OBR): required
        NTE (Optional[List[NTE]]): optional
        OBSERVATION (Optional[List[RRI_I12_OBSERVATION]]): optional
    """

    OBR: _OBR = Field(
        default=...,
        title="OBR",
        description="Required",
    )

    NTE: Optional[List[_NTE]] = Field(
        default=None,
        title="NTE",
        description="Optional, repeating",
    )

    OBSERVATION: Optional[List[_RRI_I12_OBSERVATION]] = Field(
        default=None,
        title="OBSERVATION",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}

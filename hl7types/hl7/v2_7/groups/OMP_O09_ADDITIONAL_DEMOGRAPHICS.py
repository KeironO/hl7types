"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7
Class: OMP_O09.ADDITIONAL_DEMOGRAPHICS
Type: Group
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..segments.PD1 import PD1
from ..segments.PRT import PRT

_PD1 = PD1
_PRT = PRT


class OMP_O09_ADDITIONAL_DEMOGRAPHICS(BaseModel):
    """HL7 v2 OMP_O09.ADDITIONAL_DEMOGRAPHICS group.

    Attributes:
        PD1 (PD1): required
        PRT (Optional[List[PRT]]): optional
    """

    PD1: _PD1 = Field(
        default=...,
        title="PD1",
        description="Required",
    )

    PRT: list[_PRT] | None = Field(
        default=None,
        title="PRT",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}

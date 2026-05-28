"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8
Class: RRA_O18.ADMINISTRATION
Type: Group
"""
from _future__ import annotations

from typing import Optional, List
from pydantic import BaseModel, Field

from ..segments.RXR import RXR

from .RRA_O18_TREATMENT import RRA_O18_TREATMENT

_RRA_O18_TREATMENT = RRA_O18_TREATMENT
_RXR = RXR


class RRA_O18_ADMINISTRATION(BaseModel):
    """HL7 v2 RRA_O18.ADMINISTRATION group.

    Attributes:
        TREATMENT (List[RRA_O18_TREATMENT]): required
        RXR (RXR): required
    """

    TREATMENT: List[_RRA_O18_TREATMENT] = Field(
        default=...,
        title="TREATMENT",
        description="Required, repeating",
    )

    RXR: _RXR = Field(
        default=...,
        title="RXR",
        description="Required",
    )

    model_config = {"populate_by_name": True}

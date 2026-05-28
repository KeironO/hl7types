"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.2
Class: RDE_O11.PHARMACY_TREATMENT_INFUSION_ORDER
Type: Group
"""
from _future__ import annotations

from typing import Optional, List
from pydantic import BaseModel, Field

from ..segments.NTE import NTE
from ..segments.PRT import PRT
from ..segments.RXV import RXV

from .RDE_O11_TIMING_ENCODED import RDE_O11_TIMING_ENCODED

_NTE = NTE
_PRT = PRT
_RDE_O11_TIMING_ENCODED = RDE_O11_TIMING_ENCODED
_RXV = RXV


class RDE_O11_PHARMACY_TREATMENT_INFUSION_ORDER(BaseModel):
    """HL7 v2 RDE_O11.PHARMACY_TREATMENT_INFUSION_ORDER group.

    Attributes:
        RXV (RXV): required
        PRT (Optional[List[PRT]]): optional
        NTE (Optional[List[NTE]]): optional
        TIMING_ENCODED (List[RDE_O11_TIMING_ENCODED]): required
    """

    RXV: _RXV = Field(
        default=...,
        title="RXV",
        description="Required",
    )

    PRT: Optional[List[_PRT]] = Field(
        default=None,
        title="PRT",
        description="Optional, repeating",
    )

    NTE: Optional[List[_NTE]] = Field(
        default=None,
        title="NTE",
        description="Optional, repeating",
    )

    TIMING_ENCODED: List[_RDE_O11_TIMING_ENCODED] = Field(
        default=...,
        title="TIMING_ENCODED",
        description="Required, repeating",
    )

    model_config = {"populate_by_name": True}

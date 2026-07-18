"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8
Class: RDE_O11.PHARMACY_TREATMENT_INFUSION_ORDER
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import ConfigDict, Field
from hl7types.hl7 import HL7Model

from ..segments.NTE import NTE
from ..segments.PRT import PRT
from ..segments.RXV import RXV

from .RDE_O11_TIMING_ENCODED import RDE_O11_TIMING_ENCODED

_NTE = NTE
_PRT = PRT
_RDE_O11_TIMING_ENCODED = RDE_O11_TIMING_ENCODED
_RXV = RXV


class RDE_O11_PHARMACY_TREATMENT_INFUSION_ORDER(HL7Model):
    """HL7 v2 RDE_O11.PHARMACY_TREATMENT_INFUSION_ORDER group.

    Attributes:
        RXV (RXV): Pharmacy/Treatment Infusion, required
        PRT (Optional[List[PRT]]): Participation Information, optional
        NTE (Optional[List[NTE]]): Notes and Comments, optional
        TIMING_ENCODED (List[RDE_O11_TIMING_ENCODED]): required
    """

    RXV: _RXV = Field(
        title="RXV",
        description="Pharmacy/Treatment Infusion",
    )

    PRT: Optional[List[_PRT]] = Field(
        default=None,
        title="PRT",
        description="Participation Information",
    )

    NTE: Optional[List[_NTE]] = Field(
        default=None,
        title="NTE",
        description="Notes and Comments",
    )

    TIMING_ENCODED: List[_RDE_O11_TIMING_ENCODED] = Field(
        min_length=1,
        title="TIMING_ENCODED",
    )

    model_config = ConfigDict(populate_by_name=True)

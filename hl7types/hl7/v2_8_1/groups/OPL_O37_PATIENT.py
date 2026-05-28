"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.1
Class: OPL_O37.PATIENT
Type: Group
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..segments.AL1 import AL1
from ..segments.ARV import ARV
from ..segments.PD1 import PD1
from ..segments.PID import PID
from ..segments.PRT import PRT
from .OPL_O37_INSURANCE import OPL_O37_INSURANCE
from .OPL_O37_OBSERVATIONS_ON_PATIENT import OPL_O37_OBSERVATIONS_ON_PATIENT

_AL1 = AL1
_ARV = ARV
_OPL_O37_INSURANCE = OPL_O37_INSURANCE
_OPL_O37_OBSERVATIONS_ON_PATIENT = OPL_O37_OBSERVATIONS_ON_PATIENT
_PD1 = PD1
_PID = PID
_PRT = PRT


class OPL_O37_PATIENT(BaseModel):
    """HL7 v2 OPL_O37.PATIENT group.

    Attributes:
        PID (PID): required
        PD1 (Optional[PD1]): optional
        PRT (Optional[List[PRT]]): optional
        ARV (Optional[List[ARV]]): optional
        OBSERVATIONS_ON_PATIENT (Optional[List[OPL_O37_OBSERVATIONS_ON_PATIENT]]): optional
        INSURANCE (Optional[List[OPL_O37_INSURANCE]]): optional
        AL1 (Optional[List[AL1]]): optional
    """

    PID: _PID = Field(
        default=...,
        title="PID",
        description="Required",
    )

    PD1: _PD1 | None = Field(
        default=None,
        title="PD1",
        description="Optional",
    )

    PRT: list[_PRT] | None = Field(
        default=None,
        title="PRT",
        description="Optional, repeating",
    )

    ARV: list[_ARV] | None = Field(
        default=None,
        title="ARV",
        description="Optional, repeating",
    )

    OBSERVATIONS_ON_PATIENT: list[_OPL_O37_OBSERVATIONS_ON_PATIENT] | None = Field(
        default=None,
        title="OBSERVATIONS_ON_PATIENT",
        description="Optional, repeating",
    )

    INSURANCE: list[_OPL_O37_INSURANCE] | None = Field(
        default=None,
        title="INSURANCE",
        description="Optional, repeating",
    )

    AL1: list[_AL1] | None = Field(
        default=None,
        title="AL1",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}

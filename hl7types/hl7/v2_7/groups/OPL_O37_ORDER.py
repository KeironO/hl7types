"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7
Class: OPL_O37.ORDER
Type: Group
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..segments.BLG import BLG
from ..segments.CTI import CTI
from ..segments.FT1 import FT1
from ..segments.NK1 import NK1
from .OPL_O37_PATIENT import OPL_O37_PATIENT
from .OPL_O37_PRIOR_RESULT import OPL_O37_PRIOR_RESULT
from .OPL_O37_SPECIMEN import OPL_O37_SPECIMEN

_BLG = BLG
_CTI = CTI
_FT1 = FT1
_NK1 = NK1
_OPL_O37_PATIENT = OPL_O37_PATIENT
_OPL_O37_PRIOR_RESULT = OPL_O37_PRIOR_RESULT
_OPL_O37_SPECIMEN = OPL_O37_SPECIMEN


class OPL_O37_ORDER(BaseModel):
    """HL7 v2 OPL_O37.ORDER group.

    Attributes:
        NK1 (List[NK1]): required
        PATIENT (Optional[OPL_O37_PATIENT]): optional
        SPECIMEN (List[OPL_O37_SPECIMEN]): required
        PRIOR_RESULT (Optional[OPL_O37_PRIOR_RESULT]): optional
        FT1 (Optional[List[FT1]]): optional
        CTI (Optional[List[CTI]]): optional
        BLG (Optional[BLG]): optional
    """

    NK1: list[_NK1] = Field(
        default=...,
        title="NK1",
        description="Required, repeating",
    )

    PATIENT: _OPL_O37_PATIENT | None = Field(
        default=None,
        title="PATIENT",
        description="Optional",
    )

    SPECIMEN: list[_OPL_O37_SPECIMEN] = Field(
        default=...,
        title="SPECIMEN",
        description="Required, repeating",
    )

    PRIOR_RESULT: _OPL_O37_PRIOR_RESULT | None = Field(
        default=None,
        title="PRIOR_RESULT",
        description="Optional",
    )

    FT1: list[_FT1] | None = Field(
        default=None,
        title="FT1",
        description="Optional, repeating",
    )

    CTI: list[_CTI] | None = Field(
        default=None,
        title="CTI",
        description="Optional, repeating",
    )

    BLG: _BLG | None = Field(
        default=None,
        title="BLG",
        description="Optional",
    )

    model_config = {"populate_by_name": True}

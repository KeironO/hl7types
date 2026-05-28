"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5.1
Class: OML_O21.ORDER
Type: Group
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..segments.BLG import BLG
from ..segments.CTI import CTI
from ..segments.FT1 import FT1
from ..segments.ORC import ORC
from .OML_O21_OBSERVATION_REQUEST import OML_O21_OBSERVATION_REQUEST
from .OML_O21_TIMING import OML_O21_TIMING

_BLG = BLG
_CTI = CTI
_FT1 = FT1
_OML_O21_OBSERVATION_REQUEST = OML_O21_OBSERVATION_REQUEST
_OML_O21_TIMING = OML_O21_TIMING
_ORC = ORC


class OML_O21_ORDER(BaseModel):
    """HL7 v2 OML_O21.ORDER group.

    Attributes:
        ORC (ORC): required
        TIMING (Optional[List[OML_O21_TIMING]]): optional
        OBSERVATION_REQUEST (Optional[OML_O21_OBSERVATION_REQUEST]): optional
        FT1 (Optional[List[FT1]]): optional
        CTI (Optional[List[CTI]]): optional
        BLG (Optional[BLG]): optional
    """

    ORC: _ORC = Field(
        default=...,
        title="ORC",
        description="Required",
    )

    TIMING: list[_OML_O21_TIMING] | None = Field(
        default=None,
        title="TIMING",
        description="Optional, repeating",
    )

    OBSERVATION_REQUEST: _OML_O21_OBSERVATION_REQUEST | None = Field(
        default=None,
        title="OBSERVATION_REQUEST",
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

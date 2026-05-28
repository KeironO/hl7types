"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7.1
Class: OML_O39.ORDER
Type: Group
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..segments.BLG import BLG
from ..segments.CTI import CTI
from ..segments.FT1 import FT1
from ..segments.ORC import ORC
from ..segments.PRT import PRT
from .OML_O39_OBSERVATION_REQUEST import OML_O39_OBSERVATION_REQUEST
from .OML_O39_TIMING import OML_O39_TIMING

_BLG = BLG
_CTI = CTI
_FT1 = FT1
_OML_O39_OBSERVATION_REQUEST = OML_O39_OBSERVATION_REQUEST
_OML_O39_TIMING = OML_O39_TIMING
_ORC = ORC
_PRT = PRT


class OML_O39_ORDER(BaseModel):
    """HL7 v2 OML_O39.ORDER group.

    Attributes:
        ORC (ORC): required
        PRT (Optional[List[PRT]]): optional
        TIMING (Optional[List[OML_O39_TIMING]]): optional
        OBSERVATION_REQUEST (Optional[OML_O39_OBSERVATION_REQUEST]): optional
        FT1 (Optional[List[FT1]]): optional
        CTI (Optional[List[CTI]]): optional
        BLG (Optional[BLG]): optional
    """

    ORC: _ORC = Field(
        default=...,
        title="ORC",
        description="Required",
    )

    PRT: list[_PRT] | None = Field(
        default=None,
        title="PRT",
        description="Optional, repeating",
    )

    TIMING: list[_OML_O39_TIMING] | None = Field(
        default=None,
        title="TIMING",
        description="Optional, repeating",
    )

    OBSERVATION_REQUEST: _OML_O39_OBSERVATION_REQUEST | None = Field(
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

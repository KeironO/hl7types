"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8
Class: OMQ_O57.ORDER
Type: Group
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..segments.BLG import BLG
from ..segments.CTD import CTD
from ..segments.CTI import CTI
from ..segments.DG1 import DG1
from ..segments.FT1 import FT1
from ..segments.OBX import OBX
from ..segments.ORC import ORC
from ..segments.PRT import PRT
from ..segments.TXA import TXA
from .OMQ_O57_OBSERVATION import OMQ_O57_OBSERVATION
from .OMQ_O57_PRIOR_RESULT import OMQ_O57_PRIOR_RESULT

_BLG = BLG
_CTD = CTD
_CTI = CTI
_DG1 = DG1
_FT1 = FT1
_OBX = OBX
_OMQ_O57_OBSERVATION = OMQ_O57_OBSERVATION
_OMQ_O57_PRIOR_RESULT = OMQ_O57_PRIOR_RESULT
_ORC = ORC
_PRT = PRT
_TXA = TXA


class OMQ_O57_ORDER(BaseModel):
    """HL7 v2 OMQ_O57.ORDER group.

    Attributes:
        ORC (ORC): required
        PRT (Optional[List[PRT]]): optional
        OBX (OBX): required
        TXA (TXA): required
        CTD (Optional[CTD]): optional
        DG1 (Optional[List[DG1]]): optional
        OBSERVATION (Optional[List[OMQ_O57_OBSERVATION]]): optional
        PRIOR_RESULT (Optional[List[OMQ_O57_PRIOR_RESULT]]): optional
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

    OBX: _OBX = Field(
        default=...,
        title="OBX",
        description="Required",
    )

    TXA: _TXA = Field(
        default=...,
        title="TXA",
        description="Required",
    )

    CTD: _CTD | None = Field(
        default=None,
        title="CTD",
        description="Optional",
    )

    DG1: list[_DG1] | None = Field(
        default=None,
        title="DG1",
        description="Optional, repeating",
    )

    OBSERVATION: list[_OMQ_O57_OBSERVATION] | None = Field(
        default=None,
        title="OBSERVATION",
        description="Optional, repeating",
    )

    PRIOR_RESULT: list[_OMQ_O57_PRIOR_RESULT] | None = Field(
        default=None,
        title="PRIOR_RESULT",
        description="Optional, repeating",
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

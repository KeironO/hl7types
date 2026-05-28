"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.1
Class: OMQ_O57.ORDER
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
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
from .OMQ_O57_ORDER_DOCUMENT import OMQ_O57_ORDER_DOCUMENT
from .OMQ_O57_PRIOR_RESULT import OMQ_O57_PRIOR_RESULT

_BLG = BLG
_CTD = CTD
_CTI = CTI
_DG1 = DG1
_FT1 = FT1
_OBX = OBX
_OMQ_O57_OBSERVATION = OMQ_O57_OBSERVATION
_OMQ_O57_ORDER_DOCUMENT = OMQ_O57_ORDER_DOCUMENT
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
        ORDER_DOCUMENT (Optional[List[OMQ_O57_ORDER_DOCUMENT]]): optional
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

    PRT: Optional[List[_PRT]] = Field(
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

    CTD: Optional[_CTD] = Field(
        default=None,
        title="CTD",
        description="Optional",
    )

    DG1: Optional[List[_DG1]] = Field(
        default=None,
        title="DG1",
        description="Optional, repeating",
    )

    ORDER_DOCUMENT: Optional[List[_OMQ_O57_ORDER_DOCUMENT]] = Field(
        default=None,
        title="ORDER_DOCUMENT",
        description="Optional, repeating",
    )

    OBSERVATION: Optional[List[_OMQ_O57_OBSERVATION]] = Field(
        default=None,
        title="OBSERVATION",
        description="Optional, repeating",
    )

    PRIOR_RESULT: Optional[List[_OMQ_O57_PRIOR_RESULT]] = Field(
        default=None,
        title="PRIOR_RESULT",
        description="Optional, repeating",
    )

    FT1: Optional[List[_FT1]] = Field(
        default=None,
        title="FT1",
        description="Optional, repeating",
    )

    CTI: Optional[List[_CTI]] = Field(
        default=None,
        title="CTI",
        description="Optional, repeating",
    )

    BLG: Optional[_BLG] = Field(
        default=None,
        title="BLG",
        description="Optional",
    )

    model_config = {"populate_by_name": True}

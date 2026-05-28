"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5.1
Class: OMG_O19.ORDER
Type: Group
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..segments.BLG import BLG
from ..segments.CTD import CTD
from ..segments.CTI import CTI
from ..segments.DG1 import DG1
from ..segments.FT1 import FT1
from ..segments.NTE import NTE
from ..segments.OBR import OBR
from ..segments.ORC import ORC
from .OMG_O19_OBSERVATION import OMG_O19_OBSERVATION
from .OMG_O19_PRIOR_RESULT import OMG_O19_PRIOR_RESULT
from .OMG_O19_SPECIMEN import OMG_O19_SPECIMEN
from .OMG_O19_TIMING import OMG_O19_TIMING

_BLG = BLG
_CTD = CTD
_CTI = CTI
_DG1 = DG1
_FT1 = FT1
_NTE = NTE
_OBR = OBR
_OMG_O19_OBSERVATION = OMG_O19_OBSERVATION
_OMG_O19_PRIOR_RESULT = OMG_O19_PRIOR_RESULT
_OMG_O19_SPECIMEN = OMG_O19_SPECIMEN
_OMG_O19_TIMING = OMG_O19_TIMING
_ORC = ORC


class OMG_O19_ORDER(BaseModel):
    """HL7 v2 OMG_O19.ORDER group.

    Attributes:
        ORC (ORC): required
        TIMING (Optional[List[OMG_O19_TIMING]]): optional
        OBR (OBR): required
        NTE (Optional[List[NTE]]): optional
        CTD (Optional[CTD]): optional
        DG1 (Optional[List[DG1]]): optional
        OBSERVATION (Optional[List[OMG_O19_OBSERVATION]]): optional
        SPECIMEN (Optional[List[OMG_O19_SPECIMEN]]): optional
        PRIOR_RESULT (Optional[List[OMG_O19_PRIOR_RESULT]]): optional
        FT1 (Optional[List[FT1]]): optional
        CTI (Optional[List[CTI]]): optional
        BLG (Optional[BLG]): optional
    """

    ORC: _ORC = Field(
        default=...,
        title="ORC",
        description="Required",
    )

    TIMING: list[_OMG_O19_TIMING] | None = Field(
        default=None,
        title="TIMING",
        description="Optional, repeating",
    )

    OBR: _OBR = Field(
        default=...,
        title="OBR",
        description="Required",
    )

    NTE: list[_NTE] | None = Field(
        default=None,
        title="NTE",
        description="Optional, repeating",
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

    OBSERVATION: list[_OMG_O19_OBSERVATION] | None = Field(
        default=None,
        title="OBSERVATION",
        description="Optional, repeating",
    )

    SPECIMEN: list[_OMG_O19_SPECIMEN] | None = Field(
        default=None,
        title="SPECIMEN",
        description="Optional, repeating",
    )

    PRIOR_RESULT: list[_OMG_O19_PRIOR_RESULT] | None = Field(
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

"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.4
Class: ORU_R01.ORDER_OBSERVATION
Type: Group
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..segments.CTD import CTD
from ..segments.CTI import CTI
from ..segments.FT1 import FT1
from ..segments.NTE import NTE
from ..segments.OBR import OBR
from ..segments.ORC import ORC
from .ORU_R01_OBSERVATION import ORU_R01_OBSERVATION

_CTD = CTD
_CTI = CTI
_FT1 = FT1
_NTE = NTE
_OBR = OBR
_ORC = ORC
_ORU_R01_OBSERVATION = ORU_R01_OBSERVATION


class ORU_R01_ORDER_OBSERVATION(BaseModel):
    """HL7 v2 ORU_R01.ORDER_OBSERVATION group.

    Attributes:
        ORC (Optional[ORC]): optional
        OBR (OBR): required
        NTE (Optional[List[NTE]]): optional
        CTD (Optional[CTD]): optional
        OBSERVATION (List[ORU_R01_OBSERVATION]): required
        FT1 (Optional[List[FT1]]): optional
        CTI (Optional[List[CTI]]): optional
    """

    ORC: _ORC | None = Field(
        default=None,
        title="ORC",
        description="Optional",
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

    OBSERVATION: list[_ORU_R01_OBSERVATION] = Field(
        default=...,
        title="OBSERVATION",
        description="Required, repeating",
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

    model_config = {"populate_by_name": True}

"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3
Class: ORF_R04.ORDER
Type: Group
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..segments.CTI import CTI
from ..segments.NTE import NTE
from ..segments.OBR import OBR
from ..segments.ORC import ORC
from .ORF_R04_OBSERVATION import ORF_R04_OBSERVATION

_CTI = CTI
_NTE = NTE
_OBR = OBR
_ORC = ORC
_ORF_R04_OBSERVATION = ORF_R04_OBSERVATION


class ORF_R04_ORDER(BaseModel):
    """HL7 v2 ORF_R04.ORDER group.

    Attributes:
        ORC (Optional[ORC]): optional
        OBR (OBR): required
        NTE (Optional[List[NTE]]): optional
        OBSERVATION (List[ORF_R04_OBSERVATION]): required
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

    OBSERVATION: list[_ORF_R04_OBSERVATION] = Field(
        default=...,
        title="OBSERVATION",
        description="Required, repeating",
    )

    CTI: list[_CTI] | None = Field(
        default=None,
        title="CTI",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}

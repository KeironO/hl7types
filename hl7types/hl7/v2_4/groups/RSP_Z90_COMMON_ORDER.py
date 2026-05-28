"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.4
Class: RSP_Z90.COMMON_ORDER
Type: Group
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..segments.CTD import CTD
from ..segments.NTE import NTE
from ..segments.OBR import OBR
from ..segments.ORC import ORC
from .RSP_Z90_OBSERVATION import RSP_Z90_OBSERVATION

_CTD = CTD
_NTE = NTE
_OBR = OBR
_ORC = ORC
_RSP_Z90_OBSERVATION = RSP_Z90_OBSERVATION


class RSP_Z90_COMMON_ORDER(BaseModel):
    """HL7 v2 RSP_Z90.COMMON_ORDER group.

    Attributes:
        ORC (ORC): required
        OBR (OBR): required
        NTE (Optional[List[NTE]]): optional
        CTD (Optional[CTD]): optional
        OBSERVATION (List[RSP_Z90_OBSERVATION]): required
    """

    ORC: _ORC = Field(
        default=...,
        title="ORC",
        description="Required",
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

    OBSERVATION: list[_RSP_Z90_OBSERVATION] = Field(
        default=...,
        title="OBSERVATION",
        description="Required, repeating",
    )

    model_config = {"populate_by_name": True}

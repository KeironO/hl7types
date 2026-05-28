"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.4
Class: ORG_O20.ORDER
Type: Group
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..segments.CTI import CTI
from ..segments.NTE import NTE
from ..segments.OBR import OBR
from ..segments.ORC import ORC

_CTI = CTI
_NTE = NTE
_OBR = OBR
_ORC = ORC


class ORG_O20_ORDER(BaseModel):
    """HL7 v2 ORG_O20.ORDER group.

    Attributes:
        ORC (ORC): required
        OBR (Optional[OBR]): optional
        NTE (Optional[List[NTE]]): optional
        CTI (Optional[List[CTI]]): optional
    """

    ORC: _ORC = Field(
        default=...,
        title="ORC",
        description="Required",
    )

    OBR: _OBR | None = Field(
        default=None,
        title="OBR",
        description="Optional",
    )

    NTE: list[_NTE] | None = Field(
        default=None,
        title="NTE",
        description="Optional, repeating",
    )

    CTI: list[_CTI] | None = Field(
        default=None,
        title="CTI",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}

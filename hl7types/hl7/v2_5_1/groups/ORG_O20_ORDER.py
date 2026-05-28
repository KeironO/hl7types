"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5.1
Class: ORG_O20.ORDER
Type: Group
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..segments.CTI import CTI
from ..segments.NTE import NTE
from ..segments.OBR import OBR
from ..segments.ORC import ORC
from .ORG_O20_SPECIMEN import ORG_O20_SPECIMEN
from .ORG_O20_TIMING import ORG_O20_TIMING

_CTI = CTI
_NTE = NTE
_OBR = OBR
_ORC = ORC
_ORG_O20_SPECIMEN = ORG_O20_SPECIMEN
_ORG_O20_TIMING = ORG_O20_TIMING


class ORG_O20_ORDER(BaseModel):
    """HL7 v2 ORG_O20.ORDER group.

    Attributes:
        ORC (ORC): required
        TIMING (Optional[List[ORG_O20_TIMING]]): optional
        OBR (Optional[OBR]): optional
        NTE (Optional[List[NTE]]): optional
        CTI (Optional[List[CTI]]): optional
        SPECIMEN (Optional[List[ORG_O20_SPECIMEN]]): optional
    """

    ORC: _ORC = Field(
        default=...,
        title="ORC",
        description="Required",
    )

    TIMING: list[_ORG_O20_TIMING] | None = Field(
        default=None,
        title="TIMING",
        description="Optional, repeating",
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

    SPECIMEN: list[_ORG_O20_SPECIMEN] | None = Field(
        default=None,
        title="SPECIMEN",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}

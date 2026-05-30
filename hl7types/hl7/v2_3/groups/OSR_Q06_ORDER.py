"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3
Class: OSR_Q06.ORDER
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.CTI import CTI
from ..segments.NTE import NTE
from ..segments.OBR import OBR
from ..segments.ORC import ORC

_CTI = CTI
_NTE = NTE
_OBR = OBR
_ORC = ORC


class OSR_Q06_ORDER(HL7Model):
    """HL7 v2 OSR_Q06.ORDER group.

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

    OBR: Optional[_OBR] = Field(
        default=None,
        title="OBR",
        description="Optional",
    )

    NTE: Optional[List[_NTE]] = Field(
        default=None,
        title="NTE",
        description="Optional, repeating",
    )

    CTI: Optional[List[_CTI]] = Field(
        default=None,
        title="CTI",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}

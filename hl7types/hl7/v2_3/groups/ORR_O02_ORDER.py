"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3
Class: ORR_O02.ORDER
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.CTI import CTI
from ..segments.NTE import NTE
from ..segments.ORC import ORC

from .ORR_O02_CHOICE import ORR_O02_CHOICE

_CTI = CTI
_NTE = NTE
_ORC = ORC
_ORR_O02_CHOICE = ORR_O02_CHOICE


class ORR_O02_ORDER(HL7Model):
    """HL7 v2 ORR_O02.ORDER group.

    Attributes:
        ORC (ORC): required
        CHOICE (ORR_O02_CHOICE): required
        NTE (Optional[List[NTE]]): optional
        CTI (Optional[List[CTI]]): optional
    """

    ORC: _ORC = Field(
        title="ORC",
        description="Required",
    )

    CHOICE: _ORR_O02_CHOICE = Field(
        title="CHOICE",
        description="Required",
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

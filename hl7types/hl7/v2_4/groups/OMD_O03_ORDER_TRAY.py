"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.4
Class: OMD_O03.ORDER_TRAY
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.NTE import NTE
from ..segments.ODT import ODT
from ..segments.ORC import ORC

_NTE = NTE
_ODT = ODT
_ORC = ORC


class OMD_O03_ORDER_TRAY(HL7Model):
    """HL7 v2 OMD_O03.ORDER_TRAY group.

    Attributes:
        ORC (ORC): required
        ODT (List[ODT]): required
        NTE (Optional[List[NTE]]): optional
    """

    ORC: _ORC = Field(
        title="ORC",
        description="Required",
    )

    ODT: List[_ODT] = Field(
        min_length=1,
        title="ODT",
        description="Required, repeating",
    )

    NTE: Optional[List[_NTE]] = Field(
        default=None,
        title="NTE",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}

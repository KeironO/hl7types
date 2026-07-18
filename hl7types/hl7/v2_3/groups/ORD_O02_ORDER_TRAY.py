"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3
Class: ORD_O02.ORDER_TRAY
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import ConfigDict, Field
from hl7types.hl7 import HL7Model

from ..segments.NTE import NTE
from ..segments.ODT import ODT
from ..segments.ORC import ORC

_NTE = NTE
_ODT = ODT
_ORC = ORC


class ORD_O02_ORDER_TRAY(HL7Model):
    """HL7 v2 ORD_O02.ORDER_TRAY group.

    Attributes:
        ORC (ORC): Common order segment, required
        ODT (Optional[List[ODT]]): Diet tray instructions segment, optional
        NTE (Optional[List[NTE]]): Notes and comments segment, optional
    """

    ORC: _ORC = Field(
        title="ORC",
        description="Common order segment",
    )

    ODT: Optional[List[_ODT]] = Field(
        default=None,
        title="ODT",
        description="Diet tray instructions segment",
    )

    NTE: Optional[List[_NTE]] = Field(
        default=None,
        title="NTE",
        description="Notes and comments segment",
    )

    model_config = ConfigDict(populate_by_name=True)

"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3.1
Class: OMD_O01.ORDER_TRAY
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


class OMD_O01_ORDER_TRAY(HL7Model):
    """HL7 v2 OMD_O01.ORDER_TRAY group.

    Attributes:
        ORC (ORC): ORC - common order segment, required
        ODT (List[ODT]): ODT - diet tray instructions segment, required
        NTE (Optional[List[NTE]]): NTE - notes and comments segment, optional
    """

    ORC: _ORC = Field(
        title="ORC",
        description="ORC - common order segment",
    )

    ODT: List[_ODT] = Field(
        min_length=1,
        title="ODT",
        description="ODT - diet tray instructions segment",
    )

    NTE: Optional[List[_NTE]] = Field(
        default=None,
        title="NTE",
        description="NTE - notes and comments segment",
    )

    model_config = ConfigDict(populate_by_name=True)

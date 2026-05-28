"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.4
Class: OMS_O05.ORDER
Type: Group
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..segments.BLG import BLG
from ..segments.NTE import NTE
from ..segments.ORC import ORC
from ..segments.RQ1 import RQ1
from ..segments.RQD import RQD
from .OMS_O05_OBSERVATION import OMS_O05_OBSERVATION

_BLG = BLG
_NTE = NTE
_OMS_O05_OBSERVATION = OMS_O05_OBSERVATION
_ORC = ORC
_RQ1 = RQ1
_RQD = RQD


class OMS_O05_ORDER(BaseModel):
    """HL7 v2 OMS_O05.ORDER group.

    Attributes:
        ORC (ORC): required
        RQD (RQD): required
        RQ1 (Optional[RQ1]): optional
        NTE (Optional[List[NTE]]): optional
        OBSERVATION (Optional[List[OMS_O05_OBSERVATION]]): optional
        BLG (Optional[BLG]): optional
    """

    ORC: _ORC = Field(
        default=...,
        title="ORC",
        description="Required",
    )

    RQD: _RQD = Field(
        default=...,
        title="RQD",
        description="Required",
    )

    RQ1: _RQ1 | None = Field(
        default=None,
        title="RQ1",
        description="Optional",
    )

    NTE: list[_NTE] | None = Field(
        default=None,
        title="NTE",
        description="Optional, repeating",
    )

    OBSERVATION: list[_OMS_O05_OBSERVATION] | None = Field(
        default=None,
        title="OBSERVATION",
        description="Optional, repeating",
    )

    BLG: _BLG | None = Field(
        default=None,
        title="BLG",
        description="Optional",
    )

    model_config = {"populate_by_name": True}

"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7
Class: OMS_O05.ORDER
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import ConfigDict, Field
from hl7types.hl7 import HL7Model

from ..segments.BLG import BLG
from ..segments.NTE import NTE
from ..segments.ORC import ORC
from ..segments.RQ1 import RQ1
from ..segments.RQD import RQD

from .OMS_O05_OBSERVATION import OMS_O05_OBSERVATION
from .OMS_O05_TIMING import OMS_O05_TIMING

_BLG = BLG
_NTE = NTE
_OMS_O05_OBSERVATION = OMS_O05_OBSERVATION
_OMS_O05_TIMING = OMS_O05_TIMING
_ORC = ORC
_RQ1 = RQ1
_RQD = RQD


class OMS_O05_ORDER(HL7Model):
    """HL7 v2 OMS_O05.ORDER group.

    Attributes:
        ORC (ORC): Common Order, required
        TIMING (Optional[List[OMS_O05_TIMING]]): optional
        RQD (RQD): Requisition Detail, required
        RQ1 (Optional[RQ1]): Requisition Detail-1, optional
        NTE (Optional[List[NTE]]): Notes and Comments, optional
        OBSERVATION (Optional[List[OMS_O05_OBSERVATION]]): optional
        BLG (Optional[BLG]): Billing, optional
    """

    ORC: _ORC = Field(
        title="ORC",
        description="Common Order",
    )

    TIMING: Optional[List[_OMS_O05_TIMING]] = Field(
        default=None,
        title="TIMING",
    )

    RQD: _RQD = Field(
        title="RQD",
        description="Requisition Detail",
    )

    RQ1: Optional[_RQ1] = Field(
        default=None,
        title="RQ1",
        description="Requisition Detail-1",
    )

    NTE: Optional[List[_NTE]] = Field(
        default=None,
        title="NTE",
        description="Notes and Comments",
    )

    OBSERVATION: Optional[List[_OMS_O05_OBSERVATION]] = Field(
        default=None,
        title="OBSERVATION",
    )

    BLG: Optional[_BLG] = Field(
        default=None,
        title="BLG",
        description="Billing",
    )

    model_config = ConfigDict(populate_by_name=True)

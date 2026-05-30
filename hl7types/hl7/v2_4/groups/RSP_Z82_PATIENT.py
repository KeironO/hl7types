"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.4
Class: RSP_Z82.PATIENT
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.NTE import NTE
from ..segments.PD1 import PD1
from ..segments.PID import PID

from .RSP_Z82_COMMON_ORDER import RSP_Z82_COMMON_ORDER
from .RSP_Z82_VISIT import RSP_Z82_VISIT

_NTE = NTE
_PD1 = PD1
_PID = PID
_RSP_Z82_COMMON_ORDER = RSP_Z82_COMMON_ORDER
_RSP_Z82_VISIT = RSP_Z82_VISIT


class RSP_Z82_PATIENT(HL7Model):
    """HL7 v2 RSP_Z82.PATIENT group.

    Attributes:
        PID (PID): required
        PD1 (Optional[PD1]): optional
        NTE (Optional[List[NTE]]): optional
        VISIT (Optional[RSP_Z82_VISIT]): optional
        COMMON_ORDER (List[RSP_Z82_COMMON_ORDER]): required
    """

    PID: _PID = Field(
        default=...,
        title="PID",
        description="Required",
    )

    PD1: Optional[_PD1] = Field(
        default=None,
        title="PD1",
        description="Optional",
    )

    NTE: Optional[List[_NTE]] = Field(
        default=None,
        title="NTE",
        description="Optional, repeating",
    )

    VISIT: Optional[_RSP_Z82_VISIT] = Field(
        default=None,
        title="VISIT",
        description="Optional",
    )

    COMMON_ORDER: List[_RSP_Z82_COMMON_ORDER] = Field(
        default=...,
        title="COMMON_ORDER",
        description="Required, repeating",
    )

    model_config = {"populate_by_name": True}

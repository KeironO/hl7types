"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5.1
Class: OSR_Q06.ORDER
Type: Group
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..segments.CTI import CTI
from ..segments.NTE import NTE
from ..segments.ORC import ORC
from .OSR_Q06_OBRRQDRQ1RXOODSODT_SUPPGRP import OSR_Q06_OBRRQDRQ1RXOODSODT_SUPPGRP
from .OSR_Q06_TIMING import OSR_Q06_TIMING

_CTI = CTI
_NTE = NTE
_ORC = ORC
_OSR_Q06_OBRRQDRQ1RXOODSODT_SUPPGRP = OSR_Q06_OBRRQDRQ1RXOODSODT_SUPPGRP
_OSR_Q06_TIMING = OSR_Q06_TIMING


class OSR_Q06_ORDER(BaseModel):
    """HL7 v2 OSR_Q06.ORDER group.

    Attributes:
        ORC (ORC): required
        TIMING (Optional[List[OSR_Q06_TIMING]]): optional
        OBRRQDRQ1RXOODSODT_SUPPGRP (OSR_Q06_OBRRQDRQ1RXOODSODT_SUPPGRP): required
        NTE (Optional[List[NTE]]): optional
        CTI (Optional[List[CTI]]): optional
    """

    ORC: _ORC = Field(
        default=...,
        title="ORC",
        description="Required",
    )

    TIMING: list[_OSR_Q06_TIMING] | None = Field(
        default=None,
        title="TIMING",
        description="Optional, repeating",
    )

    OBRRQDRQ1RXOODSODT_SUPPGRP: _OSR_Q06_OBRRQDRQ1RXOODSODT_SUPPGRP = Field(
        default=...,
        title="OBRRQDRQ1RXOODSODT_SUPPGRP",
        description="Required",
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

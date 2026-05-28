"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5
Class: ORM_O01.ORDER_DETAIL
Type: Group
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..segments.CTD import CTD
from ..segments.DG1 import DG1
from ..segments.NTE import NTE
from .ORM_O01_OBRRQDRQ1RXOODSODT_SUPPGRP import ORM_O01_OBRRQDRQ1RXOODSODT_SUPPGRP
from .ORM_O01_OBSERVATION import ORM_O01_OBSERVATION

_CTD = CTD
_DG1 = DG1
_NTE = NTE
_ORM_O01_OBRRQDRQ1RXOODSODT_SUPPGRP = ORM_O01_OBRRQDRQ1RXOODSODT_SUPPGRP
_ORM_O01_OBSERVATION = ORM_O01_OBSERVATION


class ORM_O01_ORDER_DETAIL(BaseModel):
    """HL7 v2 ORM_O01.ORDER_DETAIL group.

    Attributes:
        OBRRQDRQ1RXOODSODT_SUPPGRP (ORM_O01_OBRRQDRQ1RXOODSODT_SUPPGRP): required
        NTE (Optional[List[NTE]]): optional
        CTD (Optional[CTD]): optional
        DG1 (Optional[List[DG1]]): optional
        OBSERVATION (Optional[List[ORM_O01_OBSERVATION]]): optional
    """

    OBRRQDRQ1RXOODSODT_SUPPGRP: _ORM_O01_OBRRQDRQ1RXOODSODT_SUPPGRP = Field(
        default=...,
        title="OBRRQDRQ1RXOODSODT_SUPPGRP",
        description="Required",
    )

    NTE: list[_NTE] | None = Field(
        default=None,
        title="NTE",
        description="Optional, repeating",
    )

    CTD: _CTD | None = Field(
        default=None,
        title="CTD",
        description="Optional",
    )

    DG1: list[_DG1] | None = Field(
        default=None,
        title="DG1",
        description="Optional, repeating",
    )

    OBSERVATION: list[_ORM_O01_OBSERVATION] | None = Field(
        default=None,
        title="OBSERVATION",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}

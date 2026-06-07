"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5
Class: ORM_O01.ORDER_DETAIL
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

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


class ORM_O01_ORDER_DETAIL(HL7Model):
    """HL7 v2 ORM_O01.ORDER_DETAIL group.

    Attributes:
        OBRRQDRQ1RXOODSODT_SUPPGRP (ORM_O01_OBRRQDRQ1RXOODSODT_SUPPGRP): required
        NTE (Optional[List[NTE]]): optional
        CTD (Optional[CTD]): optional
        DG1 (Optional[List[DG1]]): optional
        OBSERVATION (Optional[List[ORM_O01_OBSERVATION]]): optional
    """

    OBRRQDRQ1RXOODSODT_SUPPGRP: _ORM_O01_OBRRQDRQ1RXOODSODT_SUPPGRP = Field(
        title="OBRRQDRQ1RXOODSODT_SUPPGRP",
        description="Required",
    )

    NTE: Optional[List[_NTE]] = Field(
        default=None,
        title="NTE",
        description="Optional, repeating",
    )

    CTD: Optional[_CTD] = Field(
        default=None,
        title="CTD",
        description="Optional",
    )

    DG1: Optional[List[_DG1]] = Field(
        default=None,
        title="DG1",
        description="Optional, repeating",
    )

    OBSERVATION: Optional[List[_ORM_O01_OBSERVATION]] = Field(
        default=None,
        title="OBSERVATION",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}

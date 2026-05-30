"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5.1
Class: PGL_PC6.ORDER_DETAIL
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.NTE import NTE
from ..segments.VAR import VAR

from .PGL_PC6_OBR_SUPPGRP import PGL_PC6_OBR_SUPPGRP
from .PGL_PC6_ORDER_OBSERVATION import PGL_PC6_ORDER_OBSERVATION

_NTE = NTE
_PGL_PC6_OBR_SUPPGRP = PGL_PC6_OBR_SUPPGRP
_PGL_PC6_ORDER_OBSERVATION = PGL_PC6_ORDER_OBSERVATION
_VAR = VAR


class PGL_PC6_ORDER_DETAIL(HL7Model):
    """HL7 v2 PGL_PC6.ORDER_DETAIL group.

    Attributes:
        OBR_SUPPGRP (PGL_PC6_OBR_SUPPGRP): required
        NTE (Optional[List[NTE]]): optional
        VAR (Optional[List[VAR]]): optional
        ORDER_OBSERVATION (Optional[List[PGL_PC6_ORDER_OBSERVATION]]): optional
    """

    OBR_SUPPGRP: _PGL_PC6_OBR_SUPPGRP = Field(
        default=...,
        title="OBR_SUPPGRP",
        description="Required",
    )

    NTE: Optional[List[_NTE]] = Field(
        default=None,
        title="NTE",
        description="Optional, repeating",
    )

    VAR: Optional[List[_VAR]] = Field(
        default=None,
        title="VAR",
        description="Optional, repeating",
    )

    ORDER_OBSERVATION: Optional[List[_PGL_PC6_ORDER_OBSERVATION]] = Field(
        default=None,
        title="ORDER_OBSERVATION",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}

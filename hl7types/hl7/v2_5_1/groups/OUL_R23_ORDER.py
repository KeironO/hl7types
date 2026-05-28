"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5.1
Class: OUL_R23.ORDER
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import BaseModel, Field

from ..segments.CTI import CTI
from ..segments.NTE import NTE
from ..segments.OBR import OBR
from ..segments.ORC import ORC

from .OUL_R23_OBXTCDSIDNTE_SUPPGRP import OUL_R23_OBXTCDSIDNTE_SUPPGRP
from .OUL_R23_TQ1TQ2_SUPPGRP import OUL_R23_TQ1TQ2_SUPPGRP

_CTI = CTI
_NTE = NTE
_OBR = OBR
_ORC = ORC
_OUL_R23_OBXTCDSIDNTE_SUPPGRP = OUL_R23_OBXTCDSIDNTE_SUPPGRP
_OUL_R23_TQ1TQ2_SUPPGRP = OUL_R23_TQ1TQ2_SUPPGRP


class OUL_R23_ORDER(BaseModel):
    """HL7 v2 OUL_R23.ORDER group.

    Attributes:
        OBR (OBR): required
        ORC (Optional[ORC]): optional
        NTE (Optional[List[NTE]]): optional
        TQ1TQ2_SUPPGRP (Optional[List[OUL_R23_TQ1TQ2_SUPPGRP]]): optional
        OBXTCDSIDNTE_SUPPGRP (Optional[List[OUL_R23_OBXTCDSIDNTE_SUPPGRP]]): optional
        CTI (Optional[List[CTI]]): optional
    """

    OBR: _OBR = Field(
        default=...,
        title="OBR",
        description="Required",
    )

    ORC: Optional[_ORC] = Field(
        default=None,
        title="ORC",
        description="Optional",
    )

    NTE: Optional[List[_NTE]] = Field(
        default=None,
        title="NTE",
        description="Optional, repeating",
    )

    TQ1TQ2_SUPPGRP: Optional[List[_OUL_R23_TQ1TQ2_SUPPGRP]] = Field(
        default=None,
        title="TQ1TQ2_SUPPGRP",
        description="Optional, repeating",
    )

    OBXTCDSIDNTE_SUPPGRP: Optional[List[_OUL_R23_OBXTCDSIDNTE_SUPPGRP]] = Field(
        default=None,
        title="OBXTCDSIDNTE_SUPPGRP",
        description="Optional, repeating",
    )

    CTI: Optional[List[_CTI]] = Field(
        default=None,
        title="CTI",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}

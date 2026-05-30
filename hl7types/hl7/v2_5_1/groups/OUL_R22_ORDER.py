"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5.1
Class: OUL_R22.ORDER
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.CTI import CTI
from ..segments.NTE import NTE
from ..segments.OBR import OBR
from ..segments.ORC import ORC

from .OUL_R22_OBXTCDSIDNTE_SUPPGRP import OUL_R22_OBXTCDSIDNTE_SUPPGRP
from .OUL_R22_TIMING_QTY import OUL_R22_TIMING_QTY

_CTI = CTI
_NTE = NTE
_OBR = OBR
_ORC = ORC
_OUL_R22_OBXTCDSIDNTE_SUPPGRP = OUL_R22_OBXTCDSIDNTE_SUPPGRP
_OUL_R22_TIMING_QTY = OUL_R22_TIMING_QTY


class OUL_R22_ORDER(HL7Model):
    """HL7 v2 OUL_R22.ORDER group.

    Attributes:
        OBR (OBR): required
        ORC (Optional[ORC]): optional
        NTE (Optional[List[NTE]]): optional
        TIMING_QTY (Optional[List[OUL_R22_TIMING_QTY]]): optional
        OBXTCDSIDNTE_SUPPGRP (Optional[List[OUL_R22_OBXTCDSIDNTE_SUPPGRP]]): optional
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

    TIMING_QTY: Optional[List[_OUL_R22_TIMING_QTY]] = Field(
        default=None,
        title="TIMING_QTY",
        description="Optional, repeating",
    )

    OBXTCDSIDNTE_SUPPGRP: Optional[List[_OUL_R22_OBXTCDSIDNTE_SUPPGRP]] = Field(
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

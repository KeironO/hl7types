"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5.1
Class: CSU_C09.RXARXR_SUPPGRP
Type: Group
"""
from __future__ import annotations

from typing import Optional
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.RXA import RXA
from ..segments.RXR import RXR

_RXA = RXA
_RXR = RXR


class CSU_C09_RXARXR_SUPPGRP(HL7Model):
    """HL7 v2 CSU_C09.RXARXR_SUPPGRP group.

    Attributes:
        RXA (RXA): required
        RXR (RXR): required
    """

    RXA: _RXA = Field(
        default=...,
        title="RXA",
        description="Required",
    )

    RXR: _RXR = Field(
        default=...,
        title="RXR",
        description="Required",
    )

    model_config = {"populate_by_name": True}

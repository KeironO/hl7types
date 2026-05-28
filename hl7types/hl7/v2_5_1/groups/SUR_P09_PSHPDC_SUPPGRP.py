"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5.1
Class: SUR_P09.PSHPDC_SUPPGRP
Type: Group
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..segments.PDC import PDC
from ..segments.PSH import PSH

_PDC = PDC
_PSH = PSH


class SUR_P09_PSHPDC_SUPPGRP(BaseModel):
    """HL7 v2 SUR_P09.PSHPDC_SUPPGRP group.

    Attributes:
        PSH (PSH): required
        PDC (PDC): required
    """

    PSH: _PSH = Field(
        default=...,
        title="PSH",
        description="Required",
    )

    PDC: _PDC = Field(
        default=...,
        title="PDC",
        description="Required",
    )

    model_config = {"populate_by_name": True}

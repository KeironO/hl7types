"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5.1
Class: SUR_P09.PSHPDC_SUPPGRP
Type: Group
"""
from __future__ import annotations

from pydantic import ConfigDict, Field
from hl7types.hl7 import HL7Model

from ..segments.PDC import PDC
from ..segments.PSH import PSH

_PDC = PDC
_PSH = PSH


class SUR_P09_PSHPDC_SUPPGRP(HL7Model):
    """HL7 v2 SUR_P09.PSHPDC_SUPPGRP group.

    Attributes:
        PSH (PSH): Product Summary Header, required
        PDC (PDC): Product Detail Country, required
    """

    PSH: _PSH = Field(
        title="PSH",
        description="Product Summary Header",
    )

    PDC: _PDC = Field(
        title="PDC",
        description="Product Detail Country",
    )

    model_config = ConfigDict(populate_by_name=True)

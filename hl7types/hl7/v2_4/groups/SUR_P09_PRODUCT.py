"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.4
Class: SUR_P09.PRODUCT
Type: Group
"""
from __future__ import annotations

from typing import Optional
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.PDC import PDC
from ..segments.PSH import PSH

_PDC = PDC
_PSH = PSH


class SUR_P09_PRODUCT(HL7Model):
    """HL7 v2 SUR_P09.PRODUCT group.

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

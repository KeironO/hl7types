"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.1
Class: RSP_E22.PSL_ITEM_INFO
Type: Group
"""
from __future__ import annotations

from typing import Optional
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.PSL import PSL

_PSL = PSL


class RSP_E22_PSL_ITEM_INFO(HL7Model):
    """HL7 v2 RSP_E22.PSL_ITEM_INFO group.

    Attributes:
        PSL (PSL): required
    """

    PSL: _PSL = Field(
        default=...,
        title="PSL",
        description="Required",
    )

    model_config = {"populate_by_name": True}

"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3
Class: MFN_M01.MF
Type: Group
"""
from __future__ import annotations

from typing import Optional
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.MFE import MFE

_MFE = MFE


class MFN_M01_MF(HL7Model):
    """HL7 v2 MFN_M01.MF group.

    Attributes:
        MFE (MFE): required
    """

    MFE: _MFE = Field(
        default=...,
        title="MFE",
        description="Required",
    )

    model_config = {"populate_by_name": True}

"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7.1
Class: MFN_Znn.MF_SITE_DEFINED
Type: Group
"""
from __future__ import annotations

from typing import Any
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.MFE import MFE

_MFE = MFE


class MFN_Znn_MF_SITE_DEFINED(HL7Model):
    """HL7 v2 MFN_Znn.MF_SITE_DEFINED group.

    Attributes:
        MFE (MFE): required
        anyhl7segment (Any): required
    """

    MFE: _MFE = Field(
        title="MFE",
        description="Required",
    )

    anyhl7segment: Any

    model_config = {"populate_by_name": True}

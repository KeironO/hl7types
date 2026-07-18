"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5.1
Class: MFR_M01.MF_QUERY
Type: Group
"""
from __future__ import annotations

from typing import Any
from pydantic import ConfigDict, Field
from hl7types.hl7 import HL7Model

from ..segments.MFE import MFE

_MFE = MFE


class MFR_M01_MF_QUERY(HL7Model):
    """HL7 v2 MFR_M01.MF_QUERY group.

    Attributes:
        MFE (MFE): Master File Entry, required
        anyhl7segment (Any): required
    """

    MFE: _MFE = Field(
        title="MFE",
        description="Master File Entry",
    )

    anyhl7segment: Any

    model_config = ConfigDict(populate_by_name=True)

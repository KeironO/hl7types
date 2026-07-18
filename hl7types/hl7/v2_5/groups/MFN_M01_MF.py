"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5
Class: MFN_M01.MF
Type: Group
"""
from __future__ import annotations

from typing import Optional, Any
from pydantic import ConfigDict, Field
from hl7types.hl7 import HL7Model

from ..segments.MFE import MFE

_MFE = MFE


class MFN_M01_MF(HL7Model):
    """HL7 v2 MFN_M01.MF group.

    Attributes:
        MFE (MFE): Master File Entry, required
        anyhl7segment (Optional[Any]): optional
    """

    MFE: _MFE = Field(
        title="MFE",
        description="Master File Entry",
    )

    anyhl7segment: Optional[Any] = None

    model_config = ConfigDict(populate_by_name=True)

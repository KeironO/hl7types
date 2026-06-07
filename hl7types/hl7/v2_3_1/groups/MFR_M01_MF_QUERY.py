"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3.1
Class: MFR_M01.MF_QUERY
Type: Group
"""
from __future__ import annotations

from typing import Optional, Any
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.MFE import MFE

_MFE = MFE


class MFR_M01_MF_QUERY(HL7Model):
    """HL7 v2 MFR_M01.MF_QUERY group.

    Attributes:
        MFE (MFE): required
        anyzsegment (Optional[Any]): optional
    """

    MFE: _MFE = Field(
        title="MFE",
        description="Required",
    )

    anyzsegment: Optional[Any] = None

    model_config = {"populate_by_name": True}

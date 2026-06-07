"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.2
Class: MFN_M03.MF_TEST
Type: Group
"""
from __future__ import annotations

from typing import Optional, Any
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.MFE import MFE

_MFE = MFE


class MFN_M03_MF_TEST(HL7Model):
    """HL7 v2 MFN_M03.MF_TEST group.

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

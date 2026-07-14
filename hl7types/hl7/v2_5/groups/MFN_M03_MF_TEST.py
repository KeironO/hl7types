"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5
Class: MFN_M03.MF_TEST
Type: Group
"""
from __future__ import annotations

from typing import Any
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.MFE import MFE
from ..segments.OM1 import OM1

_MFE = MFE
_OM1 = OM1


class MFN_M03_MF_TEST(HL7Model):
    """HL7 v2 MFN_M03.MF_TEST group.

    Attributes:
        MFE (MFE): Master File Entry, required
        OM1 (OM1): General Segment, required
        anyhl7segment (Any): required
    """

    MFE: _MFE = Field(
        title="MFE",
        description="Master File Entry",
    )

    OM1: _OM1 = Field(
        title="OM1",
        description="General Segment",
    )

    anyhl7segment: Any

    model_config = {"populate_by_name": True}

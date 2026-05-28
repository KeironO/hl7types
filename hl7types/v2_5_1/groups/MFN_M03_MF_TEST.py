"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5.1
Class: MFN_M03.MF_TEST
Type: Group
"""
from _future__ import annotations

from typing import Optional, Any
from pydantic import BaseModel, Field

from ..segments.MFE import MFE
from ..segments.OM1 import OM1

_MFE = MFE
_OM1 = OM1


class MFN_M03_MF_TEST(BaseModel):
    """HL7 v2 MFN_M03.MF_TEST group.

    Attributes:
        MFE (MFE): required
        OM1 (OM1): required
        anyhl7segment (Any): required
    """

    MFE: _MFE = Field(
        default=...,
        title="MFE",
        description="Required",
    )

    OM1: _OM1 = Field(
        default=...,
        title="OM1",
        description="Required",
    )

    anyhl7segment: Any

    model_config = {"populate_by_name": True}

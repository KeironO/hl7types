"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3.1
Class: MFN_M08.MF_TEST_NUMERIC
Type: Group
"""
from __future__ import annotations

from typing import Optional
from pydantic import BaseModel, Field

from ..segments.MFE import MFE
from ..segments.OM1 import OM1

from .MFN_M08_MF_NUMERIC_OBSERVATION import MFN_M08_MF_NUMERIC_OBSERVATION

_MFE = MFE
_MFN_M08_MF_NUMERIC_OBSERVATION = MFN_M08_MF_NUMERIC_OBSERVATION
_OM1 = OM1


class MFN_M08_MF_TEST_NUMERIC(BaseModel):
    """HL7 v2 MFN_M08.MF_TEST_NUMERIC group.

    Attributes:
        MFE (MFE): required
        OM1 (Optional[OM1]): optional
        MF_NUMERIC_OBSERVATION (Optional[MFN_M08_MF_NUMERIC_OBSERVATION]): optional
    """

    MFE: _MFE = Field(
        default=...,
        title="MFE",
        description="Required",
    )

    OM1: Optional[_OM1] = Field(
        default=None,
        title="OM1",
        description="Optional",
    )

    MF_NUMERIC_OBSERVATION: Optional[_MFN_M08_MF_NUMERIC_OBSERVATION] = Field(
        default=None,
        title="MF_NUMERIC_OBSERVATION",
        description="Optional",
    )

    model_config = {"populate_by_name": True}

"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5
Class: MFN_M10.MF_TEST_BATTERIES
Type: Group
"""
from _future__ import annotations

from typing import Optional
from pydantic import BaseModel, Field

from ..segments.MFE import MFE
from ..segments.OM1 import OM1

from .MFN_M10_MF_TEST_BATT_DETAIL import MFN_M10_MF_TEST_BATT_DETAIL

_MFE = MFE
_MFN_M10_MF_TEST_BATT_DETAIL = MFN_M10_MF_TEST_BATT_DETAIL
_OM1 = OM1


class MFN_M10_MF_TEST_BATTERIES(BaseModel):
    """HL7 v2 MFN_M10.MF_TEST_BATTERIES group.

    Attributes:
        MFE (MFE): required
        OM1 (OM1): required
        MF_TEST_BATT_DETAIL (Optional[MFN_M10_MF_TEST_BATT_DETAIL]): optional
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

    MF_TEST_BATT_DETAIL: Optional[_MFN_M10_MF_TEST_BATT_DETAIL] = Field(
        default=None,
        title="MF_TEST_BATT_DETAIL",
        description="Optional",
    )

    model_config = {"populate_by_name": True}

"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.2
Class: MFN_M10.MF_TEST_BATTERIES
Type: Group
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..segments.MFE import MFE
from ..segments.OM1 import OM1
from ..segments.OMC import OMC
from ..segments.PRT import PRT
from .MFN_M10_MF_TEST_BATT_DETAIL import MFN_M10_MF_TEST_BATT_DETAIL

_MFE = MFE
_MFN_M10_MF_TEST_BATT_DETAIL = MFN_M10_MF_TEST_BATT_DETAIL
_OM1 = OM1
_OMC = OMC
_PRT = PRT


class MFN_M10_MF_TEST_BATTERIES(BaseModel):
    """HL7 v2 MFN_M10.MF_TEST_BATTERIES group.

    Attributes:
        MFE (MFE): required
        OM1 (OM1): required
        OMC (Optional[List[OMC]]): optional
        PRT (Optional[List[PRT]]): optional
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

    OMC: list[_OMC] | None = Field(
        default=None,
        title="OMC",
        description="Optional, repeating",
    )

    PRT: list[_PRT] | None = Field(
        default=None,
        title="PRT",
        description="Optional, repeating",
    )

    MF_TEST_BATT_DETAIL: _MFN_M10_MF_TEST_BATT_DETAIL | None = Field(
        default=None,
        title="MF_TEST_BATT_DETAIL",
        description="Optional",
    )

    model_config = {"populate_by_name": True}

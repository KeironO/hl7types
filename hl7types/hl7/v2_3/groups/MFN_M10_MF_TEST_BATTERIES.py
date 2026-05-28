"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3
Class: MFN_M10.MF_TEST_BATTERIES
Type: Group
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from .MFN_M10_MF_TEST_BATT_DETAIL import MFN_M10_MF_TEST_BATT_DETAIL

_MFN_M10_MF_TEST_BATT_DETAIL = MFN_M10_MF_TEST_BATT_DETAIL


class MFN_M10_MF_TEST_BATTERIES(BaseModel):
    """HL7 v2 MFN_M10.MF_TEST_BATTERIES group.

    Attributes:
        MF_TEST_BATT_DETAIL (Optional[MFN_M10_MF_TEST_BATT_DETAIL]): optional
    """

    MF_TEST_BATT_DETAIL: _MFN_M10_MF_TEST_BATT_DETAIL | None = Field(
        default=None,
        title="MF_TEST_BATT_DETAIL",
        description="Optional",
    )

    model_config = {"populate_by_name": True}

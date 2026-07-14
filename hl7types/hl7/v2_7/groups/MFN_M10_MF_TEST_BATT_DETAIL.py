"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7
Class: MFN_M10.MF_TEST_BATT_DETAIL
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.OM4 import OM4
from ..segments.OM5 import OM5

_OM4 = OM4
_OM5 = OM5


class MFN_M10_MF_TEST_BATT_DETAIL(HL7Model):
    """HL7 v2 MFN_M10.MF_TEST_BATT_DETAIL group.

    Attributes:
        OM5 (OM5): Observation Batteries (Sets), required
        OM4 (Optional[List[OM4]]): Observations that Require Specimens, optional
    """

    OM5: _OM5 = Field(
        title="OM5",
        description="Observation Batteries (Sets)",
    )

    OM4: Optional[List[_OM4]] = Field(
        default=None,
        title="OM4",
        description="Observations that Require Specimens",
    )

    model_config = {"populate_by_name": True}

"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.1
Class: MFN_M11.MF_TEST_CALC_DETAIL
Type: Group
"""
from __future__ import annotations

from pydantic import ConfigDict, Field
from hl7types.hl7 import HL7Model

from ..segments.OM2 import OM2
from ..segments.OM6 import OM6

_OM2 = OM2
_OM6 = OM6


class MFN_M11_MF_TEST_CALC_DETAIL(HL7Model):
    """HL7 v2 MFN_M11.MF_TEST_CALC_DETAIL group.

    Attributes:
        OM6 (OM6): Observations that are Calculated from Other Observations, required
        OM2 (OM2): Numeric Observation, required
    """

    OM6: _OM6 = Field(
        title="OM6",
        description="Observations that are Calculated from Other Observations",
    )

    OM2: _OM2 = Field(
        title="OM2",
        description="Numeric Observation",
    )

    model_config = ConfigDict(populate_by_name=True)

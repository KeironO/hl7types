"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.4
Class: MFN_M11.MF_TEST_CALC_DETAIL
Type: Group
"""
from __future__ import annotations

from typing import Optional
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.OM2 import OM2
from ..segments.OM6 import OM6

_OM2 = OM2
_OM6 = OM6


class MFN_M11_MF_TEST_CALC_DETAIL(HL7Model):
    """HL7 v2 MFN_M11.MF_TEST_CALC_DETAIL group.

    Attributes:
        OM6 (OM6): required
        OM2 (OM2): required
    """

    OM6: _OM6 = Field(
        default=...,
        title="OM6",
        description="Required",
    )

    OM2: _OM2 = Field(
        default=...,
        title="OM2",
        description="Required",
    )

    model_config = {"populate_by_name": True}

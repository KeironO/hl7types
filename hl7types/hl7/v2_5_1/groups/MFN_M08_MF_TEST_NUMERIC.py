"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5.1
Class: MFN_M08.MF_TEST_NUMERIC
Type: Group
"""
from __future__ import annotations

from typing import Optional
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.MFE import MFE
from ..segments.OM1 import OM1
from ..segments.OM2 import OM2
from ..segments.OM3 import OM3
from ..segments.OM4 import OM4

_MFE = MFE
_OM1 = OM1
_OM2 = OM2
_OM3 = OM3
_OM4 = OM4


class MFN_M08_MF_TEST_NUMERIC(HL7Model):
    """HL7 v2 MFN_M08.MF_TEST_NUMERIC group.

    Attributes:
        MFE (MFE): Master File Entry, required
        OM1 (OM1): General Segment, required
        OM2 (Optional[OM2]): Numeric Observation, optional
        OM3 (Optional[OM3]): Categorical Service/Test/Observation, optional
        OM4 (Optional[OM4]): Observations that Require Specimens, optional
    """

    MFE: _MFE = Field(
        title="MFE",
        description="Master File Entry",
    )

    OM1: _OM1 = Field(
        title="OM1",
        description="General Segment",
    )

    OM2: Optional[_OM2] = Field(
        default=None,
        title="OM2",
        description="Numeric Observation",
    )

    OM3: Optional[_OM3] = Field(
        default=None,
        title="OM3",
        description="Categorical Service/Test/Observation",
    )

    OM4: Optional[_OM4] = Field(
        default=None,
        title="OM4",
        description="Observations that Require Specimens",
    )

    model_config = {"populate_by_name": True}

"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5
Class: MFN_M08.MF_TEST_NUMERIC
Type: Group
"""

from __future__ import annotations

from pydantic import BaseModel, Field

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


class MFN_M08_MF_TEST_NUMERIC(BaseModel):
    """HL7 v2 MFN_M08.MF_TEST_NUMERIC group.

    Attributes:
        MFE (MFE): required
        OM1 (OM1): required
        OM2 (Optional[OM2]): optional
        OM3 (Optional[OM3]): optional
        OM4 (Optional[OM4]): optional
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

    OM2: _OM2 | None = Field(
        default=None,
        title="OM2",
        description="Optional",
    )

    OM3: _OM3 | None = Field(
        default=None,
        title="OM3",
        description="Optional",
    )

    OM4: _OM4 | None = Field(
        default=None,
        title="OM4",
        description="Optional",
    )

    model_config = {"populate_by_name": True}

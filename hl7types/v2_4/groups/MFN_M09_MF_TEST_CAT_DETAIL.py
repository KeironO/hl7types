"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.4
Class: MFN_M09.MF_TEST_CAT_DETAIL
Type: Group
"""
from _future__ import annotations

from typing import Optional, List
from pydantic import BaseModel, Field

from ..segments.OM3 import OM3
from ..segments.OM4 import OM4

_OM3 = OM3
_OM4 = OM4


class MFN_M09_MF_TEST_CAT_DETAIL(BaseModel):
    """HL7 v2 MFN_M09.MF_TEST_CAT_DETAIL group.

    Attributes:
        OM3 (OM3): required
        OM4 (Optional[List[OM4]]): optional
    """

    OM3: _OM3 = Field(
        default=...,
        title="OM3",
        description="Required",
    )

    OM4: Optional[List[_OM4]] = Field(
        default=None,
        title="OM4",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}

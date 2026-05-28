"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.2
Class: DPR_O48.DONATION
Type: Group
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..segments.DON import DON
from ..segments.NTE import NTE
from ..segments.OBX import OBX
from .DPR_O48_BLOOD_UNIT import DPR_O48_BLOOD_UNIT

_DON = DON
_DPR_O48_BLOOD_UNIT = DPR_O48_BLOOD_UNIT
_NTE = NTE
_OBX = OBX


class DPR_O48_DONATION(BaseModel):
    """HL7 v2 DPR_O48.DONATION group.

    Attributes:
        DON (DON): required
        OBX (Optional[List[OBX]]): optional
        NTE (Optional[List[NTE]]): optional
        BLOOD_UNIT (Optional[DPR_O48_BLOOD_UNIT]): optional
    """

    DON: _DON = Field(
        default=...,
        title="DON",
        description="Required",
    )

    OBX: list[_OBX] | None = Field(
        default=None,
        title="OBX",
        description="Optional, repeating",
    )

    NTE: list[_NTE] | None = Field(
        default=None,
        title="NTE",
        description="Optional, repeating",
    )

    BLOOD_UNIT: _DPR_O48_BLOOD_UNIT | None = Field(
        default=None,
        title="BLOOD_UNIT",
        description="Optional",
    )

    model_config = {"populate_by_name": True}

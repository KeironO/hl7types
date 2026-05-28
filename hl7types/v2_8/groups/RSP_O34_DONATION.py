"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8
Class: RSP_O34.DONATION
Type: Group
"""
from _future__ import annotations

from typing import Optional, List
from pydantic import BaseModel, Field

from ..segments.DON import DON
from ..segments.NTE import NTE
from ..segments.OBX import OBX

_DON = DON
_NTE = NTE
_OBX = OBX


class RSP_O34_DONATION(BaseModel):
    """HL7 v2 RSP_O34.DONATION group.

    Attributes:
        DON (DON): required
        OBX (Optional[List[OBX]]): optional
        NTE (Optional[List[NTE]]): optional
    """

    DON: _DON = Field(
        default=...,
        title="DON",
        description="Required",
    )

    OBX: Optional[List[_OBX]] = Field(
        default=None,
        title="OBX",
        description="Optional, repeating",
    )

    NTE: Optional[List[_NTE]] = Field(
        default=None,
        title="NTE",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}

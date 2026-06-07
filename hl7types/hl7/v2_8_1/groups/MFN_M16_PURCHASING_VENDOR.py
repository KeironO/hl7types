"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.1
Class: MFN_M16.PURCHASING_VENDOR
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.VND import VND

from .MFN_M16_PACKAGING import MFN_M16_PACKAGING

_MFN_M16_PACKAGING = MFN_M16_PACKAGING
_VND = VND


class MFN_M16_PURCHASING_VENDOR(HL7Model):
    """HL7 v2 MFN_M16.PURCHASING_VENDOR group.

    Attributes:
        VND (VND): required
        PACKAGING (Optional[List[MFN_M16_PACKAGING]]): optional
    """

    VND: _VND = Field(
        title="VND",
        description="Required",
    )

    PACKAGING: Optional[List[_MFN_M16_PACKAGING]] = Field(
        default=None,
        title="PACKAGING",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}

"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7
Class: SDR_S32.ANTI-MICROBIAL_DEVICE_CYCLE_DATA
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.SCD import SCD
from ..segments.SDD import SDD

_SCD = SCD
_SDD = SDD


class SDR_S32_ANTI_MICROBIAL_DEVICE_CYCLE_DATA(HL7Model):
    """HL7 v2 SDR_S32.ANTI-MICROBIAL_DEVICE_CYCLE_DATA group.

    Attributes:
        SDD (Optional[SDD]): optional
        SCD (Optional[List[SCD]]): optional
    """

    SDD: Optional[_SDD] = Field(
        default=None,
        title="SDD",
        description="Optional",
    )

    SCD: Optional[List[_SCD]] = Field(
        default=None,
        title="SCD",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}

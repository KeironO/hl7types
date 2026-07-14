"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.6
Class: SDR_S31.ANTIMICROBIAL_DEVICE_DATA
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


class SDR_S31_ANTIMICROBIAL_DEVICE_DATA(HL7Model):
    """HL7 v2 SDR_S31.ANTIMICROBIAL_DEVICE_DATA group.

    Attributes:
        SDD (Optional[SDD]): Sterilization Device Data, optional
        SCD (Optional[List[SCD]]): Anti-Microbial Cycle Data, optional
    """

    SDD: Optional[_SDD] = Field(
        default=None,
        title="SDD",
        description="Sterilization Device Data",
    )

    SCD: Optional[List[_SCD]] = Field(
        default=None,
        title="SCD",
        description="Anti-Microbial Cycle Data",
    )

    model_config = {"populate_by_name": True}

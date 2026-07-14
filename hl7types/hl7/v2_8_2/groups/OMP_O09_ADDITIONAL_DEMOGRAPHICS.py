"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.2
Class: OMP_O09.ADDITIONAL_DEMOGRAPHICS
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.PD1 import PD1
from ..segments.PRT import PRT

_PD1 = PD1
_PRT = PRT


class OMP_O09_ADDITIONAL_DEMOGRAPHICS(HL7Model):
    """HL7 v2 OMP_O09.ADDITIONAL_DEMOGRAPHICS group.

    Attributes:
        PD1 (PD1): Patient Additional Demographic, required
        PRT (Optional[List[PRT]]): Participation Information, optional
    """

    PD1: _PD1 = Field(
        title="PD1",
        description="Patient Additional Demographic",
    )

    PRT: Optional[List[_PRT]] = Field(
        default=None,
        title="PRT",
        description="Participation Information",
    )

    model_config = {"populate_by_name": True}

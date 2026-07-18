"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.1
Class: RDS_O13.ADDITIONAL_DEMOGRAPHICS
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import ConfigDict, Field
from hl7types.hl7 import HL7Model

from ..segments.ARV import ARV
from ..segments.PD1 import PD1
from ..segments.PRT import PRT

_ARV = ARV
_PD1 = PD1
_PRT = PRT


class RDS_O13_ADDITIONAL_DEMOGRAPHICS(HL7Model):
    """HL7 v2 RDS_O13.ADDITIONAL_DEMOGRAPHICS group.

    Attributes:
        PD1 (PD1): Patient Additional Demographic, required
        PRT (Optional[List[PRT]]): Participation Information, optional
        ARV (Optional[List[ARV]]): Access Restriction, optional
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

    ARV: Optional[List[_ARV]] = Field(
        default=None,
        title="ARV",
        description="Access Restriction",
    )

    model_config = ConfigDict(populate_by_name=True)

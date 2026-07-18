"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.4
Class: PRR_PC5.CHOICE
Type: Group
"""
from __future__ import annotations

from typing import Optional
from pydantic import ConfigDict, Field
from hl7types.hl7 import HL7Model

from ..segments.OBR import OBR
from ..segments.RXO import RXO

_OBR = OBR
_RXO = RXO


class PRR_PC5_CHOICE(HL7Model):
    """HL7 v2 PRR_PC5.CHOICE group.

    Attributes:
        OBR (Optional[OBR]): Observation Request, optional
        RXO (Optional[RXO]): Pharmacy/Treatment Order, optional
    """

    OBR: Optional[_OBR] = Field(
        default=None,
        title="OBR",
        description="Observation Request",
    )

    RXO: Optional[_RXO] = Field(
        default=None,
        title="RXO",
        description="Pharmacy/Treatment Order",
    )

    model_config = ConfigDict(populate_by_name=True)

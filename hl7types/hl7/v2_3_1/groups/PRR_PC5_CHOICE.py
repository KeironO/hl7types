"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3.1
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
        OBR (Optional[OBR]): OBR - observation request segment, optional
        RXO (Optional[RXO]): RXO - pharmacy/treatment order segment, optional
    """

    OBR: Optional[_OBR] = Field(
        default=None,
        title="OBR",
        description="OBR - observation request segment",
    )

    RXO: Optional[_RXO] = Field(
        default=None,
        title="RXO",
        description="RXO - pharmacy/treatment order segment",
    )

    model_config = ConfigDict(populate_by_name=True)

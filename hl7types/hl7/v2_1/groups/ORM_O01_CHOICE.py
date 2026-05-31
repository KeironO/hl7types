"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.1
Class: ORM_O01.CHOICE
Type: Group
"""
from __future__ import annotations

from typing import Optional
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.OBR import OBR
from ..segments.ORO import ORO
from ..segments.RX1 import RX1

_OBR = OBR
_ORO = ORO
_RX1 = RX1


class ORM_O01_CHOICE(HL7Model):
    """HL7 v2 ORM_O01.CHOICE group.

    Attributes:
        OBR (Optional[OBR]): optional
        ORO (Optional[ORO]): optional
        RX1 (Optional[RX1]): optional
    """

    OBR: Optional[_OBR] = Field(
        default=None,
        title="OBR",
        description="Optional",
    )

    ORO: Optional[_ORO] = Field(
        default=None,
        title="ORO",
        description="Optional",
    )

    RX1: Optional[_RX1] = Field(
        default=None,
        title="RX1",
        description="Optional",
    )

    model_config = {"populate_by_name": True}

"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.4
Class: OSR_Q06.CHOICE
Type: Group
"""
from __future__ import annotations

from typing import Optional
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.OBR import OBR
from ..segments.ODS import ODS
from ..segments.ODT import ODT
from ..segments.RQ1 import RQ1
from ..segments.RQD import RQD
from ..segments.RXO import RXO

_OBR = OBR
_ODS = ODS
_ODT = ODT
_RQ1 = RQ1
_RQD = RQD
_RXO = RXO


class OSR_Q06_CHOICE(HL7Model):
    """HL7 v2 OSR_Q06.CHOICE group.

    Attributes:
        OBR (Optional[OBR]): optional
        RQD (Optional[RQD]): optional
        RQ1 (Optional[RQ1]): optional
        RXO (Optional[RXO]): optional
        ODS (Optional[ODS]): optional
        ODT (Optional[ODT]): optional
    """

    OBR: Optional[_OBR] = Field(
        default=None,
        title="OBR",
        description="Optional",
    )

    RQD: Optional[_RQD] = Field(
        default=None,
        title="RQD",
        description="Optional",
    )

    RQ1: Optional[_RQ1] = Field(
        default=None,
        title="RQ1",
        description="Optional",
    )

    RXO: Optional[_RXO] = Field(
        default=None,
        title="RXO",
        description="Optional",
    )

    ODS: Optional[_ODS] = Field(
        default=None,
        title="ODS",
        description="Optional",
    )

    ODT: Optional[_ODT] = Field(
        default=None,
        title="ODT",
        description="Optional",
    )

    model_config = {"populate_by_name": True}

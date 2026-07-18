"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3
Class: ORR_O02.CHOICE
Type: Group
"""
from __future__ import annotations

from typing import Optional
from pydantic import ConfigDict, Field
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


class ORR_O02_CHOICE(HL7Model):
    """HL7 v2 ORR_O02.CHOICE group.

    Attributes:
        OBR (Optional[OBR]): Observation request segment, optional
        RQD (Optional[RQD]): Requisition detail, optional
        RQ1 (Optional[RQ1]): Requisition detail-1 segment, optional
        RXO (Optional[RXO]): Pharmacy prescription order segment, optional
        ODS (Optional[ODS]): Dietary orders, supplements, and preferences, optional
        ODT (Optional[ODT]): Diet tray instructions segment, optional
    """

    OBR: Optional[_OBR] = Field(
        default=None,
        title="OBR",
        description="Observation request segment",
    )

    RQD: Optional[_RQD] = Field(
        default=None,
        title="RQD",
        description="Requisition detail",
    )

    RQ1: Optional[_RQ1] = Field(
        default=None,
        title="RQ1",
        description="Requisition detail-1 segment",
    )

    RXO: Optional[_RXO] = Field(
        default=None,
        title="RXO",
        description="Pharmacy prescription order segment",
    )

    ODS: Optional[_ODS] = Field(
        default=None,
        title="ODS",
        description="Dietary orders, supplements, and preferences",
    )

    ODT: Optional[_ODT] = Field(
        default=None,
        title="ODT",
        description="Diet tray instructions segment",
    )

    model_config = ConfigDict(populate_by_name=True)

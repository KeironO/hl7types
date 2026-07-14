"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.2
Class: ORR_O02.CHOICE
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


class ORR_O02_CHOICE(HL7Model):
    """HL7 v2 ORR_O02.CHOICE group.

    Attributes:
        OBR (Optional[OBR]): OBSERVATION REQUEST, optional
        RQD (Optional[RQD]): REQUISITION DETAIL, optional
        RQ1 (Optional[RQ1]): REQUISITION DETAIL-!, optional
        RXO (Optional[RXO]): PHARMACY PRESCRIPTION ORDER, optional
        ODS (Optional[ODS]): DIETARY ORDERS, SUPPLEMENTS, and PREFERENCES, optional
        ODT (Optional[ODT]): DIET TRAY INSTRUCTION, optional
    """

    OBR: Optional[_OBR] = Field(
        default=None,
        title="OBR",
        description="OBSERVATION REQUEST",
    )

    RQD: Optional[_RQD] = Field(
        default=None,
        title="RQD",
        description="REQUISITION DETAIL",
    )

    RQ1: Optional[_RQ1] = Field(
        default=None,
        title="RQ1",
        description="REQUISITION DETAIL-!",
    )

    RXO: Optional[_RXO] = Field(
        default=None,
        title="RXO",
        description="PHARMACY PRESCRIPTION ORDER",
    )

    ODS: Optional[_ODS] = Field(
        default=None,
        title="ODS",
        description="DIETARY ORDERS, SUPPLEMENTS, and PREFERENCES",
    )

    ODT: Optional[_ODT] = Field(
        default=None,
        title="ODT",
        description="DIET TRAY INSTRUCTION",
    )

    model_config = {"populate_by_name": True}

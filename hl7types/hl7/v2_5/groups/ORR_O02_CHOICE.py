"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5
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
        OBR (Optional[OBR]): Observation Request, optional
        RQD (Optional[RQD]): Requisition Detail, optional
        RQ1 (Optional[RQ1]): Requisition Detail-1, optional
        RXO (Optional[RXO]): Pharmacy/Treatment Order, optional
        ODS (Optional[ODS]): Dietary Orders, Supplements, and Preferences, optional
        ODT (Optional[ODT]): Diet Tray Instructions, optional
    """

    OBR: Optional[_OBR] = Field(
        default=None,
        title="OBR",
        description="Observation Request",
    )

    RQD: Optional[_RQD] = Field(
        default=None,
        title="RQD",
        description="Requisition Detail",
    )

    RQ1: Optional[_RQ1] = Field(
        default=None,
        title="RQ1",
        description="Requisition Detail-1",
    )

    RXO: Optional[_RXO] = Field(
        default=None,
        title="RXO",
        description="Pharmacy/Treatment Order",
    )

    ODS: Optional[_ODS] = Field(
        default=None,
        title="ODS",
        description="Dietary Orders, Supplements, and Preferences",
    )

    ODT: Optional[_ODT] = Field(
        default=None,
        title="ODT",
        description="Diet Tray Instructions",
    )

    model_config = ConfigDict(populate_by_name=True)

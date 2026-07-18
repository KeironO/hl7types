"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.1
Class: CCR_I16.CLINICAL_ORDER_OBJECT
Type: Group
"""
from __future__ import annotations

from typing import Optional
from pydantic import ConfigDict, Field
from hl7types.hl7 import HL7Model

from ..segments.OBR import OBR
from ..segments.ODS import ODS
from ..segments.PR1 import PR1
from ..segments.RXO import RXO

_OBR = OBR
_ODS = ODS
_PR1 = PR1
_RXO = RXO


class CCR_I16_CLINICAL_ORDER_OBJECT(HL7Model):
    """HL7 v2 CCR_I16.CLINICAL_ORDER_OBJECT group.

    Attributes:
        OBR (Optional[OBR]): Observation Request, optional
        RXO (Optional[RXO]): Pharmacy/Treatment Order, optional
        ODS (Optional[ODS]): Dietary Orders, Supplements, and Preferences, optional
        PR1 (Optional[PR1]): Procedures, optional
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

    ODS: Optional[_ODS] = Field(
        default=None,
        title="ODS",
        description="Dietary Orders, Supplements, and Preferences",
    )

    PR1: Optional[_PR1] = Field(
        default=None,
        title="PR1",
        description="Procedures",
    )

    model_config = ConfigDict(populate_by_name=True)

"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8
Class: RRD_O14.RESPONSE
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from .RRD_O14_ORDER import RRD_O14_ORDER
from .RRD_O14_PATIENT import RRD_O14_PATIENT

_RRD_O14_ORDER = RRD_O14_ORDER
_RRD_O14_PATIENT = RRD_O14_PATIENT


class RRD_O14_RESPONSE(HL7Model):
    """HL7 v2 RRD_O14.RESPONSE group.

    Attributes:
        PATIENT (Optional[RRD_O14_PATIENT]): optional
        ORDER (List[RRD_O14_ORDER]): required
    """

    PATIENT: Optional[_RRD_O14_PATIENT] = Field(
        default=None,
        title="PATIENT",
        description="Optional",
    )

    ORDER: List[_RRD_O14_ORDER] = Field(
        min_length=1,
        title="ORDER",
        description="Required, repeating",
    )

    model_config = {"populate_by_name": True}

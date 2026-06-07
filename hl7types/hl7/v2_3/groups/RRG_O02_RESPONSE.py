"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3
Class: RRG_O02.RESPONSE
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from .RRG_O02_ORDER import RRG_O02_ORDER
from .RRG_O02_PATIENT import RRG_O02_PATIENT

_RRG_O02_ORDER = RRG_O02_ORDER
_RRG_O02_PATIENT = RRG_O02_PATIENT


class RRG_O02_RESPONSE(HL7Model):
    """HL7 v2 RRG_O02.RESPONSE group.

    Attributes:
        PATIENT (Optional[RRG_O02_PATIENT]): optional
        ORDER (List[RRG_O02_ORDER]): required
    """

    PATIENT: Optional[_RRG_O02_PATIENT] = Field(
        default=None,
        title="PATIENT",
        description="Optional",
    )

    ORDER: List[_RRG_O02_ORDER] = Field(
        min_length=1,
        title="ORDER",
        description="Required, repeating",
    )

    model_config = {"populate_by_name": True}

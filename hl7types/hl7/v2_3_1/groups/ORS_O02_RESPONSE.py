"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3.1
Class: ORS_O02.RESPONSE
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from .ORS_O02_ORDER import ORS_O02_ORDER
from .ORS_O02_PATIENT import ORS_O02_PATIENT

_ORS_O02_ORDER = ORS_O02_ORDER
_ORS_O02_PATIENT = ORS_O02_PATIENT


class ORS_O02_RESPONSE(HL7Model):
    """HL7 v2 ORS_O02.RESPONSE group.

    Attributes:
        PATIENT (Optional[ORS_O02_PATIENT]): optional
        ORDER (List[ORS_O02_ORDER]): required
    """

    PATIENT: Optional[_ORS_O02_PATIENT] = Field(
        default=None,
        title="PATIENT",
        description="Optional",
    )

    ORDER: List[_ORS_O02_ORDER] = Field(
        min_length=1,
        title="ORDER",
        description="Required, repeating",
    )

    model_config = {"populate_by_name": True}

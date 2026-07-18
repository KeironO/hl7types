"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7.1
Class: ORS_O06.RESPONSE
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import ConfigDict, Field
from hl7types.hl7 import HL7Model

from .ORS_O06_ORDER import ORS_O06_ORDER
from .ORS_O06_PATIENT import ORS_O06_PATIENT

_ORS_O06_ORDER = ORS_O06_ORDER
_ORS_O06_PATIENT = ORS_O06_PATIENT


class ORS_O06_RESPONSE(HL7Model):
    """HL7 v2 ORS_O06.RESPONSE group.

    Attributes:
        PATIENT (Optional[ORS_O06_PATIENT]): optional
        ORDER (List[ORS_O06_ORDER]): required
    """

    PATIENT: Optional[_ORS_O06_PATIENT] = Field(
        default=None,
        title="PATIENT",
    )

    ORDER: List[_ORS_O06_ORDER] = Field(
        min_length=1,
        title="ORDER",
    )

    model_config = ConfigDict(populate_by_name=True)

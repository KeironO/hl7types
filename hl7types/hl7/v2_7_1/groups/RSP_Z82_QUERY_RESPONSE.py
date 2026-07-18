"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7.1
Class: RSP_Z82.QUERY_RESPONSE
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import ConfigDict, Field
from hl7types.hl7 import HL7Model

from .RSP_Z82_COMMON_ORDER import RSP_Z82_COMMON_ORDER
from .RSP_Z82_PATIENT import RSP_Z82_PATIENT

_RSP_Z82_COMMON_ORDER = RSP_Z82_COMMON_ORDER
_RSP_Z82_PATIENT = RSP_Z82_PATIENT


class RSP_Z82_QUERY_RESPONSE(HL7Model):
    """HL7 v2 RSP_Z82.QUERY_RESPONSE group.

    Attributes:
        PATIENT (Optional[RSP_Z82_PATIENT]): optional
        COMMON_ORDER (List[RSP_Z82_COMMON_ORDER]): required
    """

    PATIENT: Optional[_RSP_Z82_PATIENT] = Field(
        default=None,
        title="PATIENT",
    )

    COMMON_ORDER: List[_RSP_Z82_COMMON_ORDER] = Field(
        min_length=1,
        title="COMMON_ORDER",
    )

    model_config = ConfigDict(populate_by_name=True)

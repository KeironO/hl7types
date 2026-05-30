"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3.1
Class: ORF_R04.QUERY_RESPONSE
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from .ORF_R04_ORDER import ORF_R04_ORDER
from .ORF_R04_PATIENT import ORF_R04_PATIENT

_ORF_R04_ORDER = ORF_R04_ORDER
_ORF_R04_PATIENT = ORF_R04_PATIENT


class ORF_R04_QUERY_RESPONSE(HL7Model):
    """HL7 v2 ORF_R04.QUERY_RESPONSE group.

    Attributes:
        PATIENT (Optional[ORF_R04_PATIENT]): optional
        ORDER (List[ORF_R04_ORDER]): required
    """

    PATIENT: Optional[_ORF_R04_PATIENT] = Field(
        default=None,
        title="PATIENT",
        description="Optional",
    )

    ORDER: List[_ORF_R04_ORDER] = Field(
        default=...,
        title="ORDER",
        description="Required, repeating",
    )

    model_config = {"populate_by_name": True}

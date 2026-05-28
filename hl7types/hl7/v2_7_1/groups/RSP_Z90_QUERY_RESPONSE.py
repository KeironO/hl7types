"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7.1
Class: RSP_Z90.QUERY_RESPONSE
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import BaseModel, Field

from .RSP_Z90_COMMON_ORDER import RSP_Z90_COMMON_ORDER
from .RSP_Z90_PATIENT import RSP_Z90_PATIENT
from .RSP_Z90_SPECIMEN import RSP_Z90_SPECIMEN

_RSP_Z90_COMMON_ORDER = RSP_Z90_COMMON_ORDER
_RSP_Z90_PATIENT = RSP_Z90_PATIENT
_RSP_Z90_SPECIMEN = RSP_Z90_SPECIMEN


class RSP_Z90_QUERY_RESPONSE(BaseModel):
    """HL7 v2 RSP_Z90.QUERY_RESPONSE group.

    Attributes:
        PATIENT (Optional[RSP_Z90_PATIENT]): optional
        COMMON_ORDER (List[RSP_Z90_COMMON_ORDER]): required
        SPECIMEN (Optional[List[RSP_Z90_SPECIMEN]]): optional
    """

    PATIENT: Optional[_RSP_Z90_PATIENT] = Field(
        default=None,
        title="PATIENT",
        description="Optional",
    )

    COMMON_ORDER: List[_RSP_Z90_COMMON_ORDER] = Field(
        default=...,
        title="COMMON_ORDER",
        description="Required, repeating",
    )

    SPECIMEN: Optional[List[_RSP_Z90_SPECIMEN]] = Field(
        default=None,
        title="SPECIMEN",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}

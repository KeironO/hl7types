"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.6
Class: RRI_I12.PROCEDURE
Type: Group
"""
from _future__ import annotations

from typing import Optional
from pydantic import BaseModel, Field

from ..segments.PR1 import PR1

from .RRI_I12_AUTHORIZATION_CONTACT import RRI_I12_AUTHORIZATION_CONTACT

_PR1 = PR1
_RRI_I12_AUTHORIZATION_CONTACT = RRI_I12_AUTHORIZATION_CONTACT


class RRI_I12_PROCEDURE(BaseModel):
    """HL7 v2 RRI_I12.PROCEDURE group.

    Attributes:
        PR1 (PR1): required
        AUTHORIZATION_CONTACT (Optional[RRI_I12_AUTHORIZATION_CONTACT]): optional
    """

    PR1: _PR1 = Field(
        default=...,
        title="PR1",
        description="Required",
    )

    AUTHORIZATION_CONTACT: Optional[_RRI_I12_AUTHORIZATION_CONTACT] = Field(
        default=None,
        title="AUTHORIZATION_CONTACT",
        description="Optional",
    )

    model_config = {"populate_by_name": True}

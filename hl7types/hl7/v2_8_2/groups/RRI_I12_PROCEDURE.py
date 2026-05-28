"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.2
Class: RRI_I12.PROCEDURE
Type: Group
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..segments.PR1 import PR1
from .RRI_I12_AUTHORIZATION_CONTACT2 import RRI_I12_AUTHORIZATION_CONTACT2

_PR1 = PR1
_RRI_I12_AUTHORIZATION_CONTACT2 = RRI_I12_AUTHORIZATION_CONTACT2


class RRI_I12_PROCEDURE(BaseModel):
    """HL7 v2 RRI_I12.PROCEDURE group.

    Attributes:
        PR1 (PR1): required
        AUTHORIZATION_CONTACT2 (Optional[RRI_I12_AUTHORIZATION_CONTACT2]): optional
    """

    PR1: _PR1 = Field(
        default=...,
        title="PR1",
        description="Required",
    )

    AUTHORIZATION_CONTACT2: _RRI_I12_AUTHORIZATION_CONTACT2 | None = Field(
        default=None,
        title="AUTHORIZATION_CONTACT2",
        description="Optional",
    )

    model_config = {"populate_by_name": True}

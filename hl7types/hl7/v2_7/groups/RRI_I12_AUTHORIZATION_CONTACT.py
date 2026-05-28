"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7
Class: RRI_I12.AUTHORIZATION_CONTACT
Type: Group
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..segments.AUT import AUT
from ..segments.CTD import CTD

_AUT = AUT
_CTD = CTD


class RRI_I12_AUTHORIZATION_CONTACT(BaseModel):
    """HL7 v2 RRI_I12.AUTHORIZATION_CONTACT group.

    Attributes:
        AUT (AUT): required
        CTD (Optional[CTD]): optional
    """

    AUT: _AUT = Field(
        default=...,
        title="AUT",
        description="Required",
    )

    CTD: _CTD | None = Field(
        default=None,
        title="CTD",
        description="Optional",
    )

    model_config = {"populate_by_name": True}

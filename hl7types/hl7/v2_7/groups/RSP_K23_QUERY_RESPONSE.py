"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7
Class: RSP_K23.QUERY_RESPONSE
Type: Group
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..segments.PID import PID

_PID = PID


class RSP_K23_QUERY_RESPONSE(BaseModel):
    """HL7 v2 RSP_K23.QUERY_RESPONSE group.

    Attributes:
        PID (PID): required
    """

    PID: _PID = Field(
        default=...,
        title="PID",
        description="Required",
    )

    model_config = {"populate_by_name": True}

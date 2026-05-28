"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.6
Class: ED
Type: Segment
"""

from __future__ import annotations

from pydantic import BaseModel


class ED(BaseModel):
    """HL7 v2 ED segment."""

    pass

    model_config = {"populate_by_name": True}

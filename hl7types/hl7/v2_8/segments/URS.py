"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8
Class: URS
Type: Segment
"""

from __future__ import annotations

from pydantic import BaseModel


class URS(BaseModel):
    """HL7 v2 URS segment."""

    pass

    model_config = {"populate_by_name": True}

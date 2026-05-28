"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.1
Class: UB1
Type: Segment
"""

from __future__ import annotations

from pydantic import BaseModel


class UB1(BaseModel):
    """HL7 v2 UB1 segment."""

    pass

    model_config = {"populate_by_name": True}

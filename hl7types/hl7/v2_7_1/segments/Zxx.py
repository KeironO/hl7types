"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7.1
Class: Zxx
Type: Segment
"""

from __future__ import annotations

from pydantic import BaseModel


class Zxx(BaseModel):
    """HL7 v2 Zxx segment."""

    pass

    model_config = {"populate_by_name": True}

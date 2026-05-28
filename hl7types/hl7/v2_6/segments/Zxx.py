"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.6
Class: Zxx
Type: Segment
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, BaseModel, Field


class Zxx(BaseModel):
    """HL7 v2 Zxx segment."""

    pass

    model_config = {"populate_by_name": True}

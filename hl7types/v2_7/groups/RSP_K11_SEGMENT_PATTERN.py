"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7
Class: RSP_K11.SEGMENT_PATTERN
Type: Group
"""
from _future__ import annotations

from typing import Optional, Any
from pydantic import BaseModel, Field


class RSP_K11_SEGMENT_PATTERN(BaseModel):
    """HL7 v2 RSP_K11.SEGMENT_PATTERN group.

    Attributes:
        anyhl7segment (Any): required
    """

    anyhl7segment: Any

    model_config = {"populate_by_name": True}

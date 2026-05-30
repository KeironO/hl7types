"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.2
Class: RSP_K11.SEGMENT_PATTERN
Type: Group
"""
from __future__ import annotations

from typing import Optional, Any
from pydantic import Field
from hl7types.hl7 import HL7Model


class RSP_K11_SEGMENT_PATTERN(HL7Model):
    """HL7 v2 RSP_K11.SEGMENT_PATTERN group.

    Attributes:
        anyhl7segment (Any): required
    """

    anyhl7segment: Any

    model_config = {"populate_by_name": True}

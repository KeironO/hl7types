"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8
Class: ZL7
Type: Segment
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, Field
from hl7types.hl7 import HL7Model


class ZL7(HL7Model):
    """HL7 v2 ZL7 segment."""

    pass

    model_config = {"populate_by_name": True}

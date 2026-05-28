"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7.1
Class: QRF
Type: Segment
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, BaseModel, Field


class QRF(BaseModel):
    """HL7 v2 QRF segment."""

    pass

    model_config = {"populate_by_name": True}

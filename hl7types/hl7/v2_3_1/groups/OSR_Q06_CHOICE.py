"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3.1
Class: OSR_Q06.CHOICE
Type: Group
"""
from __future__ import annotations

from typing import Optional
from pydantic import BaseModel, Field


class OSR_Q06_CHOICE(BaseModel):
    """HL7 v2 OSR_Q06.CHOICE group."""

    pass

    model_config = {"populate_by_name": True}

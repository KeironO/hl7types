"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.6
Class: ORR_O02.CHOICE
Type: Group
"""
from __future__ import annotations

from typing import Optional
from pydantic import BaseModel, Field


class ORR_O02_CHOICE(BaseModel):
    """HL7 v2 ORR_O02.CHOICE group."""

    pass

    model_config = {"populate_by_name": True}

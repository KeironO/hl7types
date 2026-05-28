"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7
Class: PGL_PC6.CHOICE
Type: Group
"""
from _future__ import annotations

from typing import Optional
from pydantic import BaseModel, Field


class PGL_PC6_CHOICE(BaseModel):
    """HL7 v2 PGL_PC6.CHOICE group."""

    pass

    model_config = {"populate_by_name": True}

"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.1
Class: PGL_PC6.CHOICE
Type: Group
"""

from __future__ import annotations

from pydantic import BaseModel


class PGL_PC6_CHOICE(BaseModel):
    """HL7 v2 PGL_PC6.CHOICE group."""

    pass

    model_config = {"populate_by_name": True}

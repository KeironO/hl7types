"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7
Class: PRR_PC5.CHOICE
Type: Group
"""

from __future__ import annotations

from pydantic import BaseModel


class PRR_PC5_CHOICE(BaseModel):
    """HL7 v2 PRR_PC5.CHOICE group."""

    pass

    model_config = {"populate_by_name": True}

"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7.1
Class: PTR_PCF.CHOICE
Type: Group
"""

from __future__ import annotations

from pydantic import BaseModel


class PTR_PCF_CHOICE(BaseModel):
    """HL7 v2 PTR_PCF.CHOICE group."""

    pass

    model_config = {"populate_by_name": True}

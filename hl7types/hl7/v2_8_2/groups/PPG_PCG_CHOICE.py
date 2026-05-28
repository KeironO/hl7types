"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.2
Class: PPG_PCG.CHOICE
Type: Group
"""

from __future__ import annotations

from pydantic import BaseModel


class PPG_PCG_CHOICE(BaseModel):
    """HL7 v2 PPG_PCG.CHOICE group."""

    pass

    model_config = {"populate_by_name": True}

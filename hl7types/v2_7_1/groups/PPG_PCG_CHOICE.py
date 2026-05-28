"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7.1
Class: PPG_PCG.CHOICE
Type: Group
"""
from _future__ import annotations

from typing import Optional
from pydantic import BaseModel, Field


class PPG_PCG_CHOICE(BaseModel):
    """HL7 v2 PPG_PCG.CHOICE group."""

    pass

    model_config = {"populate_by_name": True}

"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7.1
Class: PPP_PCB.CHOICE
Type: Group
"""
from _future__ import annotations

from typing import Optional
from pydantic import BaseModel, Field


class PPP_PCB_CHOICE(BaseModel):
    """HL7 v2 PPP_PCB.CHOICE group."""

    pass

    model_config = {"populate_by_name": True}

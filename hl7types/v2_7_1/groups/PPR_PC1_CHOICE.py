"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7.1
Class: PPR_PC1.CHOICE
Type: Group
"""
from _future__ import annotations

from typing import Optional
from pydantic import BaseModel, Field


class PPR_PC1_CHOICE(BaseModel):
    """HL7 v2 PPR_PC1.CHOICE group."""

    pass

    model_config = {"populate_by_name": True}

"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.6
Class: PPR_PC1.CHOICE
Type: Group
"""

from __future__ import annotations

from pydantic import BaseModel


class PPR_PC1_CHOICE(BaseModel):
    """HL7 v2 PPR_PC1.CHOICE group."""

    pass

    model_config = {"populate_by_name": True}

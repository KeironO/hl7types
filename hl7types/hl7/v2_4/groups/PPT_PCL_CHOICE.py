"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.4
Class: PPT_PCL.CHOICE
Type: Group
"""

from __future__ import annotations

from pydantic import BaseModel


class PPT_PCL_CHOICE(BaseModel):
    """HL7 v2 PPT_PCL.CHOICE group."""

    pass

    model_config = {"populate_by_name": True}

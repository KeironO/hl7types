"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3.1
Class: TX
Type: Datatype
"""

from __future__ import annotations

from pydantic import BaseModel


class TX(BaseModel):
    """HL7 v2 TX data type."""

    pass

    model_config = {"populate_by_name": True}

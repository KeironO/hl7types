"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.2
Class: FT
Type: Datatype
"""

from __future__ import annotations

from pydantic import BaseModel


class FT(BaseModel):
    """HL7 v2 FT data type."""

    pass

    model_config = {"populate_by_name": True}

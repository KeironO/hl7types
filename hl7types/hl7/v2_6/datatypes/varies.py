"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.6
Class: varies
Type: Datatype
"""

from __future__ import annotations

from pydantic import BaseModel


class varies(BaseModel):
    """HL7 v2 varies data type."""

    pass

    model_config = {"populate_by_name": True}

"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.1
Class: varies
Type: Datatype
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, BaseModel, Field


class varies(BaseModel):
    """HL7 v2 varies data type."""

    pass

    model_config = {"populate_by_name": True}

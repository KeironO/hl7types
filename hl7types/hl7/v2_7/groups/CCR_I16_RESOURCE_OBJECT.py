"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7
Class: CCR_I16.RESOURCE_OBJECT
Type: Group
"""
from __future__ import annotations

from typing import Optional
from pydantic import BaseModel, Field


class CCR_I16_RESOURCE_OBJECT(BaseModel):
    """HL7 v2 CCR_I16.RESOURCE_OBJECT group."""

    pass

    model_config = {"populate_by_name": True}

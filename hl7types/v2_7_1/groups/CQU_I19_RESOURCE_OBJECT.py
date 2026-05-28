"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7.1
Class: CQU_I19.RESOURCE_OBJECT
Type: Group
"""
from _future__ import annotations

from typing import Optional
from pydantic import BaseModel, Field


class CQU_I19_RESOURCE_OBJECT(BaseModel):
    """HL7 v2 CQU_I19.RESOURCE_OBJECT group."""

    pass

    model_config = {"populate_by_name": True}

"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8
Class: CQU_I19.RESOURCE_OBJECT
Type: Group
"""

from __future__ import annotations

from pydantic import BaseModel


class CQU_I19_RESOURCE_OBJECT(BaseModel):
    """HL7 v2 CQU_I19.RESOURCE_OBJECT group."""

    pass

    model_config = {"populate_by_name": True}

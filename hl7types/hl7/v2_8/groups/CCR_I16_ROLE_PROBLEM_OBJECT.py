"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8
Class: CCR_I16.ROLE_PROBLEM_OBJECT
Type: Group
"""

from __future__ import annotations

from pydantic import BaseModel


class CCR_I16_ROLE_PROBLEM_OBJECT(BaseModel):
    """HL7 v2 CCR_I16.ROLE_PROBLEM_OBJECT group."""

    pass

    model_config = {"populate_by_name": True}

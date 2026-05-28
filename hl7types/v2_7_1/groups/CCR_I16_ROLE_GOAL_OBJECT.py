"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7.1
Class: CCR_I16.ROLE_GOAL_OBJECT
Type: Group
"""
from _future__ import annotations

from typing import Optional
from pydantic import BaseModel, Field


class CCR_I16_ROLE_GOAL_OBJECT(BaseModel):
    """HL7 v2 CCR_I16.ROLE_GOAL_OBJECT group."""

    pass

    model_config = {"populate_by_name": True}

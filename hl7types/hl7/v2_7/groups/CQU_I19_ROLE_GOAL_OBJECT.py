"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7
Class: CQU_I19.ROLE_GOAL_OBJECT
Type: Group
"""
from __future__ import annotations

from typing import Optional
from pydantic import BaseModel, Field


class CQU_I19_ROLE_GOAL_OBJECT(BaseModel):
    """HL7 v2 CQU_I19.ROLE_GOAL_OBJECT group."""

    pass

    model_config = {"populate_by_name": True}

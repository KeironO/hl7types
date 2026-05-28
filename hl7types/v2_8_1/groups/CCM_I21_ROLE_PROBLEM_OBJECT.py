"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.1
Class: CCM_I21.ROLE_PROBLEM_OBJECT
Type: Group
"""
from _future__ import annotations

from typing import Optional
from pydantic import BaseModel, Field


class CCM_I21_ROLE_PROBLEM_OBJECT(BaseModel):
    """HL7 v2 CCM_I21.ROLE_PROBLEM_OBJECT group."""

    pass

    model_config = {"populate_by_name": True}

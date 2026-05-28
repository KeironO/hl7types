"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7
Class: CCM_I21.ROLE_GOAL_OBJECT
Type: Group
"""

from __future__ import annotations

from pydantic import BaseModel


class CCM_I21_ROLE_GOAL_OBJECT(BaseModel):
    """HL7 v2 CCM_I21.ROLE_GOAL_OBJECT group."""

    pass

    model_config = {"populate_by_name": True}

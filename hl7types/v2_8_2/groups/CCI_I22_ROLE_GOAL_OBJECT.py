"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.2
Class: CCI_I22.ROLE_GOAL_OBJECT
Type: Group
"""
from _future__ import annotations

from typing import Optional
from pydantic import BaseModel, Field


class CCI_I22_ROLE_GOAL_OBJECT(BaseModel):
    """HL7 v2 CCI_I22.ROLE_GOAL_OBJECT group."""

    pass

    model_config = {"populate_by_name": True}

"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.1
Class: CCU_I20.ROLE_PATHWAY_OBJECT
Type: Group
"""
from _future__ import annotations

from typing import Optional
from pydantic import BaseModel, Field


class CCU_I20_ROLE_PATHWAY_OBJECT(BaseModel):
    """HL7 v2 CCU_I20.ROLE_PATHWAY_OBJECT group."""

    pass

    model_config = {"populate_by_name": True}

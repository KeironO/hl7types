"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7.1
Class: CCM_I21.ROLE_CLINICAL_HISTORY_OBJECT
Type: Group
"""
from _future__ import annotations

from typing import Optional
from pydantic import BaseModel, Field


class CCM_I21_ROLE_CLINICAL_HISTORY_OBJECT(BaseModel):
    """HL7 v2 CCM_I21.ROLE_CLINICAL_HISTORY_OBJECT group."""

    pass

    model_config = {"populate_by_name": True}

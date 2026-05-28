"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8
Class: CCU_I20.ROLE_CLINICAL_HISTORY_OBJECT
Type: Group
"""

from __future__ import annotations

from pydantic import BaseModel


class CCU_I20_ROLE_CLINICAL_HISTORY_OBJECT(BaseModel):
    """HL7 v2 CCU_I20.ROLE_CLINICAL_HISTORY_OBJECT group."""

    pass

    model_config = {"populate_by_name": True}

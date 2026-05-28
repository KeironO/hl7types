"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8
Class: CCM_I21.CLINICAL_HISTORY_OBJECT
Type: Group
"""

from __future__ import annotations

from pydantic import BaseModel


class CCM_I21_CLINICAL_HISTORY_OBJECT(BaseModel):
    """HL7 v2 CCM_I21.CLINICAL_HISTORY_OBJECT group."""

    pass

    model_config = {"populate_by_name": True}

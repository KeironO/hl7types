"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.2
Class: CCR_I16.CLINICAL_ORDER_OBJECT
Type: Group
"""

from __future__ import annotations

from pydantic import BaseModel


class CCR_I16_CLINICAL_ORDER_OBJECT(BaseModel):
    """HL7 v2 CCR_I16.CLINICAL_ORDER_OBJECT group."""

    pass

    model_config = {"populate_by_name": True}

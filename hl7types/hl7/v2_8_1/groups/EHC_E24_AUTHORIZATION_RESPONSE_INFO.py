"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.1
Class: EHC_E24.AUTHORIZATION_RESPONSE_INFO
Type: Group
"""

from __future__ import annotations

from pydantic import BaseModel


class EHC_E24_AUTHORIZATION_RESPONSE_INFO(BaseModel):
    """HL7 v2 EHC_E24.AUTHORIZATION_RESPONSE_INFO group."""

    pass

    model_config = {"populate_by_name": True}

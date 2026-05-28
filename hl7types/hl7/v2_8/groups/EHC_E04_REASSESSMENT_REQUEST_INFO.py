"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8
Class: EHC_E04.REASSESSMENT_REQUEST_INFO
Type: Group
"""

from __future__ import annotations

from pydantic import BaseModel


class EHC_E04_REASSESSMENT_REQUEST_INFO(BaseModel):
    """HL7 v2 EHC_E04.REASSESSMENT_REQUEST_INFO group."""

    pass

    model_config = {"populate_by_name": True}

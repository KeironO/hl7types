"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7.1
Class: EHC_E20.AUTHORIZATION_REQUEST
Type: Group
"""

from __future__ import annotations

from pydantic import BaseModel


class EHC_E20_AUTHORIZATION_REQUEST(BaseModel):
    """HL7 v2 EHC_E20.AUTHORIZATION_REQUEST group."""

    pass

    model_config = {"populate_by_name": True}

"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7
Class: EHC_E20.AUTHORIZATION_REQUEST
Type: Group
"""
from __future__ import annotations

from typing import Optional
from pydantic import BaseModel, Field


class EHC_E20_AUTHORIZATION_REQUEST(BaseModel):
    """HL7 v2 EHC_E20.AUTHORIZATION_REQUEST group."""

    pass

    model_config = {"populate_by_name": True}

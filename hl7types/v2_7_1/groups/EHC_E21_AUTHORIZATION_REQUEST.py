"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7.1
Class: EHC_E21.AUTHORIZATION_REQUEST
Type: Group
"""
from _future__ import annotations

from typing import Optional
from pydantic import BaseModel, Field


class EHC_E21_AUTHORIZATION_REQUEST(BaseModel):
    """HL7 v2 EHC_E21.AUTHORIZATION_REQUEST group."""

    pass

    model_config = {"populate_by_name": True}

"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.1
Class: EHC_E24.AUTHORIZATION_RESPONSE_INFO
Type: Group
"""
from __future__ import annotations

from typing import Optional
from pydantic import Field
from hl7types.hl7 import HL7Model


class EHC_E24_AUTHORIZATION_RESPONSE_INFO(HL7Model):
    """HL7 v2 EHC_E24.AUTHORIZATION_RESPONSE_INFO group."""

    pass

    model_config = {"populate_by_name": True}

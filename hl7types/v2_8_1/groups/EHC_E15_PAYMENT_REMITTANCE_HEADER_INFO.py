"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.1
Class: EHC_E15.PAYMENT_REMITTANCE_HEADER_INFO
Type: Group
"""
from _future__ import annotations

from typing import Optional
from pydantic import BaseModel, Field


class EHC_E15_PAYMENT_REMITTANCE_HEADER_INFO(BaseModel):
    """HL7 v2 EHC_E15.PAYMENT_REMITTANCE_HEADER_INFO group."""

    pass

    model_config = {"populate_by_name": True}

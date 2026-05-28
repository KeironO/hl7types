"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.6
Class: EHC_E15.PAYMENT_REMITTANCE_HEADER_INFO
Type: Group
"""

from __future__ import annotations

from pydantic import BaseModel


class EHC_E15_PAYMENT_REMITTANCE_HEADER_INFO(BaseModel):
    """HL7 v2 EHC_E15.PAYMENT_REMITTANCE_HEADER_INFO group."""

    pass

    model_config = {"populate_by_name": True}

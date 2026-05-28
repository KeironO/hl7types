"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7.1
Class: EHC_E01.INVOICE_INFORMATION
Type: Group
"""
from __future__ import annotations

from typing import Optional
from pydantic import BaseModel, Field


class EHC_E01_INVOICE_INFORMATION(BaseModel):
    """HL7 v2 EHC_E01.INVOICE_INFORMATION group."""

    pass

    model_config = {"populate_by_name": True}

"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.1
Class: EHC_E02.INVOICE_INFORMATION_CANCEL
Type: Group
"""
from __future__ import annotations

from typing import Optional
from pydantic import Field
from hl7types.hl7 import HL7Model


class EHC_E02_INVOICE_INFORMATION_CANCEL(HL7Model):
    """HL7 v2 EHC_E02.INVOICE_INFORMATION_CANCEL group."""

    pass

    model_config = {"populate_by_name": True}

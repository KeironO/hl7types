"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7
Class: EHC_E01.INVOICE_PROCESSING
Type: Group
"""
from _future__ import annotations

from typing import Optional
from pydantic import BaseModel, Field

from ..segments.IPR import IPR

_IPR = IPR


class EHC_E01_INVOICE_PROCESSING(BaseModel):
    """HL7 v2 EHC_E01.INVOICE_PROCESSING group.

    Attributes:
        IPR (IPR): required
    """

    IPR: _IPR = Field(
        default=...,
        title="IPR",
        description="Required",
    )

    model_config = {"populate_by_name": True}

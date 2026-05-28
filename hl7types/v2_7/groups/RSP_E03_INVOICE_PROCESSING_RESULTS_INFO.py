"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7
Class: RSP_E03.INVOICE_PROCESSING_RESULTS_INFO
Type: Group
"""
from _future__ import annotations

from typing import Optional
from pydantic import BaseModel, Field

from ..segments.IPR import IPR

_IPR = IPR


class RSP_E03_INVOICE_PROCESSING_RESULTS_INFO(BaseModel):
    """HL7 v2 RSP_E03.INVOICE_PROCESSING_RESULTS_INFO group.

    Attributes:
        IPR (IPR): required
    """

    IPR: _IPR = Field(
        default=...,
        title="IPR",
        description="Required",
    )

    model_config = {"populate_by_name": True}

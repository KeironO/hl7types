"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7.1
Class: RSP_E03.INVOICE_PROCESSING_RESULTS_INFO
Type: Group
"""
from __future__ import annotations

from pydantic import ConfigDict, Field
from hl7types.hl7 import HL7Model

from ..segments.IPR import IPR

_IPR = IPR


class RSP_E03_INVOICE_PROCESSING_RESULTS_INFO(HL7Model):
    """HL7 v2 RSP_E03.INVOICE_PROCESSING_RESULTS_INFO group.

    Attributes:
        IPR (IPR): Invoice Processing Results, required
    """

    IPR: _IPR = Field(
        title="IPR",
        description="Invoice Processing Results",
    )

    model_config = ConfigDict(populate_by_name=True)

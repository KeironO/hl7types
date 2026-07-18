"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7
Class: EHC_E01.INVOICE_PROCESSING
Type: Group
"""
from __future__ import annotations

from pydantic import ConfigDict, Field
from hl7types.hl7 import HL7Model

from ..segments.IPR import IPR

_IPR = IPR


class EHC_E01_INVOICE_PROCESSING(HL7Model):
    """HL7 v2 EHC_E01.INVOICE_PROCESSING group.

    Attributes:
        IPR (IPR): Invoice Processing Results, required
    """

    IPR: _IPR = Field(
        title="IPR",
        description="Invoice Processing Results",
    )

    model_config = ConfigDict(populate_by_name=True)

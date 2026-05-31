"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.1
Class: EHC_E15.PAYMENT_REMITTANCE_HEADER_INFO
Type: Group
"""
from __future__ import annotations

from typing import Optional
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.PMT import PMT
from ..segments.PYE import PYE

_PMT = PMT
_PYE = PYE


class EHC_E15_PAYMENT_REMITTANCE_HEADER_INFO(HL7Model):
    """HL7 v2 EHC_E15.PAYMENT_REMITTANCE_HEADER_INFO group.

    Attributes:
        PMT (Optional[PMT]): optional
        PYE (Optional[PYE]): optional
    """

    PMT: Optional[_PMT] = Field(
        default=None,
        title="PMT",
        description="Optional",
    )

    PYE: Optional[_PYE] = Field(
        default=None,
        title="PYE",
        description="Optional",
    )

    model_config = {"populate_by_name": True}

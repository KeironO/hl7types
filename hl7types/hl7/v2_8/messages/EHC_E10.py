"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8
Class: EHC_E10
Type: Message
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.ERR import ERR
from ..segments.MSA import MSA
from ..segments.MSH import MSH
from ..segments.SFT import SFT
from ..segments.UAC import UAC

from ..groups.EHC_E10_INVOICE_PROCESSING_RESULTS_INFO import EHC_E10_INVOICE_PROCESSING_RESULTS_INFO

_EHC_E10_INVOICE_PROCESSING_RESULTS_INFO = EHC_E10_INVOICE_PROCESSING_RESULTS_INFO
_ERR = ERR
_MSA = MSA
_MSH = MSH
_SFT = SFT
_UAC = UAC


class EHC_E10(HL7Model):
    """Edit/Adjudication Results (S16.3.1).

    Attributes:
        MSH (MSH): Message Header, required
        SFT (Optional[List[SFT]]): Software Segment, optional
        UAC (Optional[List[UAC]]): User Authentication Credential Segment, optional
        MSA (MSA): Message Acknowledgment, required
        ERR (Optional[List[ERR]]): Error, optional
        INVOICE_PROCESSING_RESULTS_INFO (List[EHC_E10_INVOICE_PROCESSING_RESULTS_INFO]): required
    """

    MSH: _MSH = Field(
        title="MSH",
        description="Message Header",
    )

    SFT: Optional[List[_SFT]] = Field(
        default=None,
        title="SFT",
        description="Software Segment",
    )

    UAC: Optional[List[_UAC]] = Field(
        default=None,
        title="UAC",
        description="User Authentication Credential Segment",
    )

    MSA: _MSA = Field(
        title="MSA",
        description="Message Acknowledgment",
    )

    ERR: Optional[List[_ERR]] = Field(
        default=None,
        title="ERR",
        description="Error",
    )

    INVOICE_PROCESSING_RESULTS_INFO: List[_EHC_E10_INVOICE_PROCESSING_RESULTS_INFO] = Field(
        min_length=1,
        title="INVOICE_PROCESSING_RESULTS_INFO",
    )

    model_config = {"populate_by_name": True}

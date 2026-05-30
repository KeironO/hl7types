"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5.1
Class: DOC_T12
Type: Message
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.DSC import DSC
from ..segments.ERR import ERR
from ..segments.MSA import MSA
from ..segments.MSH import MSH
from ..segments.QAK import QAK
from ..segments.QRD import QRD

from ..groups.DOC_T12_EVNPIDPV1TXAOBX_SUPPGRP import DOC_T12_EVNPIDPV1TXAOBX_SUPPGRP

_DOC_T12_EVNPIDPV1TXAOBX_SUPPGRP = DOC_T12_EVNPIDPV1TXAOBX_SUPPGRP
_DSC = DSC
_ERR = ERR
_MSA = MSA
_MSH = MSH
_QAK = QAK
_QRD = QRD


class DOC_T12(HL7Model):
    """HL7 v2 DOC_T12 message.

    Attributes:
        MSH (MSH): required
        MSA (MSA): required
        ERR (Optional[ERR]): optional
        QAK (Optional[QAK]): optional
        QRD (QRD): required
        EVNPIDPV1TXAOBX_SUPPGRP (List[DOC_T12_EVNPIDPV1TXAOBX_SUPPGRP]): required
        DSC (Optional[DSC]): optional
    """

    MSH: _MSH = Field(
        default=...,
        title="MSH",
        description="Required",
    )

    MSA: _MSA = Field(
        default=...,
        title="MSA",
        description="Required",
    )

    ERR: Optional[_ERR] = Field(
        default=None,
        title="ERR",
        description="Optional",
    )

    QAK: Optional[_QAK] = Field(
        default=None,
        title="QAK",
        description="Optional",
    )

    QRD: _QRD = Field(
        default=...,
        title="QRD",
        description="Required",
    )

    EVNPIDPV1TXAOBX_SUPPGRP: List[_DOC_T12_EVNPIDPV1TXAOBX_SUPPGRP] = Field(
        default=...,
        title="EVNPIDPV1TXAOBX_SUPPGRP",
        description="Required, repeating",
    )

    DSC: Optional[_DSC] = Field(
        default=None,
        title="DSC",
        description="Optional",
    )

    model_config = {"populate_by_name": True}

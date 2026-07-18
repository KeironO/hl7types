"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5.1
Class: OUL_R23
Type: Message
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import ConfigDict, Field
from hl7types.hl7 import HL7Model

from ..segments.DSC import DSC
from ..segments.MSH import MSH
from ..segments.NTE import NTE
from ..segments.SFT import SFT

from ..groups.OUL_R23_PIDPD1NTE_SUPPGRP import OUL_R23_PIDPD1NTE_SUPPGRP
from ..groups.OUL_R23_PV1PV2_SUPPGRP import OUL_R23_PV1PV2_SUPPGRP
from ..groups.OUL_R23_SPMOBXSACINVOBRORCNTETQ1TQ2OBXTCDSIDNTECTI_SUPPGRP import OUL_R23_SPMOBXSACINVOBRORCNTETQ1TQ2OBXTCDSIDNTECTI_SUPPGRP

_DSC = DSC
_MSH = MSH
_NTE = NTE
_OUL_R23_PIDPD1NTE_SUPPGRP = OUL_R23_PIDPD1NTE_SUPPGRP
_OUL_R23_PV1PV2_SUPPGRP = OUL_R23_PV1PV2_SUPPGRP
_OUL_R23_SPMOBXSACINVOBRORCNTETQ1TQ2OBXTCDSIDNTECTI_SUPPGRP = OUL_R23_SPMOBXSACINVOBRORCNTETQ1TQ2OBXTCDSIDNTECTI_SUPPGRP
_SFT = SFT


class OUL_R23(HL7Model):
    """OUL - Unsolicited Specimen Container Oriented Observation Message (S7.3.2).

    Attributes:
        MSH (MSH): Message Header, required
        SFT (Optional[List[SFT]]): Software Segment, optional
        NTE (Optional[NTE]): Notes and Comments, optional
        PIDPD1NTE_SUPPGRP (Optional[OUL_R23_PIDPD1NTE_SUPPGRP]): optional
        PV1PV2_SUPPGRP (Optional[OUL_R23_PV1PV2_SUPPGRP]): optional
        SPMOBXSACINVOBRORCNTETQ1TQ2OBXTCDSIDNTECTI_SUPPGRP (List[OUL_R23_SPMOBXSACINVOBRORCNTETQ1TQ2OBXTCDSIDNTECTI_SUPPGRP]): required
        DSC (Optional[DSC]): Continuation Pointer, optional
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

    NTE: Optional[_NTE] = Field(
        default=None,
        title="NTE",
        description="Notes and Comments",
    )

    PIDPD1NTE_SUPPGRP: Optional[_OUL_R23_PIDPD1NTE_SUPPGRP] = Field(
        default=None,
        title="PIDPD1NTE_SUPPGRP",
    )

    PV1PV2_SUPPGRP: Optional[_OUL_R23_PV1PV2_SUPPGRP] = Field(
        default=None,
        title="PV1PV2_SUPPGRP",
    )

    SPMOBXSACINVOBRORCNTETQ1TQ2OBXTCDSIDNTECTI_SUPPGRP: List[_OUL_R23_SPMOBXSACINVOBRORCNTETQ1TQ2OBXTCDSIDNTECTI_SUPPGRP] = Field(
        min_length=1,
        title="SPMOBXSACINVOBRORCNTETQ1TQ2OBXTCDSIDNTECTI_SUPPGRP",
    )

    DSC: Optional[_DSC] = Field(
        default=None,
        title="DSC",
        description="Continuation Pointer",
    )

    model_config = ConfigDict(populate_by_name=True)

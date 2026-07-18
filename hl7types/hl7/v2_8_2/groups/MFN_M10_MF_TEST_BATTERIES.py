"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.2
Class: MFN_M10.MF_TEST_BATTERIES
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import ConfigDict, Field
from hl7types.hl7 import HL7Model

from ..segments.MFE import MFE
from ..segments.OM1 import OM1
from ..segments.OMC import OMC
from ..segments.PRT import PRT

from .MFN_M10_MF_TEST_BATT_DETAIL import MFN_M10_MF_TEST_BATT_DETAIL

_MFE = MFE
_MFN_M10_MF_TEST_BATT_DETAIL = MFN_M10_MF_TEST_BATT_DETAIL
_OM1 = OM1
_OMC = OMC
_PRT = PRT


class MFN_M10_MF_TEST_BATTERIES(HL7Model):
    """HL7 v2 MFN_M10.MF_TEST_BATTERIES group.

    Attributes:
        MFE (MFE): Master File Entry, required
        OM1 (OM1): General Segment, required
        OMC (Optional[List[OMC]]): Supporting Clinical Information, optional
        PRT (Optional[List[PRT]]): Participation Information, optional
        MF_TEST_BATT_DETAIL (Optional[MFN_M10_MF_TEST_BATT_DETAIL]): optional
    """

    MFE: _MFE = Field(
        title="MFE",
        description="Master File Entry",
    )

    OM1: _OM1 = Field(
        title="OM1",
        description="General Segment",
    )

    OMC: Optional[List[_OMC]] = Field(
        default=None,
        title="OMC",
        description="Supporting Clinical Information",
    )

    PRT: Optional[List[_PRT]] = Field(
        default=None,
        title="PRT",
        description="Participation Information",
    )

    MF_TEST_BATT_DETAIL: Optional[_MFN_M10_MF_TEST_BATT_DETAIL] = Field(
        default=None,
        title="MF_TEST_BATT_DETAIL",
    )

    model_config = ConfigDict(populate_by_name=True)

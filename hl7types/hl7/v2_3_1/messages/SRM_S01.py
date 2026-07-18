"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3.1
Class: SRM_S01
Type: Message
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import ConfigDict, Field
from hl7types.hl7 import HL7Model

from ..segments.APR import APR
from ..segments.ARQ import ARQ
from ..segments.MSH import MSH
from ..segments.NTE import NTE

from ..groups.SRM_S01_PATIENT import SRM_S01_PATIENT
from ..groups.SRM_S01_RESOURCES import SRM_S01_RESOURCES

_APR = APR
_ARQ = ARQ
_MSH = MSH
_NTE = NTE
_SRM_S01_PATIENT = SRM_S01_PATIENT
_SRM_S01_RESOURCES = SRM_S01_RESOURCES


class SRM_S01(HL7Model):
    """SRM/SRR - Request new appointment booking.

    Attributes:
        MSH (MSH): MSH - message header segment, required
        ARQ (ARQ): ARQ - appointment request segment, required
        APR (Optional[APR]): APR - appointment preferences segment, optional
        NTE (Optional[List[NTE]]): NTE - notes and comments segment, optional
        PATIENT (Optional[List[SRM_S01_PATIENT]]): optional
        RESOURCES (List[SRM_S01_RESOURCES]): required
    """

    MSH: _MSH = Field(
        title="MSH",
        description="MSH - message header segment",
    )

    ARQ: _ARQ = Field(
        title="ARQ",
        description="ARQ - appointment request segment",
    )

    APR: Optional[_APR] = Field(
        default=None,
        title="APR",
        description="APR - appointment preferences segment",
    )

    NTE: Optional[List[_NTE]] = Field(
        default=None,
        title="NTE",
        description="NTE - notes and comments segment",
    )

    PATIENT: Optional[List[_SRM_S01_PATIENT]] = Field(
        default=None,
        title="PATIENT",
    )

    RESOURCES: List[_SRM_S01_RESOURCES] = Field(
        min_length=1,
        title="RESOURCES",
    )

    model_config = ConfigDict(populate_by_name=True)

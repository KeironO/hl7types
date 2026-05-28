"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8
Class: SRM_S01
Type: Message
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..groups.SRM_S01_PATIENT import SRM_S01_PATIENT
from ..groups.SRM_S01_RESOURCES import SRM_S01_RESOURCES
from ..segments.APR import APR
from ..segments.ARQ import ARQ
from ..segments.MSH import MSH
from ..segments.NTE import NTE

_APR = APR
_ARQ = ARQ
_MSH = MSH
_NTE = NTE
_SRM_S01_PATIENT = SRM_S01_PATIENT
_SRM_S01_RESOURCES = SRM_S01_RESOURCES


class SRM_S01(BaseModel):
    """HL7 v2 SRM_S01 message.

    Attributes:
        MSH (MSH): required
        ARQ (ARQ): required
        APR (Optional[APR]): optional
        NTE (Optional[List[NTE]]): optional
        PATIENT (Optional[List[SRM_S01_PATIENT]]): optional
        RESOURCES (List[SRM_S01_RESOURCES]): required
    """

    MSH: _MSH = Field(
        default=...,
        title="MSH",
        description="Required",
    )

    ARQ: _ARQ = Field(
        default=...,
        title="ARQ",
        description="Required",
    )

    APR: _APR | None = Field(
        default=None,
        title="APR",
        description="Optional",
    )

    NTE: list[_NTE] | None = Field(
        default=None,
        title="NTE",
        description="Optional, repeating",
    )

    PATIENT: list[_SRM_S01_PATIENT] | None = Field(
        default=None,
        title="PATIENT",
        description="Optional, repeating",
    )

    RESOURCES: list[_SRM_S01_RESOURCES] = Field(
        default=...,
        title="RESOURCES",
        description="Required, repeating",
    )

    model_config = {"populate_by_name": True}

"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3
Class: RPI_I01
Type: Message
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.MSA import MSA
from ..segments.MSH import MSH
from ..segments.NK1 import NK1
from ..segments.NTE import NTE
from ..segments.PID import PID

from ..groups.RPI_I01_GUARANTOR_INSURANCE import RPI_I01_GUARANTOR_INSURANCE
from ..groups.RPI_I01_PROVIDER import RPI_I01_PROVIDER

_MSA = MSA
_MSH = MSH
_NK1 = NK1
_NTE = NTE
_PID = PID
_RPI_I01_GUARANTOR_INSURANCE = RPI_I01_GUARANTOR_INSURANCE
_RPI_I01_PROVIDER = RPI_I01_PROVIDER


class RPI_I01(HL7Model):
    """HL7 v2 RPI_I01 message.

    Attributes:
        MSH (MSH): required
        MSA (MSA): required
        PROVIDER (List[RPI_I01_PROVIDER]): required
        PID (PID): required
        NK1 (Optional[List[NK1]]): optional
        GUARANTOR_INSURANCE (Optional[RPI_I01_GUARANTOR_INSURANCE]): optional
        NTE (Optional[List[NTE]]): optional
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

    PROVIDER: List[_RPI_I01_PROVIDER] = Field(
        default=...,
        title="PROVIDER",
        description="Required, repeating",
    )

    PID: _PID = Field(
        default=...,
        title="PID",
        description="Required",
    )

    NK1: Optional[List[_NK1]] = Field(
        default=None,
        title="NK1",
        description="Optional, repeating",
    )

    GUARANTOR_INSURANCE: Optional[_RPI_I01_GUARANTOR_INSURANCE] = Field(
        default=None,
        title="GUARANTOR_INSURANCE",
        description="Optional",
    )

    NTE: Optional[List[_NTE]] = Field(
        default=None,
        title="NTE",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}

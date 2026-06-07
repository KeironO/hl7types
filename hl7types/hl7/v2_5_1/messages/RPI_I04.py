"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5.1
Class: RPI_I04
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
from ..segments.SFT import SFT

from ..groups.RPI_I04_GUARANTOR_INSURANCE import RPI_I04_GUARANTOR_INSURANCE
from ..groups.RPI_I04_PROVIDER import RPI_I04_PROVIDER

_MSA = MSA
_MSH = MSH
_NK1 = NK1
_NTE = NTE
_PID = PID
_RPI_I04_GUARANTOR_INSURANCE = RPI_I04_GUARANTOR_INSURANCE
_RPI_I04_PROVIDER = RPI_I04_PROVIDER
_SFT = SFT


class RPI_I04(HL7Model):
    """HL7 v2 RPI_I04 message.

    Attributes:
        MSH (MSH): required
        SFT (Optional[List[SFT]]): optional
        MSA (MSA): required
        PROVIDER (List[RPI_I04_PROVIDER]): required
        PID (PID): required
        NK1 (Optional[List[NK1]]): optional
        GUARANTOR_INSURANCE (Optional[RPI_I04_GUARANTOR_INSURANCE]): optional
        NTE (Optional[List[NTE]]): optional
    """

    MSH: _MSH = Field(
        title="MSH",
        description="Required",
    )

    SFT: Optional[List[_SFT]] = Field(
        default=None,
        title="SFT",
        description="Optional, repeating",
    )

    MSA: _MSA = Field(
        title="MSA",
        description="Required",
    )

    PROVIDER: List[_RPI_I04_PROVIDER] = Field(
        min_length=1,
        title="PROVIDER",
        description="Required, repeating",
    )

    PID: _PID = Field(
        title="PID",
        description="Required",
    )

    NK1: Optional[List[_NK1]] = Field(
        default=None,
        title="NK1",
        description="Optional, repeating",
    )

    GUARANTOR_INSURANCE: Optional[_RPI_I04_GUARANTOR_INSURANCE] = Field(
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

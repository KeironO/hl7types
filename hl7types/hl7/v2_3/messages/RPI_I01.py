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
    """RQI/RPI - Request for insurance information.

    Attributes:
        MSH (MSH): Message header segment, required
        MSA (MSA): Message acknowledgement segment, required
        PROVIDER (List[RPI_I01_PROVIDER]): required
        PID (PID): Patient Identification, required
        NK1 (Optional[List[NK1]]): Next of kin, optional
        GUARANTOR_INSURANCE (Optional[RPI_I01_GUARANTOR_INSURANCE]): optional
        NTE (Optional[List[NTE]]): Notes and comments segment, optional
    """

    MSH: _MSH = Field(
        title="MSH",
        description="Message header segment",
    )

    MSA: _MSA = Field(
        title="MSA",
        description="Message acknowledgement segment",
    )

    PROVIDER: List[_RPI_I01_PROVIDER] = Field(
        min_length=1,
        title="PROVIDER",
    )

    PID: _PID = Field(
        title="PID",
        description="Patient Identification",
    )

    NK1: Optional[List[_NK1]] = Field(
        default=None,
        title="NK1",
        description="Next of kin",
    )

    GUARANTOR_INSURANCE: Optional[_RPI_I01_GUARANTOR_INSURANCE] = Field(
        default=None,
        title="GUARANTOR_INSURANCE",
    )

    NTE: Optional[List[_NTE]] = Field(
        default=None,
        title="NTE",
        description="Notes and comments segment",
    )

    model_config = {"populate_by_name": True}

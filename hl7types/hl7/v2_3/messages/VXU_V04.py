"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3
Class: VXU_V04
Type: Message
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import ConfigDict, Field
from hl7types.hl7 import HL7Model

from ..segments.MSH import MSH
from ..segments.NK1 import NK1
from ..segments.PD1 import PD1
from ..segments.PID import PID

from ..groups.VXU_V04_INSURANCE import VXU_V04_INSURANCE
from ..groups.VXU_V04_ORDER import VXU_V04_ORDER
from ..groups.VXU_V04_PATIENT import VXU_V04_PATIENT

_MSH = MSH
_NK1 = NK1
_PD1 = PD1
_PID = PID
_VXU_V04_INSURANCE = VXU_V04_INSURANCE
_VXU_V04_ORDER = VXU_V04_ORDER
_VXU_V04_PATIENT = VXU_V04_PATIENT


class VXU_V04(HL7Model):
    """VXU - Unsolicited vaccination record update.

    Attributes:
        MSH (MSH): Message header segment, required
        PID (PID): Patient Identification, required
        PD1 (Optional[PD1]): Patient Demographic, optional
        NK1 (Optional[List[NK1]]): Next of kin, optional
        PATIENT (Optional[VXU_V04_PATIENT]): optional
        INSURANCE (Optional[List[VXU_V04_INSURANCE]]): optional
        ORDER (Optional[List[VXU_V04_ORDER]]): optional
    """

    MSH: _MSH = Field(
        title="MSH",
        description="Message header segment",
    )

    PID: _PID = Field(
        title="PID",
        description="Patient Identification",
    )

    PD1: Optional[_PD1] = Field(
        default=None,
        title="PD1",
        description="Patient Demographic",
    )

    NK1: Optional[List[_NK1]] = Field(
        default=None,
        title="NK1",
        description="Next of kin",
    )

    PATIENT: Optional[_VXU_V04_PATIENT] = Field(
        default=None,
        title="PATIENT",
    )

    INSURANCE: Optional[List[_VXU_V04_INSURANCE]] = Field(
        default=None,
        title="INSURANCE",
    )

    ORDER: Optional[List[_VXU_V04_ORDER]] = Field(
        default=None,
        title="ORDER",
    )

    model_config = ConfigDict(populate_by_name=True)

"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.4
Class: OMS_O05
Type: Message
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.MSH import MSH
from ..segments.NTE import NTE

from ..groups.OMS_O05_ORDER import OMS_O05_ORDER
from ..groups.OMS_O05_PATIENT import OMS_O05_PATIENT

_MSH = MSH
_NTE = NTE
_OMS_O05_ORDER = OMS_O05_ORDER
_OMS_O05_PATIENT = OMS_O05_PATIENT


class OMS_O05(HL7Model):
    """OMS - Stock requisition order (S4).

    Attributes:
        MSH (MSH): Message Header, required
        NTE (Optional[List[NTE]]): Notes and Comments, optional
        PATIENT (Optional[OMS_O05_PATIENT]): optional
        ORDER (List[OMS_O05_ORDER]): required
    """

    MSH: _MSH = Field(
        title="MSH",
        description="Message Header",
    )

    NTE: Optional[List[_NTE]] = Field(
        default=None,
        title="NTE",
        description="Notes and Comments",
    )

    PATIENT: Optional[_OMS_O05_PATIENT] = Field(
        default=None,
        title="PATIENT",
    )

    ORDER: List[_OMS_O05_ORDER] = Field(
        min_length=1,
        title="ORDER",
    )

    model_config = {"populate_by_name": True}

"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.4
Class: RGV_O15
Type: Message
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.MSH import MSH
from ..segments.NTE import NTE

from ..groups.RGV_O15_ORDER import RGV_O15_ORDER
from ..groups.RGV_O15_PATIENT import RGV_O15_PATIENT

_MSH = MSH
_NTE = NTE
_RGV_O15_ORDER = RGV_O15_ORDER
_RGV_O15_PATIENT = RGV_O15_PATIENT


class RGV_O15(HL7Model):
    """HL7 v2 RGV_O15 message.

    Attributes:
        MSH (MSH): required
        NTE (Optional[List[NTE]]): optional
        PATIENT (Optional[RGV_O15_PATIENT]): optional
        ORDER (List[RGV_O15_ORDER]): required
    """

    MSH: _MSH = Field(
        title="MSH",
        description="Required",
    )

    NTE: Optional[List[_NTE]] = Field(
        default=None,
        title="NTE",
        description="Optional, repeating",
    )

    PATIENT: Optional[_RGV_O15_PATIENT] = Field(
        default=None,
        title="PATIENT",
        description="Optional",
    )

    ORDER: List[_RGV_O15_ORDER] = Field(
        min_length=1,
        title="ORDER",
        description="Required, repeating",
    )

    model_config = {"populate_by_name": True}

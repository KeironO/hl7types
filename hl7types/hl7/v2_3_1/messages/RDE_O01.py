"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3.1
Class: RDE_O01
Type: Message
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.MSH import MSH
from ..segments.NTE import NTE

from ..groups.RDE_O01_ORDER import RDE_O01_ORDER
from ..groups.RDE_O01_PATIENT import RDE_O01_PATIENT

_MSH = MSH
_NTE = NTE
_RDE_O01_ORDER = RDE_O01_ORDER
_RDE_O01_PATIENT = RDE_O01_PATIENT


class RDE_O01(HL7Model):
    """ORM - Order message (also RDE, RDS, RGV, RAS).

    Attributes:
        MSH (MSH): MSH - message header segment, required
        NTE (Optional[List[NTE]]): NTE - notes and comments segment, optional
        PATIENT (Optional[RDE_O01_PATIENT]): optional
        ORDER (List[RDE_O01_ORDER]): required
    """

    MSH: _MSH = Field(
        title="MSH",
        description="MSH - message header segment",
    )

    NTE: Optional[List[_NTE]] = Field(
        default=None,
        title="NTE",
        description="NTE - notes and comments segment",
    )

    PATIENT: Optional[_RDE_O01_PATIENT] = Field(
        default=None,
        title="PATIENT",
    )

    ORDER: List[_RDE_O01_ORDER] = Field(
        min_length=1,
        title="ORDER",
    )

    model_config = {"populate_by_name": True}

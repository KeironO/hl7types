"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.4
Class: RDE_O11
Type: Message
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.MSH import MSH
from ..segments.NTE import NTE

from ..groups.RDE_O11_ORDER import RDE_O11_ORDER
from ..groups.RDE_O11_PATIENT import RDE_O11_PATIENT

_MSH = MSH
_NTE = NTE
_RDE_O11_ORDER = RDE_O11_ORDER
_RDE_O11_PATIENT = RDE_O11_PATIENT


class RDE_O11(HL7Model):
    """RDE - Pharmacy/treatment encoded order (S4).

    Attributes:
        MSH (MSH): Message Header, required
        NTE (Optional[List[NTE]]): Notes and Comments, optional
        PATIENT (Optional[RDE_O11_PATIENT]): optional
        ORDER (List[RDE_O11_ORDER]): required
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

    PATIENT: Optional[_RDE_O11_PATIENT] = Field(
        default=None,
        title="PATIENT",
    )

    ORDER: List[_RDE_O11_ORDER] = Field(
        min_length=1,
        title="ORDER",
    )

    model_config = {"populate_by_name": True}

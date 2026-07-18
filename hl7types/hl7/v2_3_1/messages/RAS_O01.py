"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3.1
Class: RAS_O01
Type: Message
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import ConfigDict, Field
from hl7types.hl7 import HL7Model

from ..segments.MSH import MSH
from ..segments.NTE import NTE

from ..groups.RAS_O01_ORDER import RAS_O01_ORDER
from ..groups.RAS_O01_PATIENT import RAS_O01_PATIENT

_MSH = MSH
_NTE = NTE
_RAS_O01_ORDER = RAS_O01_ORDER
_RAS_O01_PATIENT = RAS_O01_PATIENT


class RAS_O01(HL7Model):
    """ORM - Order message (also RDE, RDS, RGV, RAS).

    Attributes:
        MSH (MSH): MSH - message header segment, required
        NTE (Optional[List[NTE]]): NTE - notes and comments segment, optional
        PATIENT (Optional[RAS_O01_PATIENT]): optional
        ORDER (List[RAS_O01_ORDER]): required
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

    PATIENT: Optional[_RAS_O01_PATIENT] = Field(
        default=None,
        title="PATIENT",
    )

    ORDER: List[_RAS_O01_ORDER] = Field(
        min_length=1,
        title="ORDER",
    )

    model_config = ConfigDict(populate_by_name=True)

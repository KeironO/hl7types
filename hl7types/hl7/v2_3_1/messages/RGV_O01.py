"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3.1
Class: RGV_O01
Type: Message
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import ConfigDict, Field
from hl7types.hl7 import HL7Model

from ..segments.MSH import MSH
from ..segments.NTE import NTE

from ..groups.RGV_O01_ORDER import RGV_O01_ORDER
from ..groups.RGV_O01_PATIENT import RGV_O01_PATIENT

_MSH = MSH
_NTE = NTE
_RGV_O01_ORDER = RGV_O01_ORDER
_RGV_O01_PATIENT = RGV_O01_PATIENT


class RGV_O01(HL7Model):
    """ORM - Order message (also RDE, RDS, RGV, RAS).

    Attributes:
        MSH (MSH): MSH - message header segment, required
        NTE (Optional[List[NTE]]): NTE - notes and comments segment, optional
        PATIENT (Optional[RGV_O01_PATIENT]): optional
        ORDER (List[RGV_O01_ORDER]): required
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

    PATIENT: Optional[_RGV_O01_PATIENT] = Field(
        default=None,
        title="PATIENT",
    )

    ORDER: List[_RGV_O01_ORDER] = Field(
        min_length=1,
        title="ORDER",
    )

    model_config = ConfigDict(populate_by_name=True)

"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3.1
Class: RDS_O01
Type: Message
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.MSH import MSH
from ..segments.NTE import NTE

from ..groups.RDS_O01_ORDER import RDS_O01_ORDER
from ..groups.RDS_O01_PATIENT import RDS_O01_PATIENT

_MSH = MSH
_NTE = NTE
_RDS_O01_ORDER = RDS_O01_ORDER
_RDS_O01_PATIENT = RDS_O01_PATIENT


class RDS_O01(HL7Model):
    """HL7 v2 RDS_O01 message.

    Attributes:
        MSH (MSH): required
        NTE (Optional[List[NTE]]): optional
        PATIENT (Optional[RDS_O01_PATIENT]): optional
        ORDER (List[RDS_O01_ORDER]): required
    """

    MSH: _MSH = Field(
        default=...,
        title="MSH",
        description="Required",
    )

    NTE: Optional[List[_NTE]] = Field(
        default=None,
        title="NTE",
        description="Optional, repeating",
    )

    PATIENT: Optional[_RDS_O01_PATIENT] = Field(
        default=None,
        title="PATIENT",
        description="Optional",
    )

    ORDER: List[_RDS_O01_ORDER] = Field(
        default=...,
        title="ORDER",
        description="Required, repeating",
    )

    model_config = {"populate_by_name": True}

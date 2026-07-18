"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3
Class: ORM_O01
Type: Message
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import ConfigDict, Field
from hl7types.hl7 import HL7Model

from ..segments.MSH import MSH
from ..segments.NTE import NTE

from ..groups.ORM_O01_ORDER import ORM_O01_ORDER
from ..groups.ORM_O01_PATIENT import ORM_O01_PATIENT

_MSH = MSH
_NTE = NTE
_ORM_O01_ORDER = ORM_O01_ORDER
_ORM_O01_PATIENT = ORM_O01_PATIENT


class ORM_O01(HL7Model):
    """ORM - Order message (also RDE, RDS, RGV, RAS,.

    Attributes:
        MSH (MSH): Message header segment, required
        NTE (Optional[List[NTE]]): Notes and comments segment, optional
        PATIENT (Optional[ORM_O01_PATIENT]): optional
        ORDER (List[ORM_O01_ORDER]): required
    """

    MSH: _MSH = Field(
        title="MSH",
        description="Message header segment",
    )

    NTE: Optional[List[_NTE]] = Field(
        default=None,
        title="NTE",
        description="Notes and comments segment",
    )

    PATIENT: Optional[_ORM_O01_PATIENT] = Field(
        default=None,
        title="PATIENT",
    )

    ORDER: List[_ORM_O01_ORDER] = Field(
        min_length=1,
        title="ORDER",
    )

    model_config = ConfigDict(populate_by_name=True)

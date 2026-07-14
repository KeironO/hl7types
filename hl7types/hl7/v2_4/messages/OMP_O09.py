"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.4
Class: OMP_O09
Type: Message
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.MSH import MSH
from ..segments.NTE import NTE

from ..groups.OMP_O09_ORDER import OMP_O09_ORDER
from ..groups.OMP_O09_PATIENT import OMP_O09_PATIENT

_MSH = MSH
_NTE = NTE
_OMP_O09_ORDER = OMP_O09_ORDER
_OMP_O09_PATIENT = OMP_O09_PATIENT


class OMP_O09(HL7Model):
    """OMP - Pharmacy/treatment order (S4).

    Attributes:
        MSH (MSH): Message Header, required
        NTE (Optional[List[NTE]]): Notes and Comments, optional
        PATIENT (Optional[OMP_O09_PATIENT]): optional
        ORDER (List[OMP_O09_ORDER]): required
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

    PATIENT: Optional[_OMP_O09_PATIENT] = Field(
        default=None,
        title="PATIENT",
    )

    ORDER: List[_OMP_O09_ORDER] = Field(
        min_length=1,
        title="ORDER",
    )

    model_config = {"populate_by_name": True}

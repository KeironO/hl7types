"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5
Class: OML_O21
Type: Message
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.MSH import MSH
from ..segments.NTE import NTE
from ..segments.SFT import SFT

from ..groups.OML_O21_ORDER import OML_O21_ORDER
from ..groups.OML_O21_PATIENT import OML_O21_PATIENT

_MSH = MSH
_NTE = NTE
_OML_O21_ORDER = OML_O21_ORDER
_OML_O21_PATIENT = OML_O21_PATIENT
_SFT = SFT


class OML_O21(HL7Model):
    """OML - Laboratory order (S4.4.6).

    Attributes:
        MSH (MSH): Message Header, required
        SFT (Optional[List[SFT]]): Software Segment, optional
        NTE (Optional[List[NTE]]): Notes and Comments, optional
        PATIENT (Optional[OML_O21_PATIENT]): optional
        ORDER (List[OML_O21_ORDER]): required
    """

    MSH: _MSH = Field(
        title="MSH",
        description="Message Header",
    )

    SFT: Optional[List[_SFT]] = Field(
        default=None,
        title="SFT",
        description="Software Segment",
    )

    NTE: Optional[List[_NTE]] = Field(
        default=None,
        title="NTE",
        description="Notes and Comments",
    )

    PATIENT: Optional[_OML_O21_PATIENT] = Field(
        default=None,
        title="PATIENT",
    )

    ORDER: List[_OML_O21_ORDER] = Field(
        min_length=1,
        title="ORDER",
    )

    model_config = {"populate_by_name": True}

"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.4
Class: OML_O21
Type: Message
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.MSH import MSH
from ..segments.NTE import NTE

from ..groups.OML_O21_ORDER_GENERAL import OML_O21_ORDER_GENERAL
from ..groups.OML_O21_PATIENT import OML_O21_PATIENT

_MSH = MSH
_NTE = NTE
_OML_O21_ORDER_GENERAL = OML_O21_ORDER_GENERAL
_OML_O21_PATIENT = OML_O21_PATIENT


class OML_O21(HL7Model):
    """OML - Laboratory order (S4).

    Attributes:
        MSH (MSH): Message Header, required
        NTE (Optional[List[NTE]]): Notes and Comments, optional
        PATIENT (Optional[OML_O21_PATIENT]): optional
        ORDER_GENERAL (List[OML_O21_ORDER_GENERAL]): required
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

    PATIENT: Optional[_OML_O21_PATIENT] = Field(
        default=None,
        title="PATIENT",
    )

    ORDER_GENERAL: List[_OML_O21_ORDER_GENERAL] = Field(
        min_length=1,
        title="ORDER_GENERAL",
    )

    model_config = {"populate_by_name": True}

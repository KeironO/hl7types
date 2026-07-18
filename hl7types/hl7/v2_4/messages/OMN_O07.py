"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.4
Class: OMN_O07
Type: Message
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import ConfigDict, Field
from hl7types.hl7 import HL7Model

from ..segments.MSH import MSH
from ..segments.NTE import NTE

from ..groups.OMN_O07_ORDER import OMN_O07_ORDER
from ..groups.OMN_O07_PATIENT import OMN_O07_PATIENT

_MSH = MSH
_NTE = NTE
_OMN_O07_ORDER = OMN_O07_ORDER
_OMN_O07_PATIENT = OMN_O07_PATIENT


class OMN_O07(HL7Model):
    """OMN - Non-stock requisition order (S4).

    Attributes:
        MSH (MSH): Message Header, required
        NTE (Optional[List[NTE]]): Notes and Comments, optional
        PATIENT (Optional[OMN_O07_PATIENT]): optional
        ORDER (List[OMN_O07_ORDER]): required
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

    PATIENT: Optional[_OMN_O07_PATIENT] = Field(
        default=None,
        title="PATIENT",
    )

    ORDER: List[_OMN_O07_ORDER] = Field(
        min_length=1,
        title="ORDER",
    )

    model_config = ConfigDict(populate_by_name=True)

"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.4
Class: OMG_O19
Type: Message
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import ConfigDict, Field
from hl7types.hl7 import HL7Model

from ..segments.MSH import MSH
from ..segments.NTE import NTE

from ..groups.OMG_O19_ORDER import OMG_O19_ORDER
from ..groups.OMG_O19_PATIENT import OMG_O19_PATIENT

_MSH = MSH
_NTE = NTE
_OMG_O19_ORDER = OMG_O19_ORDER
_OMG_O19_PATIENT = OMG_O19_PATIENT


class OMG_O19(HL7Model):
    """OMG - General clinical order (S4).

    Attributes:
        MSH (MSH): Message Header, required
        NTE (Optional[List[NTE]]): Notes and Comments, optional
        PATIENT (Optional[OMG_O19_PATIENT]): optional
        ORDER (List[OMG_O19_ORDER]): required
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

    PATIENT: Optional[_OMG_O19_PATIENT] = Field(
        default=None,
        title="PATIENT",
    )

    ORDER: List[_OMG_O19_ORDER] = Field(
        min_length=1,
        title="ORDER",
    )

    model_config = ConfigDict(populate_by_name=True)

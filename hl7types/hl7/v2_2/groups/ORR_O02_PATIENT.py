"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.2
Class: ORR_O02.PATIENT
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import ConfigDict, Field
from hl7types.hl7 import HL7Model

from ..segments.NTE import NTE
from ..segments.PID import PID

from .ORR_O02_ORDER import ORR_O02_ORDER

_NTE = NTE
_ORR_O02_ORDER = ORR_O02_ORDER
_PID = PID


class ORR_O02_PATIENT(HL7Model):
    """HL7 v2 ORR_O02.PATIENT group.

    Attributes:
        PID (Optional[PID]): PATIENT IDENTIFICATION, optional
        NTE (Optional[List[NTE]]): NOTES AND COMMENTS, optional
        ORDER (List[ORR_O02_ORDER]): required
    """

    PID: Optional[_PID] = Field(
        default=None,
        title="PID",
        description="PATIENT IDENTIFICATION",
    )

    NTE: Optional[List[_NTE]] = Field(
        default=None,
        title="NTE",
        description="NOTES AND COMMENTS",
    )

    ORDER: List[_ORR_O02_ORDER] = Field(
        min_length=1,
        title="ORDER",
    )

    model_config = ConfigDict(populate_by_name=True)

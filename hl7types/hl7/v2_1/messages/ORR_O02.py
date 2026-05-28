"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.1
Class: ORR_O02
Type: Message
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..groups.ORR_O02_PATIENT import ORR_O02_PATIENT
from ..segments.MSA import MSA
from ..segments.MSH import MSH
from ..segments.NTE import NTE

_MSA = MSA
_MSH = MSH
_NTE = NTE
_ORR_O02_PATIENT = ORR_O02_PATIENT


class ORR_O02(BaseModel):
    """HL7 v2 ORR_O02 message.

    Attributes:
        MSH (MSH): required
        MSA (MSA): required
        NTE (Optional[List[NTE]]): optional
        PATIENT (Optional[ORR_O02_PATIENT]): optional
    """

    MSH: _MSH = Field(
        default=...,
        title="MSH",
        description="Required",
    )

    MSA: _MSA = Field(
        default=...,
        title="MSA",
        description="Required",
    )

    NTE: list[_NTE] | None = Field(
        default=None,
        title="NTE",
        description="Optional, repeating",
    )

    PATIENT: _ORR_O02_PATIENT | None = Field(
        default=None,
        title="PATIENT",
        description="Optional",
    )

    model_config = {"populate_by_name": True}

"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3
Class: RRD_O02
Type: Message
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.ERR import ERR
from ..segments.MSA import MSA
from ..segments.MSH import MSH
from ..segments.NTE import NTE

from ..groups.RRD_O02_PATIENT import RRD_O02_PATIENT

_ERR = ERR
_MSA = MSA
_MSH = MSH
_NTE = NTE
_RRD_O02_PATIENT = RRD_O02_PATIENT


class RRD_O02(HL7Model):
    """HL7 v2 RRD_O02 message.

    Attributes:
        MSH (MSH): required
        MSA (MSA): required
        ERR (Optional[ERR]): optional
        NTE (Optional[List[NTE]]): optional
        PATIENT (Optional[RRD_O02_PATIENT]): optional
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

    ERR: Optional[_ERR] = Field(
        default=None,
        title="ERR",
        description="Optional",
    )

    NTE: Optional[List[_NTE]] = Field(
        default=None,
        title="NTE",
        description="Optional, repeating",
    )

    PATIENT: Optional[_RRD_O02_PATIENT] = Field(
        default=None,
        title="PATIENT",
        description="Optional",
    )

    model_config = {"populate_by_name": True}

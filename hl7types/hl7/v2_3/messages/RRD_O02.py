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
    """ORR - Order response (also RRE, RRD, RRG, RRA,.

    Attributes:
        MSH (MSH): Message header segment, required
        MSA (MSA): Message acknowledgement segment, required
        ERR (Optional[ERR]): Error segment, optional
        NTE (Optional[List[NTE]]): Notes and comments segment, optional
        PATIENT (Optional[RRD_O02_PATIENT]): optional
    """

    MSH: _MSH = Field(
        title="MSH",
        description="Message header segment",
    )

    MSA: _MSA = Field(
        title="MSA",
        description="Message acknowledgement segment",
    )

    ERR: Optional[_ERR] = Field(
        default=None,
        title="ERR",
        description="Error segment",
    )

    NTE: Optional[List[_NTE]] = Field(
        default=None,
        title="NTE",
        description="Notes and comments segment",
    )

    PATIENT: Optional[_RRD_O02_PATIENT] = Field(
        default=None,
        title="PATIENT",
    )

    model_config = {"populate_by_name": True}

"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.4
Class: RPR_I03
Type: Message
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import ConfigDict, Field
from hl7types.hl7 import HL7Model

from ..segments.MSA import MSA
from ..segments.MSH import MSH
from ..segments.NTE import NTE
from ..segments.PID import PID

from ..groups.RPR_I03_PROVIDER import RPR_I03_PROVIDER

_MSA = MSA
_MSH = MSH
_NTE = NTE
_PID = PID
_RPR_I03_PROVIDER = RPR_I03_PROVIDER


class RPR_I03(HL7Model):
    """RQI/RPR - Request/receipt of patient selection list (S11).

    Attributes:
        MSH (MSH): Message Header, required
        MSA (MSA): Message Acknowledgment, required
        PROVIDER (List[RPR_I03_PROVIDER]): required
        PID (Optional[List[PID]]): Patient identification, optional
        NTE (Optional[List[NTE]]): Notes and Comments, optional
    """

    MSH: _MSH = Field(
        title="MSH",
        description="Message Header",
    )

    MSA: _MSA = Field(
        title="MSA",
        description="Message Acknowledgment",
    )

    PROVIDER: List[_RPR_I03_PROVIDER] = Field(
        min_length=1,
        title="PROVIDER",
    )

    PID: Optional[List[_PID]] = Field(
        default=None,
        title="PID",
        description="Patient identification",
    )

    NTE: Optional[List[_NTE]] = Field(
        default=None,
        title="NTE",
        description="Notes and Comments",
    )

    model_config = ConfigDict(populate_by_name=True)

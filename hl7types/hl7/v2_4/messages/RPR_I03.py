"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.4
Class: RPR_I03
Type: Message
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
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
    """HL7 v2 RPR_I03 message.

    Attributes:
        MSH (MSH): required
        MSA (MSA): required
        PROVIDER (List[RPR_I03_PROVIDER]): required
        PID (Optional[List[PID]]): optional
        NTE (Optional[List[NTE]]): optional
    """

    MSH: _MSH = Field(
        title="MSH",
        description="Required",
    )

    MSA: _MSA = Field(
        title="MSA",
        description="Required",
    )

    PROVIDER: List[_RPR_I03_PROVIDER] = Field(
        min_length=1,
        title="PROVIDER",
        description="Required, repeating",
    )

    PID: Optional[List[_PID]] = Field(
        default=None,
        title="PID",
        description="Optional, repeating",
    )

    NTE: Optional[List[_NTE]] = Field(
        default=None,
        title="NTE",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}

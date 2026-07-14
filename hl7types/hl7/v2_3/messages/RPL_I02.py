"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3
Class: RPL_I02
Type: Message
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.DSC import DSC
from ..segments.DSP import DSP
from ..segments.MSA import MSA
from ..segments.MSH import MSH
from ..segments.NTE import NTE

from ..groups.RPL_I02_PROVIDER import RPL_I02_PROVIDER

_DSC = DSC
_DSP = DSP
_MSA = MSA
_MSH = MSH
_NTE = NTE
_RPL_I02_PROVIDER = RPL_I02_PROVIDER


class RPL_I02(HL7Model):
    """RQI/RPL - Request/receipt of patient selection display list.

    Attributes:
        MSH (MSH): Message header segment, required
        MSA (MSA): Message acknowledgement segment, required
        PROVIDER (List[RPL_I02_PROVIDER]): required
        NTE (Optional[List[NTE]]): Notes and comments segment, optional
        DSP (Optional[List[DSP]]): Display data segment, optional
        DSC (Optional[DSC]): Continuation pointer segment, optional
    """

    MSH: _MSH = Field(
        title="MSH",
        description="Message header segment",
    )

    MSA: _MSA = Field(
        title="MSA",
        description="Message acknowledgement segment",
    )

    PROVIDER: List[_RPL_I02_PROVIDER] = Field(
        min_length=1,
        title="PROVIDER",
    )

    NTE: Optional[List[_NTE]] = Field(
        default=None,
        title="NTE",
        description="Notes and comments segment",
    )

    DSP: Optional[List[_DSP]] = Field(
        default=None,
        title="DSP",
        description="Display data segment",
    )

    DSC: Optional[_DSC] = Field(
        default=None,
        title="DSC",
        description="Continuation pointer segment",
    )

    model_config = {"populate_by_name": True}

"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5
Class: ADT_A18
Type: Message
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.EVN import EVN
from ..segments.MRG import MRG
from ..segments.MSH import MSH
from ..segments.PD1 import PD1
from ..segments.PID import PID
from ..segments.PV1 import PV1
from ..segments.SFT import SFT

_EVN = EVN
_MRG = MRG
_MSH = MSH
_PD1 = PD1
_PID = PID
_PV1 = PV1
_SFT = SFT


class ADT_A18(HL7Model):
    """HL7 v2 ADT_A18 message.

    Attributes:
        MSH (MSH): required
        SFT (Optional[List[SFT]]): optional
        EVN (EVN): required
        PID (PID): required
        PD1 (Optional[PD1]): optional
        MRG (MRG): required
        PV1 (PV1): required
    """

    MSH: _MSH = Field(
        title="MSH",
        description="Required",
    )

    SFT: Optional[List[_SFT]] = Field(
        default=None,
        title="SFT",
        description="Optional, repeating",
    )

    EVN: _EVN = Field(
        title="EVN",
        description="Required",
    )

    PID: _PID = Field(
        title="PID",
        description="Required",
    )

    PD1: Optional[_PD1] = Field(
        default=None,
        title="PD1",
        description="Optional",
    )

    MRG: _MRG = Field(
        title="MRG",
        description="Required",
    )

    PV1: _PV1 = Field(
        title="PV1",
        description="Required",
    )

    model_config = {"populate_by_name": True}

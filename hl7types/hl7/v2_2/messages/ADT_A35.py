"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.2
Class: ADT_A35
Type: Message
"""
from __future__ import annotations

from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.EVN import EVN
from ..segments.MRG import MRG
from ..segments.MSH import MSH
from ..segments.PID import PID

_EVN = EVN
_MRG = MRG
_MSH = MSH
_PID = PID


class ADT_A35(HL7Model):
    """HL7 v2 ADT_A35 message.

    Attributes:
        MSH (MSH): required
        EVN (EVN): required
        PID (PID): required
        MRG (MRG): required
    """

    MSH: _MSH = Field(
        title="MSH",
        description="Required",
    )

    EVN: _EVN = Field(
        title="EVN",
        description="Required",
    )

    PID: _PID = Field(
        title="PID",
        description="Required",
    )

    MRG: _MRG = Field(
        title="MRG",
        description="Required",
    )

    model_config = {"populate_by_name": True}

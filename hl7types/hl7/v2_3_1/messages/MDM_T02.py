"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3.1
Class: MDM_T02
Type: Message
"""
from __future__ import annotations

from typing import List
from pydantic import ConfigDict, Field
from hl7types.hl7 import HL7Model

from ..segments.EVN import EVN
from ..segments.MSH import MSH
from ..segments.OBX import OBX
from ..segments.PID import PID
from ..segments.PV1 import PV1
from ..segments.TXA import TXA

_EVN = EVN
_MSH = MSH
_OBX = OBX
_PID = PID
_PV1 = PV1
_TXA = TXA


class MDM_T02(HL7Model):
    """MDM/ACK - Original document notification and content.

    Attributes:
        MSH (MSH): MSH - message header segment, required
        EVN (EVN): EVN - event type segment, required
        PID (PID): PID - patient identification segment, required
        PV1 (PV1): PV1 - patient visit segment-, required
        TXA (TXA): Document notification segment, required
        OBX (List[OBX]): OBX - observation/result segment, required
    """

    MSH: _MSH = Field(
        title="MSH",
        description="MSH - message header segment",
    )

    EVN: _EVN = Field(
        title="EVN",
        description="EVN - event type segment",
    )

    PID: _PID = Field(
        title="PID",
        description="PID - patient identification segment",
    )

    PV1: _PV1 = Field(
        title="PV1",
        description="PV1 - patient visit segment-",
    )

    TXA: _TXA = Field(
        title="TXA",
        description="Document notification segment",
    )

    OBX: List[_OBX] = Field(
        min_length=1,
        title="OBX",
        description="OBX - observation/result segment",
    )

    model_config = ConfigDict(populate_by_name=True)

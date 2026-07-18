"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3
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
        MSH (MSH): Message header segment, required
        EVN (EVN): Event type, required
        PID (PID): Patient Identification, required
        PV1 (PV1): Patient visit, required
        TXA (TXA): Document notification segment, required
        OBX (List[OBX]): Observation segment, required
    """

    MSH: _MSH = Field(
        title="MSH",
        description="Message header segment",
    )

    EVN: _EVN = Field(
        title="EVN",
        description="Event type",
    )

    PID: _PID = Field(
        title="PID",
        description="Patient Identification",
    )

    PV1: _PV1 = Field(
        title="PV1",
        description="Patient visit",
    )

    TXA: _TXA = Field(
        title="TXA",
        description="Document notification segment",
    )

    OBX: List[_OBX] = Field(
        min_length=1,
        title="OBX",
        description="Observation segment",
    )

    model_config = ConfigDict(populate_by_name=True)

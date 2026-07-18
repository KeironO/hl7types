"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.2
Class: ADT_A17
Type: Message
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import ConfigDict, Field
from hl7types.hl7 import HL7Model

from ..segments.EVN import EVN
from ..segments.MSH import MSH
from ..segments.OBX import OBX
from ..segments.PID import PID
from ..segments.PV1 import PV1
from ..segments.PV2 import PV2

_EVN = EVN
_MSH = MSH
_OBX = OBX
_PID = PID
_PV1 = PV1
_PV2 = PV2


class ADT_A17(HL7Model):
    """HL7 v2 ADT_A17 message.

    Attributes:
        MSH (MSH): MESSAGE HEADER, required
        EVN (EVN): EVENT TYPE, required
        PID (PID): PATIENT IDENTIFICATION, required
        PV1 (PV1): PATIENT VISIT, required
        PV2 (Optional[PV2]): PATIENT VISIT - additional information, optional
        OBX (Optional[List[OBX]]): OBSERVATION RESULT, optional
    """

    MSH: _MSH = Field(
        title="MSH",
        description="MESSAGE HEADER",
    )

    EVN: _EVN = Field(
        title="EVN",
        description="EVENT TYPE",
    )

    PID: _PID = Field(
        title="PID",
        description="PATIENT IDENTIFICATION",
    )

    PV1: _PV1 = Field(
        title="PV1",
        description="PATIENT VISIT",
    )

    PV2: Optional[_PV2] = Field(
        default=None,
        title="PV2",
        description="PATIENT VISIT - additional information",
    )

    OBX: Optional[List[_OBX]] = Field(
        default=None,
        title="OBX",
        description="OBSERVATION RESULT",
    )

    model_config = ConfigDict(populate_by_name=True)

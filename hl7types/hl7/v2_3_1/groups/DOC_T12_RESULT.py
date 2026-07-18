"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3.1
Class: DOC_T12.RESULT
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import ConfigDict, Field
from hl7types.hl7 import HL7Model

from ..segments.EVN import EVN
from ..segments.OBX import OBX
from ..segments.PID import PID
from ..segments.PV1 import PV1
from ..segments.TXA import TXA

_EVN = EVN
_OBX = OBX
_PID = PID
_PV1 = PV1
_TXA = TXA


class DOC_T12_RESULT(HL7Model):
    """HL7 v2 DOC_T12.RESULT group.

    Attributes:
        EVN (Optional[EVN]): EVN - event type segment, optional
        PID (PID): PID - patient identification segment, required
        PV1 (PV1): PV1 - patient visit segment-, required
        TXA (TXA): Document notification segment, required
        OBX (Optional[List[OBX]]): OBX - observation/result segment, optional
    """

    EVN: Optional[_EVN] = Field(
        default=None,
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

    OBX: Optional[List[_OBX]] = Field(
        default=None,
        title="OBX",
        description="OBX - observation/result segment",
    )

    model_config = ConfigDict(populate_by_name=True)

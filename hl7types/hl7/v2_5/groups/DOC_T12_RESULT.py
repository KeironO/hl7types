"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5
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
        EVN (Optional[EVN]): Event Type, optional
        PID (PID): Patient Identification, required
        PV1 (PV1): Patient Visit, required
        TXA (TXA): Transcription Document Header, required
        OBX (Optional[List[OBX]]): Observation/Result, optional
    """

    EVN: Optional[_EVN] = Field(
        default=None,
        title="EVN",
        description="Event Type",
    )

    PID: _PID = Field(
        title="PID",
        description="Patient Identification",
    )

    PV1: _PV1 = Field(
        title="PV1",
        description="Patient Visit",
    )

    TXA: _TXA = Field(
        title="TXA",
        description="Transcription Document Header",
    )

    OBX: Optional[List[_OBX]] = Field(
        default=None,
        title="OBX",
        description="Observation/Result",
    )

    model_config = ConfigDict(populate_by_name=True)

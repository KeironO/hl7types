"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7.1
Class: EHC_E13.RESPONSE
Type: Group
"""
from __future__ import annotations

from typing import Optional
from pydantic import ConfigDict, Field
from hl7types.hl7 import HL7Model

from ..segments.NTE import NTE
from ..segments.OBX import OBX
from ..segments.TXA import TXA

_NTE = NTE
_OBX = OBX
_TXA = TXA


class EHC_E13_RESPONSE(HL7Model):
    """HL7 v2 EHC_E13.RESPONSE group.

    Attributes:
        OBX (OBX): Observation/Result, required
        NTE (Optional[NTE]): Notes and Comments, optional
        TXA (Optional[TXA]): Transcription Document Header, optional
    """

    OBX: _OBX = Field(
        title="OBX",
        description="Observation/Result",
    )

    NTE: Optional[_NTE] = Field(
        default=None,
        title="NTE",
        description="Notes and Comments",
    )

    TXA: Optional[_TXA] = Field(
        default=None,
        title="TXA",
        description="Transcription Document Header",
    )

    model_config = ConfigDict(populate_by_name=True)

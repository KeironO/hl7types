"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.1
Class: CQU_I19.MEDICATION_ENCODING_DETAIL
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.RXC import RXC
from ..segments.RXE import RXE
from ..segments.RXR import RXR

from .CQU_I19_MEDICATION_ENCODING_OBSERVATION import CQU_I19_MEDICATION_ENCODING_OBSERVATION

_CQU_I19_MEDICATION_ENCODING_OBSERVATION = CQU_I19_MEDICATION_ENCODING_OBSERVATION
_RXC = RXC
_RXE = RXE
_RXR = RXR


class CQU_I19_MEDICATION_ENCODING_DETAIL(HL7Model):
    """HL7 v2 CQU_I19.MEDICATION_ENCODING_DETAIL group.

    Attributes:
        RXE (RXE): required
        RXR (List[RXR]): required
        RXC (Optional[List[RXC]]): optional
        MEDICATION_ENCODING_OBSERVATION (Optional[List[CQU_I19_MEDICATION_ENCODING_OBSERVATION]]): optional
    """

    RXE: _RXE = Field(
        default=...,
        title="RXE",
        description="Required",
    )

    RXR: List[_RXR] = Field(
        default=...,
        title="RXR",
        description="Required, repeating",
    )

    RXC: Optional[List[_RXC]] = Field(
        default=None,
        title="RXC",
        description="Optional, repeating",
    )

    MEDICATION_ENCODING_OBSERVATION: Optional[List[_CQU_I19_MEDICATION_ENCODING_OBSERVATION]] = Field(
        default=None,
        title="MEDICATION_ENCODING_OBSERVATION",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}

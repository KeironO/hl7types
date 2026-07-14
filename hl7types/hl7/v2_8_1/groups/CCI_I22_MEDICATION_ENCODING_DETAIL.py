"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.1
Class: CCI_I22.MEDICATION_ENCODING_DETAIL
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.RXC import RXC
from ..segments.RXE import RXE
from ..segments.RXR import RXR

from .CCI_I22_MEDICATION_ENCODING_OBSERVATION import CCI_I22_MEDICATION_ENCODING_OBSERVATION

_CCI_I22_MEDICATION_ENCODING_OBSERVATION = CCI_I22_MEDICATION_ENCODING_OBSERVATION
_RXC = RXC
_RXE = RXE
_RXR = RXR


class CCI_I22_MEDICATION_ENCODING_DETAIL(HL7Model):
    """HL7 v2 CCI_I22.MEDICATION_ENCODING_DETAIL group.

    Attributes:
        RXE (RXE): Pharmacy/Treatment Encoded Order, required
        RXR (List[RXR]): Pharmacy/Treatment Route, required
        RXC (Optional[List[RXC]]): Pharmacy/Treatment Component Order, optional
        MEDICATION_ENCODING_OBSERVATION (Optional[List[CCI_I22_MEDICATION_ENCODING_OBSERVATION]]): optional
    """

    RXE: _RXE = Field(
        title="RXE",
        description="Pharmacy/Treatment Encoded Order",
    )

    RXR: List[_RXR] = Field(
        min_length=1,
        title="RXR",
        description="Pharmacy/Treatment Route",
    )

    RXC: Optional[List[_RXC]] = Field(
        default=None,
        title="RXC",
        description="Pharmacy/Treatment Component Order",
    )

    MEDICATION_ENCODING_OBSERVATION: Optional[List[_CCI_I22_MEDICATION_ENCODING_OBSERVATION]] = Field(
        default=None,
        title="MEDICATION_ENCODING_OBSERVATION",
    )

    model_config = {"populate_by_name": True}

"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5.1
Class: OMP_O09
Type: Message
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import BaseModel, Field

from ..segments.MSH import MSH
from ..segments.NTE import NTE
from ..segments.SFT import SFT

from ..groups.OMP_O09_ORDER import OMP_O09_ORDER
from ..groups.OMP_O09_PATIENT import OMP_O09_PATIENT

_MSH = MSH
_NTE = NTE
_OMP_O09_ORDER = OMP_O09_ORDER
_OMP_O09_PATIENT = OMP_O09_PATIENT
_SFT = SFT


class OMP_O09(BaseModel):
    """HL7 v2 OMP_O09 message.

    Attributes:
        MSH (MSH): required
        SFT (Optional[List[SFT]]): optional
        NTE (Optional[List[NTE]]): optional
        PATIENT (Optional[OMP_O09_PATIENT]): optional
        ORDER (List[OMP_O09_ORDER]): required
    """

    MSH: _MSH = Field(
        default=...,
        title="MSH",
        description="Required",
    )

    SFT: Optional[List[_SFT]] = Field(
        default=None,
        title="SFT",
        description="Optional, repeating",
    )

    NTE: Optional[List[_NTE]] = Field(
        default=None,
        title="NTE",
        description="Optional, repeating",
    )

    PATIENT: Optional[_OMP_O09_PATIENT] = Field(
        default=None,
        title="PATIENT",
        description="Optional",
    )

    ORDER: List[_OMP_O09_ORDER] = Field(
        default=...,
        title="ORDER",
        description="Required, repeating",
    )

    model_config = {"populate_by_name": True}

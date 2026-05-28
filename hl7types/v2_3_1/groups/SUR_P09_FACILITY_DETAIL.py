"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3.1
Class: SUR_P09.FACILITY_DETAIL
Type: Group
"""
from _future__ import annotations

from typing import Optional
from pydantic import BaseModel, Field

from ..segments.FAC import FAC
from ..segments.NTE import NTE
from ..segments.PDC import PDC

_FAC = FAC
_NTE = NTE
_PDC = PDC


class SUR_P09_FACILITY_DETAIL(BaseModel):
    """HL7 v2 SUR_P09.FACILITY_DETAIL group.

    Attributes:
        FAC (FAC): required
        PDC (PDC): required
        NTE (NTE): required
    """

    FAC: _FAC = Field(
        default=...,
        title="FAC",
        description="Required",
    )

    PDC: _PDC = Field(
        default=...,
        title="PDC",
        description="Required",
    )

    NTE: _NTE = Field(
        default=...,
        title="NTE",
        description="Required",
    )

    model_config = {"populate_by_name": True}

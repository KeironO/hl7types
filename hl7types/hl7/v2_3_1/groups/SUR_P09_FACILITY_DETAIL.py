"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3.1
Class: SUR_P09.FACILITY_DETAIL
Type: Group
"""
from __future__ import annotations

from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.FAC import FAC
from ..segments.NTE import NTE
from ..segments.PDC import PDC

_FAC = FAC
_NTE = NTE
_PDC = PDC


class SUR_P09_FACILITY_DETAIL(HL7Model):
    """HL7 v2 SUR_P09.FACILITY_DETAIL group.

    Attributes:
        FAC (FAC): FAC - facility segment, required
        PDC (PDC): PDC - product detail country segment, required
        NTE (NTE): NTE - notes and comments segment, required
    """

    FAC: _FAC = Field(
        title="FAC",
        description="FAC - facility segment",
    )

    PDC: _PDC = Field(
        title="PDC",
        description="PDC - product detail country segment",
    )

    NTE: _NTE = Field(
        title="NTE",
        description="NTE - notes and comments segment",
    )

    model_config = {"populate_by_name": True}

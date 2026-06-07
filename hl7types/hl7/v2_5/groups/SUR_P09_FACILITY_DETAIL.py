"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5
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
        FAC (FAC): required
        PDC (PDC): required
        NTE (NTE): required
    """

    FAC: _FAC = Field(
        title="FAC",
        description="Required",
    )

    PDC: _PDC = Field(
        title="PDC",
        description="Required",
    )

    NTE: _NTE = Field(
        title="NTE",
        description="Required",
    )

    model_config = {"populate_by_name": True}

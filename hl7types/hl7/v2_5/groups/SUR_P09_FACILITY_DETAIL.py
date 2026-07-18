"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5
Class: SUR_P09.FACILITY_DETAIL
Type: Group
"""
from __future__ import annotations

from pydantic import ConfigDict, Field
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
        FAC (FAC): Facility, required
        PDC (PDC): Product Detail Country, required
        NTE (NTE): Notes and Comments, required
    """

    FAC: _FAC = Field(
        title="FAC",
        description="Facility",
    )

    PDC: _PDC = Field(
        title="PDC",
        description="Product Detail Country",
    )

    NTE: _NTE = Field(
        title="NTE",
        description="Notes and Comments",
    )

    model_config = ConfigDict(populate_by_name=True)

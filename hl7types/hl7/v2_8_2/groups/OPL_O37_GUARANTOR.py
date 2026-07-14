"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.2
Class: OPL_O37.GUARANTOR
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.GT1 import GT1
from ..segments.NTE import NTE

_GT1 = GT1
_NTE = NTE


class OPL_O37_GUARANTOR(HL7Model):
    """HL7 v2 OPL_O37.GUARANTOR group.

    Attributes:
        GT1 (GT1): Guarantor, required
        NTE (Optional[List[NTE]]): Notes and Comments, optional
    """

    GT1: _GT1 = Field(
        title="GT1",
        description="Guarantor",
    )

    NTE: Optional[List[_NTE]] = Field(
        default=None,
        title="NTE",
        description="Notes and Comments",
    )

    model_config = {"populate_by_name": True}

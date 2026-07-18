"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.1
Class: MFN_M16.STERILIZATION
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import ConfigDict, Field
from hl7types.hl7 import HL7Model

from ..segments.NTE import NTE
from ..segments.STZ import STZ

_NTE = NTE
_STZ = STZ


class MFN_M16_STERILIZATION(HL7Model):
    """HL7 v2 MFN_M16.STERILIZATION group.

    Attributes:
        STZ (STZ): Sterilization Parameter, required
        NTE (Optional[List[NTE]]): Notes and Comments, optional
    """

    STZ: _STZ = Field(
        title="STZ",
        description="Sterilization Parameter",
    )

    NTE: Optional[List[_NTE]] = Field(
        default=None,
        title="NTE",
        description="Notes and Comments",
    )

    model_config = ConfigDict(populate_by_name=True)

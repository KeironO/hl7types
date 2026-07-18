"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.2
Class: NMD_N01.CLOCK
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import ConfigDict, Field
from hl7types.hl7 import HL7Model

from ..segments.NCK import NCK
from ..segments.NTE import NTE

_NCK = NCK
_NTE = NTE


class NMD_N01_CLOCK(HL7Model):
    """HL7 v2 NMD_N01.CLOCK group.

    Attributes:
        NCK (NCK): System Clock, required
        NTE (Optional[List[NTE]]): NOTES AND COMMENTS, optional
    """

    NCK: _NCK = Field(
        title="NCK",
        description="System Clock",
    )

    NTE: Optional[List[_NTE]] = Field(
        default=None,
        title="NTE",
        description="NOTES AND COMMENTS",
    )

    model_config = ConfigDict(populate_by_name=True)

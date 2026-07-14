"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5.1
Class: NMD_N02.CLOCK
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.NCK import NCK
from ..segments.NTE import NTE

_NCK = NCK
_NTE = NTE


class NMD_N02_CLOCK(HL7Model):
    """HL7 v2 NMD_N02.CLOCK group.

    Attributes:
        NCK (NCK): System Clock, required
        NTE (Optional[List[NTE]]): Notes and Comments, optional
    """

    NCK: _NCK = Field(
        title="NCK",
        description="System Clock",
    )

    NTE: Optional[List[_NTE]] = Field(
        default=None,
        title="NTE",
        description="Notes and Comments",
    )

    model_config = {"populate_by_name": True}

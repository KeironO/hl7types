"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5.1
Class: ORF_R04.PIDNTE_SUPPGRP
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.NTE import NTE
from ..segments.PID import PID

_NTE = NTE
_PID = PID


class ORF_R04_PIDNTE_SUPPGRP(HL7Model):
    """HL7 v2 ORF_R04.PIDNTE_SUPPGRP group.

    Attributes:
        PID (PID): required
        NTE (Optional[List[NTE]]): optional
    """

    PID: _PID = Field(
        title="PID",
        description="Required",
    )

    NTE: Optional[List[_NTE]] = Field(
        default=None,
        title="NTE",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}

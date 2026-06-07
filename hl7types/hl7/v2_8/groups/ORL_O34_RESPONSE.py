"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8
Class: ORL_O34.RESPONSE
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.ARV import ARV
from ..segments.PID import PID
from ..segments.PRT import PRT

from .ORL_O34_SPECIMEN import ORL_O34_SPECIMEN

_ARV = ARV
_ORL_O34_SPECIMEN = ORL_O34_SPECIMEN
_PID = PID
_PRT = PRT


class ORL_O34_RESPONSE(HL7Model):
    """HL7 v2 ORL_O34.RESPONSE group.

    Attributes:
        PID (PID): required
        PRT (Optional[List[PRT]]): optional
        ARV (Optional[List[ARV]]): optional
        SPECIMEN (List[ORL_O34_SPECIMEN]): required
    """

    PID: _PID = Field(
        title="PID",
        description="Required",
    )

    PRT: Optional[List[_PRT]] = Field(
        default=None,
        title="PRT",
        description="Optional, repeating",
    )

    ARV: Optional[List[_ARV]] = Field(
        default=None,
        title="ARV",
        description="Optional, repeating",
    )

    SPECIMEN: List[_ORL_O34_SPECIMEN] = Field(
        min_length=1,
        title="SPECIMEN",
        description="Required, repeating",
    )

    model_config = {"populate_by_name": True}

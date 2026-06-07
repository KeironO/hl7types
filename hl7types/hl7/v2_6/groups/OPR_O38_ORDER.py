"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.6
Class: OPR_O38.ORDER
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.NK1 import NK1
from ..segments.PID import PID

from .OPR_O38_SPECIMEN import OPR_O38_SPECIMEN

_NK1 = NK1
_OPR_O38_SPECIMEN = OPR_O38_SPECIMEN
_PID = PID


class OPR_O38_ORDER(HL7Model):
    """HL7 v2 OPR_O38.ORDER group.

    Attributes:
        NK1 (List[NK1]): required
        PID (Optional[PID]): optional
        SPECIMEN (Optional[List[OPR_O38_SPECIMEN]]): optional
    """

    NK1: List[_NK1] = Field(
        min_length=1,
        title="NK1",
        description="Required, repeating",
    )

    PID: Optional[_PID] = Field(
        default=None,
        title="PID",
        description="Optional",
    )

    SPECIMEN: Optional[List[_OPR_O38_SPECIMEN]] = Field(
        default=None,
        title="SPECIMEN",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}

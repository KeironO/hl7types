"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.2
Class: OPR_O38.ORDER
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.ARV import ARV
from ..segments.NK1 import NK1
from ..segments.PID import PID
from ..segments.PRT import PRT

from .OPR_O38_SPECIMEN import OPR_O38_SPECIMEN

_ARV = ARV
_NK1 = NK1
_OPR_O38_SPECIMEN = OPR_O38_SPECIMEN
_PID = PID
_PRT = PRT


class OPR_O38_ORDER(HL7Model):
    """HL7 v2 OPR_O38.ORDER group.

    Attributes:
        NK1 (List[NK1]): required
        PID (Optional[PID]): optional
        PRT (Optional[List[PRT]]): optional
        ARV (Optional[List[ARV]]): optional
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

    SPECIMEN: Optional[List[_OPR_O38_SPECIMEN]] = Field(
        default=None,
        title="SPECIMEN",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}

"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.2
Class: OPR_O38.ORDER
Type: Group
"""

from __future__ import annotations

from pydantic import BaseModel, Field

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


class OPR_O38_ORDER(BaseModel):
    """HL7 v2 OPR_O38.ORDER group.

    Attributes:
        NK1 (List[NK1]): required
        PID (Optional[PID]): optional
        PRT (Optional[List[PRT]]): optional
        ARV (Optional[List[ARV]]): optional
        SPECIMEN (Optional[List[OPR_O38_SPECIMEN]]): optional
    """

    NK1: list[_NK1] = Field(
        default=...,
        title="NK1",
        description="Required, repeating",
    )

    PID: _PID | None = Field(
        default=None,
        title="PID",
        description="Optional",
    )

    PRT: list[_PRT] | None = Field(
        default=None,
        title="PRT",
        description="Optional, repeating",
    )

    ARV: list[_ARV] | None = Field(
        default=None,
        title="ARV",
        description="Optional, repeating",
    )

    SPECIMEN: list[_OPR_O38_SPECIMEN] | None = Field(
        default=None,
        title="SPECIMEN",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}

"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8
Class: RAS_O17.PATIENT_VISIT
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.ARV import ARV
from ..segments.PRT import PRT
from ..segments.PV1 import PV1
from ..segments.PV2 import PV2

_ARV = ARV
_PRT = PRT
_PV1 = PV1
_PV2 = PV2


class RAS_O17_PATIENT_VISIT(HL7Model):
    """HL7 v2 RAS_O17.PATIENT_VISIT group.

    Attributes:
        PV1 (PV1): required
        PV2 (Optional[PV2]): optional
        PRT (Optional[List[PRT]]): optional
        ARV (Optional[List[ARV]]): optional
    """

    PV1: _PV1 = Field(
        title="PV1",
        description="Required",
    )

    PV2: Optional[_PV2] = Field(
        default=None,
        title="PV2",
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

    model_config = {"populate_by_name": True}

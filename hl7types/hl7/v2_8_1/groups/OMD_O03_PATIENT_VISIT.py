"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.1
Class: OMD_O03.PATIENT_VISIT
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.PRT import PRT
from ..segments.PV1 import PV1
from ..segments.PV2 import PV2

_PRT = PRT
_PV1 = PV1
_PV2 = PV2


class OMD_O03_PATIENT_VISIT(HL7Model):
    """HL7 v2 OMD_O03.PATIENT_VISIT group.

    Attributes:
        PV1 (PV1): required
        PV2 (Optional[PV2]): optional
        PRT (Optional[List[PRT]]): optional
    """

    PV1: _PV1 = Field(
        default=...,
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

    model_config = {"populate_by_name": True}

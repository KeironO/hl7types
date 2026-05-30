"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.1
Class: ORM_O01.PATIENT
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.NTE import NTE
from ..segments.PID import PID
from ..segments.PV1 import PV1

_NTE = NTE
_PID = PID
_PV1 = PV1


class ORM_O01_PATIENT(HL7Model):
    """HL7 v2 ORM_O01.PATIENT group.

    Attributes:
        PID (PID): required
        NTE (Optional[List[NTE]]): optional
        PV1 (Optional[PV1]): optional
    """

    PID: _PID = Field(
        default=...,
        title="PID",
        description="Required",
    )

    NTE: Optional[List[_NTE]] = Field(
        default=None,
        title="NTE",
        description="Optional, repeating",
    )

    PV1: Optional[_PV1] = Field(
        default=None,
        title="PV1",
        description="Optional",
    )

    model_config = {"populate_by_name": True}

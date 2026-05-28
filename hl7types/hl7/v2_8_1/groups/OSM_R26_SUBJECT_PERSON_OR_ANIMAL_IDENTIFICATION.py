"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.1
Class: OSM_R26.SUBJECT_PERSON_OR_ANIMAL_IDENTIFICATION
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import BaseModel, Field

from ..segments.ARV import ARV
from ..segments.NK1 import NK1
from ..segments.PID import PID
from ..segments.PRT import PRT

from .OSM_R26_PATIENT_OBSERVATION import OSM_R26_PATIENT_OBSERVATION

_ARV = ARV
_NK1 = NK1
_OSM_R26_PATIENT_OBSERVATION = OSM_R26_PATIENT_OBSERVATION
_PID = PID
_PRT = PRT


class OSM_R26_SUBJECT_PERSON_OR_ANIMAL_IDENTIFICATION(BaseModel):
    """HL7 v2 OSM_R26.SUBJECT_PERSON_OR_ANIMAL_IDENTIFICATION group.

    Attributes:
        PID (PID): required
        PRT (Optional[List[PRT]]): optional
        ARV (Optional[List[ARV]]): optional
        PATIENT_OBSERVATION (Optional[List[OSM_R26_PATIENT_OBSERVATION]]): optional
        NK1 (Optional[List[NK1]]): optional
    """

    PID: _PID = Field(
        default=...,
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

    PATIENT_OBSERVATION: Optional[List[_OSM_R26_PATIENT_OBSERVATION]] = Field(
        default=None,
        title="PATIENT_OBSERVATION",
        description="Optional, repeating",
    )

    NK1: Optional[List[_NK1]] = Field(
        default=None,
        title="NK1",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}

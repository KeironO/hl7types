"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7
Class: OSM_R26.SUBJECT_POPULATION_LOCATION_IDENTIFICATION
Type: Group
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..segments.NK1 import NK1
from ..segments.PRT import PRT
from ..segments.PV1 import PV1
from .OSM_R26_PATIENT_INFORMATION import OSM_R26_PATIENT_INFORMATION
from .OSM_R26_PATIENT_VISIT_OBSERVATION import OSM_R26_PATIENT_VISIT_OBSERVATION

_NK1 = NK1
_OSM_R26_PATIENT_INFORMATION = OSM_R26_PATIENT_INFORMATION
_OSM_R26_PATIENT_VISIT_OBSERVATION = OSM_R26_PATIENT_VISIT_OBSERVATION
_PRT = PRT
_PV1 = PV1


class OSM_R26_SUBJECT_POPULATION_LOCATION_IDENTIFICATION(BaseModel):
    """HL7 v2 OSM_R26.SUBJECT_POPULATION_LOCATION_IDENTIFICATION group.

    Attributes:
        PV1 (PV1): required
        PRT (Optional[List[PRT]]): optional
        PATIENT_VISIT_OBSERVATION (Optional[List[OSM_R26_PATIENT_VISIT_OBSERVATION]]): optional
        PATIENT_INFORMATION (Optional[OSM_R26_PATIENT_INFORMATION]): optional
        NK1 (Optional[List[NK1]]): optional
    """

    PV1: _PV1 = Field(
        default=...,
        title="PV1",
        description="Required",
    )

    PRT: list[_PRT] | None = Field(
        default=None,
        title="PRT",
        description="Optional, repeating",
    )

    PATIENT_VISIT_OBSERVATION: list[_OSM_R26_PATIENT_VISIT_OBSERVATION] | None = Field(
        default=None,
        title="PATIENT_VISIT_OBSERVATION",
        description="Optional, repeating",
    )

    PATIENT_INFORMATION: _OSM_R26_PATIENT_INFORMATION | None = Field(
        default=None,
        title="PATIENT_INFORMATION",
        description="Optional",
    )

    NK1: list[_NK1] | None = Field(
        default=None,
        title="NK1",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}

"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8
Class: OSM_R26.SUBJECT_POPULATION_OR_LOCATION_IDENTIFICATION
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

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


class OSM_R26_SUBJECT_POPULATION_OR_LOCATION_IDENTIFICATION(HL7Model):
    """HL7 v2 OSM_R26.SUBJECT_POPULATION_OR_LOCATION_IDENTIFICATION group.

    Attributes:
        PV1 (PV1): Patient Visit, required
        PRT (Optional[List[PRT]]): Participation Information, optional
        PATIENT_VISIT_OBSERVATION (Optional[List[OSM_R26_PATIENT_VISIT_OBSERVATION]]): optional
        PATIENT_INFORMATION (Optional[OSM_R26_PATIENT_INFORMATION]): optional
        NK1 (Optional[List[NK1]]): Next of Kin / Associated Parties, optional
    """

    PV1: _PV1 = Field(
        title="PV1",
        description="Patient Visit",
    )

    PRT: Optional[List[_PRT]] = Field(
        default=None,
        title="PRT",
        description="Participation Information",
    )

    PATIENT_VISIT_OBSERVATION: Optional[List[_OSM_R26_PATIENT_VISIT_OBSERVATION]] = Field(
        default=None,
        title="PATIENT_VISIT_OBSERVATION",
    )

    PATIENT_INFORMATION: Optional[_OSM_R26_PATIENT_INFORMATION] = Field(
        default=None,
        title="PATIENT_INFORMATION",
    )

    NK1: Optional[List[_NK1]] = Field(
        default=None,
        title="NK1",
        description="Next of Kin / Associated Parties",
    )

    model_config = {"populate_by_name": True}

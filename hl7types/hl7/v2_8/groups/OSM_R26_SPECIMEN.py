"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8
Class: OSM_R26.SPECIMEN
Type: Group
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..segments.PRT import PRT
from ..segments.SPM import SPM
from .OSM_R26_CONTAINER import OSM_R26_CONTAINER
from .OSM_R26_SPECIMEN_OBSERVATION import OSM_R26_SPECIMEN_OBSERVATION
from .OSM_R26_SUBJECT_PERSON_OR_ANIMAL_IDENTIFICATION import (
    OSM_R26_SUBJECT_PERSON_OR_ANIMAL_IDENTIFICATION,
)
from .OSM_R26_SUBJECT_POPULATION_OR_LOCATION_IDENTIFICATION import (
    OSM_R26_SUBJECT_POPULATION_OR_LOCATION_IDENTIFICATION,
)

_OSM_R26_CONTAINER = OSM_R26_CONTAINER
_OSM_R26_SPECIMEN_OBSERVATION = OSM_R26_SPECIMEN_OBSERVATION
_OSM_R26_SUBJECT_PERSON_OR_ANIMAL_IDENTIFICATION = OSM_R26_SUBJECT_PERSON_OR_ANIMAL_IDENTIFICATION
_OSM_R26_SUBJECT_POPULATION_OR_LOCATION_IDENTIFICATION = (
    OSM_R26_SUBJECT_POPULATION_OR_LOCATION_IDENTIFICATION
)
_PRT = PRT
_SPM = SPM


class OSM_R26_SPECIMEN(BaseModel):
    """HL7 v2 OSM_R26.SPECIMEN group.

    Attributes:
        SPM (SPM): required
        PRT (Optional[List[PRT]]): optional
        SPECIMEN_OBSERVATION (Optional[List[OSM_R26_SPECIMEN_OBSERVATION]]): optional
        CONTAINER (Optional[List[OSM_R26_CONTAINER]]): optional
        SUBJECT_PERSON_OR_ANIMAL_IDENTIFICATION (Optional[OSM_R26_SUBJECT_PERSON_OR_ANIMAL_IDENTIFICATION]): optional
        SUBJECT_POPULATION_OR_LOCATION_IDENTIFICATION (Optional[OSM_R26_SUBJECT_POPULATION_OR_LOCATION_IDENTIFICATION]): optional
    """

    SPM: _SPM = Field(
        default=...,
        title="SPM",
        description="Required",
    )

    PRT: list[_PRT] | None = Field(
        default=None,
        title="PRT",
        description="Optional, repeating",
    )

    SPECIMEN_OBSERVATION: list[_OSM_R26_SPECIMEN_OBSERVATION] | None = Field(
        default=None,
        title="SPECIMEN_OBSERVATION",
        description="Optional, repeating",
    )

    CONTAINER: list[_OSM_R26_CONTAINER] | None = Field(
        default=None,
        title="CONTAINER",
        description="Optional, repeating",
    )

    SUBJECT_PERSON_OR_ANIMAL_IDENTIFICATION: (
        _OSM_R26_SUBJECT_PERSON_OR_ANIMAL_IDENTIFICATION | None
    ) = Field(
        default=None,
        title="SUBJECT_PERSON_OR_ANIMAL_IDENTIFICATION",
        description="Optional",
    )

    SUBJECT_POPULATION_OR_LOCATION_IDENTIFICATION: (
        _OSM_R26_SUBJECT_POPULATION_OR_LOCATION_IDENTIFICATION | None
    ) = Field(
        default=None,
        title="SUBJECT_POPULATION_OR_LOCATION_IDENTIFICATION",
        description="Optional",
    )

    model_config = {"populate_by_name": True}

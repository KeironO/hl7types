"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.1
Class: OSM_R26.SPECIMEN
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import ConfigDict, Field
from hl7types.hl7 import HL7Model

from ..segments.PRT import PRT
from ..segments.SPM import SPM

from .OSM_R26_CONTAINER import OSM_R26_CONTAINER
from .OSM_R26_SPECIMEN_OBSERVATION import OSM_R26_SPECIMEN_OBSERVATION
from .OSM_R26_SUBJECT_PERSON_OR_ANIMAL_IDENTIFICATION import OSM_R26_SUBJECT_PERSON_OR_ANIMAL_IDENTIFICATION
from .OSM_R26_SUBJECT_POPULATION_OR_LOCATION_IDENTIFICATION import OSM_R26_SUBJECT_POPULATION_OR_LOCATION_IDENTIFICATION

_OSM_R26_CONTAINER = OSM_R26_CONTAINER
_OSM_R26_SPECIMEN_OBSERVATION = OSM_R26_SPECIMEN_OBSERVATION
_OSM_R26_SUBJECT_PERSON_OR_ANIMAL_IDENTIFICATION = OSM_R26_SUBJECT_PERSON_OR_ANIMAL_IDENTIFICATION
_OSM_R26_SUBJECT_POPULATION_OR_LOCATION_IDENTIFICATION = OSM_R26_SUBJECT_POPULATION_OR_LOCATION_IDENTIFICATION
_PRT = PRT
_SPM = SPM


class OSM_R26_SPECIMEN(HL7Model):
    """HL7 v2 OSM_R26.SPECIMEN group.

    Attributes:
        SPM (SPM): Specimen, required
        PRT (Optional[List[PRT]]): Participation Information, optional
        SPECIMEN_OBSERVATION (Optional[List[OSM_R26_SPECIMEN_OBSERVATION]]): optional
        CONTAINER (Optional[List[OSM_R26_CONTAINER]]): optional
        SUBJECT_PERSON_OR_ANIMAL_IDENTIFICATION (Optional[OSM_R26_SUBJECT_PERSON_OR_ANIMAL_IDENTIFICATION]): optional
        SUBJECT_POPULATION_OR_LOCATION_IDENTIFICATION (Optional[OSM_R26_SUBJECT_POPULATION_OR_LOCATION_IDENTIFICATION]): optional
    """

    SPM: _SPM = Field(
        title="SPM",
        description="Specimen",
    )

    PRT: Optional[List[_PRT]] = Field(
        default=None,
        title="PRT",
        description="Participation Information",
    )

    SPECIMEN_OBSERVATION: Optional[List[_OSM_R26_SPECIMEN_OBSERVATION]] = Field(
        default=None,
        title="SPECIMEN_OBSERVATION",
    )

    CONTAINER: Optional[List[_OSM_R26_CONTAINER]] = Field(
        default=None,
        title="CONTAINER",
    )

    SUBJECT_PERSON_OR_ANIMAL_IDENTIFICATION: Optional[_OSM_R26_SUBJECT_PERSON_OR_ANIMAL_IDENTIFICATION] = Field(
        default=None,
        title="SUBJECT_PERSON_OR_ANIMAL_IDENTIFICATION",
    )

    SUBJECT_POPULATION_OR_LOCATION_IDENTIFICATION: Optional[_OSM_R26_SUBJECT_POPULATION_OR_LOCATION_IDENTIFICATION] = Field(
        default=None,
        title="SUBJECT_POPULATION_OR_LOCATION_IDENTIFICATION",
    )

    model_config = ConfigDict(populate_by_name=True)

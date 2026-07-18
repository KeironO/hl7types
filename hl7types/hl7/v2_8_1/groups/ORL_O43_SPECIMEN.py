"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.1
Class: ORL_O43.SPECIMEN
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import ConfigDict, Field
from hl7types.hl7 import HL7Model

from ..segments.NTE import NTE
from ..segments.SPM import SPM

from .ORL_O43_SPECIMEN_CONTAINER import ORL_O43_SPECIMEN_CONTAINER
from .ORL_O43_SPECIMEN_OBSERVATION import ORL_O43_SPECIMEN_OBSERVATION

_NTE = NTE
_ORL_O43_SPECIMEN_CONTAINER = ORL_O43_SPECIMEN_CONTAINER
_ORL_O43_SPECIMEN_OBSERVATION = ORL_O43_SPECIMEN_OBSERVATION
_SPM = SPM


class ORL_O43_SPECIMEN(HL7Model):
    """HL7 v2 ORL_O43.SPECIMEN group.

    Attributes:
        SPM (SPM): Specimen, required
        SPECIMEN_OBSERVATION (Optional[List[ORL_O43_SPECIMEN_OBSERVATION]]): optional
        NTE (Optional[List[NTE]]): Notes and Comments, optional
        SPECIMEN_CONTAINER (List[ORL_O43_SPECIMEN_CONTAINER]): required
    """

    SPM: _SPM = Field(
        title="SPM",
        description="Specimen",
    )

    SPECIMEN_OBSERVATION: Optional[List[_ORL_O43_SPECIMEN_OBSERVATION]] = Field(
        default=None,
        title="SPECIMEN_OBSERVATION",
    )

    NTE: Optional[List[_NTE]] = Field(
        default=None,
        title="NTE",
        description="Notes and Comments",
    )

    SPECIMEN_CONTAINER: List[_ORL_O43_SPECIMEN_CONTAINER] = Field(
        min_length=1,
        title="SPECIMEN_CONTAINER",
    )

    model_config = ConfigDict(populate_by_name=True)

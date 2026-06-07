"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.2
Class: ORL_O36.SPECIMEN
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.NTE import NTE
from ..segments.SPM import SPM

from .ORL_O36_SPECIMEN_CONTAINER import ORL_O36_SPECIMEN_CONTAINER
from .ORL_O36_SPECIMEN_OBSERVATION import ORL_O36_SPECIMEN_OBSERVATION

_NTE = NTE
_ORL_O36_SPECIMEN_CONTAINER = ORL_O36_SPECIMEN_CONTAINER
_ORL_O36_SPECIMEN_OBSERVATION = ORL_O36_SPECIMEN_OBSERVATION
_SPM = SPM


class ORL_O36_SPECIMEN(HL7Model):
    """HL7 v2 ORL_O36.SPECIMEN group.

    Attributes:
        SPM (SPM): required
        SPECIMEN_OBSERVATION (Optional[List[ORL_O36_SPECIMEN_OBSERVATION]]): optional
        NTE (Optional[List[NTE]]): optional
        SPECIMEN_CONTAINER (List[ORL_O36_SPECIMEN_CONTAINER]): required
    """

    SPM: _SPM = Field(
        title="SPM",
        description="Required",
    )

    SPECIMEN_OBSERVATION: Optional[List[_ORL_O36_SPECIMEN_OBSERVATION]] = Field(
        default=None,
        title="SPECIMEN_OBSERVATION",
        description="Optional, repeating",
    )

    NTE: Optional[List[_NTE]] = Field(
        default=None,
        title="NTE",
        description="Optional, repeating",
    )

    SPECIMEN_CONTAINER: List[_ORL_O36_SPECIMEN_CONTAINER] = Field(
        min_length=1,
        title="SPECIMEN_CONTAINER",
        description="Required, repeating",
    )

    model_config = {"populate_by_name": True}

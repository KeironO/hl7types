"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5
Class: OMD_O03.DIET
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import ConfigDict, Field
from hl7types.hl7 import HL7Model

from ..segments.NTE import NTE
from ..segments.ODS import ODS

from .OMD_O03_OBSERVATION import OMD_O03_OBSERVATION

_NTE = NTE
_ODS = ODS
_OMD_O03_OBSERVATION = OMD_O03_OBSERVATION


class OMD_O03_DIET(HL7Model):
    """HL7 v2 OMD_O03.DIET group.

    Attributes:
        ODS (List[ODS]): Dietary Orders, Supplements, and Preferences, required
        NTE (Optional[List[NTE]]): Notes and Comments, optional
        OBSERVATION (Optional[List[OMD_O03_OBSERVATION]]): optional
    """

    ODS: List[_ODS] = Field(
        min_length=1,
        title="ODS",
        description="Dietary Orders, Supplements, and Preferences",
    )

    NTE: Optional[List[_NTE]] = Field(
        default=None,
        title="NTE",
        description="Notes and Comments",
    )

    OBSERVATION: Optional[List[_OMD_O03_OBSERVATION]] = Field(
        default=None,
        title="OBSERVATION",
    )

    model_config = ConfigDict(populate_by_name=True)

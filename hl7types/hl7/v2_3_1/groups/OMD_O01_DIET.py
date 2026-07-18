"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3.1
Class: OMD_O01.DIET
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import ConfigDict, Field
from hl7types.hl7 import HL7Model

from ..segments.NTE import NTE
from ..segments.ODS import ODS

from .OMD_O01_OBSERVATION import OMD_O01_OBSERVATION

_NTE = NTE
_ODS = ODS
_OMD_O01_OBSERVATION = OMD_O01_OBSERVATION


class OMD_O01_DIET(HL7Model):
    """HL7 v2 OMD_O01.DIET group.

    Attributes:
        ODS (List[ODS]): ODS - dietary orders, supplements, and preferences segment, required
        NTE (Optional[List[NTE]]): NTE - notes and comments segment, optional
        OBSERVATION (List[OMD_O01_OBSERVATION]): required
    """

    ODS: List[_ODS] = Field(
        min_length=1,
        title="ODS",
        description=(
            "ODS - dietary orders, supplements, and preferences segment"
        ),
    )

    NTE: Optional[List[_NTE]] = Field(
        default=None,
        title="NTE",
        description="NTE - notes and comments segment",
    )

    OBSERVATION: List[_OMD_O01_OBSERVATION] = Field(
        min_length=1,
        title="OBSERVATION",
    )

    model_config = ConfigDict(populate_by_name=True)

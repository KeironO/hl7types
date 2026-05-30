"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3.1
Class: OMD_O01.DIET
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
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
        ODS (List[ODS]): required
        NTE (Optional[List[NTE]]): optional
        OBSERVATION (List[OMD_O01_OBSERVATION]): required
    """

    ODS: List[_ODS] = Field(
        default=...,
        title="ODS",
        description="Required, repeating",
    )

    NTE: Optional[List[_NTE]] = Field(
        default=None,
        title="NTE",
        description="Optional, repeating",
    )

    OBSERVATION: List[_OMD_O01_OBSERVATION] = Field(
        default=...,
        title="OBSERVATION",
        description="Required, repeating",
    )

    model_config = {"populate_by_name": True}

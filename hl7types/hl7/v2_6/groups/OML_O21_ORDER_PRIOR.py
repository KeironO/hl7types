"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.6
Class: OML_O21.ORDER_PRIOR
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.NTE import NTE
from ..segments.OBR import OBR
from ..segments.ORC import ORC
from ..segments.ROL import ROL

from .OML_O21_OBSERVATION_PRIOR import OML_O21_OBSERVATION_PRIOR
from .OML_O21_TIMING_PRIOR import OML_O21_TIMING_PRIOR

_NTE = NTE
_OBR = OBR
_OML_O21_OBSERVATION_PRIOR = OML_O21_OBSERVATION_PRIOR
_OML_O21_TIMING_PRIOR = OML_O21_TIMING_PRIOR
_ORC = ORC
_ROL = ROL


class OML_O21_ORDER_PRIOR(HL7Model):
    """HL7 v2 OML_O21.ORDER_PRIOR group.

    Attributes:
        ORC (Optional[ORC]): optional
        OBR (OBR): required
        NTE (Optional[List[NTE]]): optional
        ROL (Optional[List[ROL]]): optional
        TIMING_PRIOR (Optional[List[OML_O21_TIMING_PRIOR]]): optional
        OBSERVATION_PRIOR (List[OML_O21_OBSERVATION_PRIOR]): required
    """

    ORC: Optional[_ORC] = Field(
        default=None,
        title="ORC",
        description="Optional",
    )

    OBR: _OBR = Field(
        default=...,
        title="OBR",
        description="Required",
    )

    NTE: Optional[List[_NTE]] = Field(
        default=None,
        title="NTE",
        description="Optional, repeating",
    )

    ROL: Optional[List[_ROL]] = Field(
        default=None,
        title="ROL",
        description="Optional, repeating",
    )

    TIMING_PRIOR: Optional[List[_OML_O21_TIMING_PRIOR]] = Field(
        default=None,
        title="TIMING_PRIOR",
        description="Optional, repeating",
    )

    OBSERVATION_PRIOR: List[_OML_O21_OBSERVATION_PRIOR] = Field(
        default=...,
        title="OBSERVATION_PRIOR",
        description="Required, repeating",
    )

    model_config = {"populate_by_name": True}

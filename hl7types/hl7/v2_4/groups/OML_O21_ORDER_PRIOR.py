"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.4
Class: OML_O21.ORDER_PRIOR
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import BaseModel, Field

from ..segments.NTE import NTE
from ..segments.OBR import OBR
from ..segments.ORC import ORC

from .OML_O21_OBSERVATION_PRIOR import OML_O21_OBSERVATION_PRIOR

_NTE = NTE
_OBR = OBR
_OML_O21_OBSERVATION_PRIOR = OML_O21_OBSERVATION_PRIOR
_ORC = ORC


class OML_O21_ORDER_PRIOR(BaseModel):
    """HL7 v2 OML_O21.ORDER_PRIOR group.

    Attributes:
        ORC (Optional[ORC]): optional
        OBR (OBR): required
        NTE (Optional[List[NTE]]): optional
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

    OBSERVATION_PRIOR: List[_OML_O21_OBSERVATION_PRIOR] = Field(
        default=...,
        title="OBSERVATION_PRIOR",
        description="Required, repeating",
    )

    model_config = {"populate_by_name": True}

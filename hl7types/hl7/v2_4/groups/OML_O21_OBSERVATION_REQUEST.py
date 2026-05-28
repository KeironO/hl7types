"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.4
Class: OML_O21.OBSERVATION_REQUEST
Type: Group
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..segments.DG1 import DG1
from ..segments.NTE import NTE
from ..segments.OBR import OBR
from ..segments.TCD import TCD
from .OML_O21_CONTAINER_2 import OML_O21_CONTAINER_2
from .OML_O21_OBSERVATION import OML_O21_OBSERVATION
from .OML_O21_PRIOR_RESULT import OML_O21_PRIOR_RESULT

_DG1 = DG1
_NTE = NTE
_OBR = OBR
_OML_O21_CONTAINER_2 = OML_O21_CONTAINER_2
_OML_O21_OBSERVATION = OML_O21_OBSERVATION
_OML_O21_PRIOR_RESULT = OML_O21_PRIOR_RESULT
_TCD = TCD


class OML_O21_OBSERVATION_REQUEST(BaseModel):
    """HL7 v2 OML_O21.OBSERVATION_REQUEST group.

    Attributes:
        OBR (OBR): required
        CONTAINER_2 (Optional[List[OML_O21_CONTAINER_2]]): optional
        TCD (Optional[TCD]): optional
        NTE (Optional[List[NTE]]): optional
        DG1 (Optional[List[DG1]]): optional
        OBSERVATION (Optional[List[OML_O21_OBSERVATION]]): optional
        PRIOR_RESULT (Optional[List[OML_O21_PRIOR_RESULT]]): optional
    """

    OBR: _OBR = Field(
        default=...,
        title="OBR",
        description="Required",
    )

    CONTAINER_2: list[_OML_O21_CONTAINER_2] | None = Field(
        default=None,
        title="CONTAINER_2",
        description="Optional, repeating",
    )

    TCD: _TCD | None = Field(
        default=None,
        title="TCD",
        description="Optional",
    )

    NTE: list[_NTE] | None = Field(
        default=None,
        title="NTE",
        description="Optional, repeating",
    )

    DG1: list[_DG1] | None = Field(
        default=None,
        title="DG1",
        description="Optional, repeating",
    )

    OBSERVATION: list[_OML_O21_OBSERVATION] | None = Field(
        default=None,
        title="OBSERVATION",
        description="Optional, repeating",
    )

    PRIOR_RESULT: list[_OML_O21_PRIOR_RESULT] | None = Field(
        default=None,
        title="PRIOR_RESULT",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}

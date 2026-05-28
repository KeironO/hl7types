"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.6
Class: OML_O21.OBSERVATION_REQUEST
Type: Group
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..segments.CTD import CTD
from ..segments.DG1 import DG1
from ..segments.NTE import NTE
from ..segments.OBR import OBR
from ..segments.ROL import ROL
from ..segments.TCD import TCD
from .OML_O21_OBSERVATION import OML_O21_OBSERVATION
from .OML_O21_PRIOR_RESULT import OML_O21_PRIOR_RESULT
from .OML_O21_SPECIMEN import OML_O21_SPECIMEN

_CTD = CTD
_DG1 = DG1
_NTE = NTE
_OBR = OBR
_OML_O21_OBSERVATION = OML_O21_OBSERVATION
_OML_O21_PRIOR_RESULT = OML_O21_PRIOR_RESULT
_OML_O21_SPECIMEN = OML_O21_SPECIMEN
_ROL = ROL
_TCD = TCD


class OML_O21_OBSERVATION_REQUEST(BaseModel):
    """HL7 v2 OML_O21.OBSERVATION_REQUEST group.

    Attributes:
        OBR (OBR): required
        TCD (Optional[TCD]): optional
        NTE (Optional[List[NTE]]): optional
        ROL (Optional[List[ROL]]): optional
        CTD (Optional[CTD]): optional
        DG1 (Optional[List[DG1]]): optional
        OBSERVATION (Optional[List[OML_O21_OBSERVATION]]): optional
        SPECIMEN (Optional[List[OML_O21_SPECIMEN]]): optional
        PRIOR_RESULT (Optional[List[OML_O21_PRIOR_RESULT]]): optional
    """

    OBR: _OBR = Field(
        default=...,
        title="OBR",
        description="Required",
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

    ROL: list[_ROL] | None = Field(
        default=None,
        title="ROL",
        description="Optional, repeating",
    )

    CTD: _CTD | None = Field(
        default=None,
        title="CTD",
        description="Optional",
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

    SPECIMEN: list[_OML_O21_SPECIMEN] | None = Field(
        default=None,
        title="SPECIMEN",
        description="Optional, repeating",
    )

    PRIOR_RESULT: list[_OML_O21_PRIOR_RESULT] | None = Field(
        default=None,
        title="PRIOR_RESULT",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}

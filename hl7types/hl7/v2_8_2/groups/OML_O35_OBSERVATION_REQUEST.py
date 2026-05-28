"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.2
Class: OML_O35.OBSERVATION_REQUEST
Type: Group
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..segments.DG1 import DG1
from ..segments.NTE import NTE
from ..segments.OBR import OBR
from ..segments.PRT import PRT
from ..segments.SGH import SGH
from ..segments.SGT import SGT
from ..segments.TCD import TCD
from .OML_O35_OBSERVATION import OML_O35_OBSERVATION
from .OML_O35_PRIOR_RESULT import OML_O35_PRIOR_RESULT

_DG1 = DG1
_NTE = NTE
_OBR = OBR
_OML_O35_OBSERVATION = OML_O35_OBSERVATION
_OML_O35_PRIOR_RESULT = OML_O35_PRIOR_RESULT
_PRT = PRT
_SGH = SGH
_SGT = SGT
_TCD = TCD


class OML_O35_OBSERVATION_REQUEST(BaseModel):
    """HL7 v2 OML_O35.OBSERVATION_REQUEST group.

    Attributes:
        OBR (OBR): required
        TCD (Optional[TCD]): optional
        NTE (Optional[List[NTE]]): optional
        PRT (Optional[List[PRT]]): optional
        DG1 (Optional[List[DG1]]): optional
        OBSERVATION (Optional[List[OML_O35_OBSERVATION]]): optional
        SGH (Optional[SGH]): optional
        PRIOR_RESULT (Optional[List[OML_O35_PRIOR_RESULT]]): optional
        SGT (Optional[SGT]): optional
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

    PRT: list[_PRT] | None = Field(
        default=None,
        title="PRT",
        description="Optional, repeating",
    )

    DG1: list[_DG1] | None = Field(
        default=None,
        title="DG1",
        description="Optional, repeating",
    )

    OBSERVATION: list[_OML_O35_OBSERVATION] | None = Field(
        default=None,
        title="OBSERVATION",
        description="Optional, repeating",
    )

    SGH: _SGH | None = Field(
        default=None,
        title="SGH",
        description="Optional",
    )

    PRIOR_RESULT: list[_OML_O35_PRIOR_RESULT] | None = Field(
        default=None,
        title="PRIOR_RESULT",
        description="Optional, repeating",
    )

    SGT: _SGT | None = Field(
        default=None,
        title="SGT",
        description="Optional",
    )

    model_config = {"populate_by_name": True}

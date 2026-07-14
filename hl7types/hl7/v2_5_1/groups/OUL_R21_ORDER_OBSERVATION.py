"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5.1
Class: OUL_R21.ORDER_OBSERVATION
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.CTI import CTI
from ..segments.NTE import NTE
from ..segments.OBR import OBR
from ..segments.ORC import ORC

from .OUL_R21_CONTAINER import OUL_R21_CONTAINER
from .OUL_R21_OBSERVATION import OUL_R21_OBSERVATION
from .OUL_R21_TIMING_QTY import OUL_R21_TIMING_QTY

_CTI = CTI
_NTE = NTE
_OBR = OBR
_ORC = ORC
_OUL_R21_CONTAINER = OUL_R21_CONTAINER
_OUL_R21_OBSERVATION = OUL_R21_OBSERVATION
_OUL_R21_TIMING_QTY = OUL_R21_TIMING_QTY


class OUL_R21_ORDER_OBSERVATION(HL7Model):
    """HL7 v2 OUL_R21.ORDER_OBSERVATION group.

    Attributes:
        CONTAINER (Optional[OUL_R21_CONTAINER]): optional
        ORC (Optional[ORC]): Common Order, optional
        OBR (OBR): Observation Request, required
        NTE (Optional[List[NTE]]): Notes and Comments, optional
        TIMING_QTY (Optional[List[OUL_R21_TIMING_QTY]]): optional
        OBSERVATION (List[OUL_R21_OBSERVATION]): required
        CTI (Optional[List[CTI]]): Clinical Trial Identification, optional
    """

    CONTAINER: Optional[_OUL_R21_CONTAINER] = Field(
        default=None,
        title="CONTAINER",
    )

    ORC: Optional[_ORC] = Field(
        default=None,
        title="ORC",
        description="Common Order",
    )

    OBR: _OBR = Field(
        title="OBR",
        description="Observation Request",
    )

    NTE: Optional[List[_NTE]] = Field(
        default=None,
        title="NTE",
        description="Notes and Comments",
    )

    TIMING_QTY: Optional[List[_OUL_R21_TIMING_QTY]] = Field(
        default=None,
        title="TIMING_QTY",
    )

    OBSERVATION: List[_OUL_R21_OBSERVATION] = Field(
        min_length=1,
        title="OBSERVATION",
    )

    CTI: Optional[List[_CTI]] = Field(
        default=None,
        title="CTI",
        description="Clinical Trial Identification",
    )

    model_config = {"populate_by_name": True}

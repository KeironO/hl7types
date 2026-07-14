"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.2
Class: OUL_R22.ORDER
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.CTI import CTI
from ..segments.NTE import NTE
from ..segments.OBR import OBR
from ..segments.PRT import PRT

from .OUL_R22_COMMON_ORDER import OUL_R22_COMMON_ORDER
from .OUL_R22_RESULT import OUL_R22_RESULT
from .OUL_R22_TIMING_QTY import OUL_R22_TIMING_QTY

_CTI = CTI
_NTE = NTE
_OBR = OBR
_OUL_R22_COMMON_ORDER = OUL_R22_COMMON_ORDER
_OUL_R22_RESULT = OUL_R22_RESULT
_OUL_R22_TIMING_QTY = OUL_R22_TIMING_QTY
_PRT = PRT


class OUL_R22_ORDER(HL7Model):
    """HL7 v2 OUL_R22.ORDER group.

    Attributes:
        OBR (OBR): Observation Request, required
        PRT (Optional[List[PRT]]): Participation Information, optional
        COMMON_ORDER (Optional[OUL_R22_COMMON_ORDER]): optional
        NTE (Optional[List[NTE]]): Notes and Comments, optional
        TIMING_QTY (Optional[List[OUL_R22_TIMING_QTY]]): optional
        RESULT (Optional[List[OUL_R22_RESULT]]): optional
        CTI (Optional[List[CTI]]): Clinical Trial Identification, optional
    """

    OBR: _OBR = Field(
        title="OBR",
        description="Observation Request",
    )

    PRT: Optional[List[_PRT]] = Field(
        default=None,
        title="PRT",
        description="Participation Information",
    )

    COMMON_ORDER: Optional[_OUL_R22_COMMON_ORDER] = Field(
        default=None,
        title="COMMON_ORDER",
    )

    NTE: Optional[List[_NTE]] = Field(
        default=None,
        title="NTE",
        description="Notes and Comments",
    )

    TIMING_QTY: Optional[List[_OUL_R22_TIMING_QTY]] = Field(
        default=None,
        title="TIMING_QTY",
    )

    RESULT: Optional[List[_OUL_R22_RESULT]] = Field(
        default=None,
        title="RESULT",
    )

    CTI: Optional[List[_CTI]] = Field(
        default=None,
        title="CTI",
        description="Clinical Trial Identification",
    )

    model_config = {"populate_by_name": True}

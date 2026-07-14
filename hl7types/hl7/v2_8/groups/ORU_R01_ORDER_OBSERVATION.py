"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8
Class: ORU_R01.ORDER_OBSERVATION
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.CTD import CTD
from ..segments.CTI import CTI
from ..segments.FT1 import FT1
from ..segments.NTE import NTE
from ..segments.OBR import OBR
from ..segments.PRT import PRT

from .ORU_R01_COMMON_ORDER import ORU_R01_COMMON_ORDER
from .ORU_R01_OBSERVATION import ORU_R01_OBSERVATION
from .ORU_R01_SPECIMEN import ORU_R01_SPECIMEN
from .ORU_R01_TIMING_QTY import ORU_R01_TIMING_QTY

_CTD = CTD
_CTI = CTI
_FT1 = FT1
_NTE = NTE
_OBR = OBR
_ORU_R01_COMMON_ORDER = ORU_R01_COMMON_ORDER
_ORU_R01_OBSERVATION = ORU_R01_OBSERVATION
_ORU_R01_SPECIMEN = ORU_R01_SPECIMEN
_ORU_R01_TIMING_QTY = ORU_R01_TIMING_QTY
_PRT = PRT


class ORU_R01_ORDER_OBSERVATION(HL7Model):
    """HL7 v2 ORU_R01.ORDER_OBSERVATION group.

    Attributes:
        COMMON_ORDER (Optional[ORU_R01_COMMON_ORDER]): optional
        OBR (OBR): Observation Request, required
        NTE (Optional[List[NTE]]): Notes and Comments, optional
        PRT (Optional[List[PRT]]): Participation Information, optional
        TIMING_QTY (Optional[List[ORU_R01_TIMING_QTY]]): optional
        CTD (Optional[CTD]): Contact Data, optional
        OBSERVATION (Optional[List[ORU_R01_OBSERVATION]]): optional
        FT1 (Optional[List[FT1]]): Financial Transaction, optional
        CTI (Optional[List[CTI]]): Clinical Trial Identification, optional
        SPECIMEN (Optional[List[ORU_R01_SPECIMEN]]): optional
    """

    COMMON_ORDER: Optional[_ORU_R01_COMMON_ORDER] = Field(
        default=None,
        title="COMMON_ORDER",
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

    PRT: Optional[List[_PRT]] = Field(
        default=None,
        title="PRT",
        description="Participation Information",
    )

    TIMING_QTY: Optional[List[_ORU_R01_TIMING_QTY]] = Field(
        default=None,
        title="TIMING_QTY",
    )

    CTD: Optional[_CTD] = Field(
        default=None,
        title="CTD",
        description="Contact Data",
    )

    OBSERVATION: Optional[List[_ORU_R01_OBSERVATION]] = Field(
        default=None,
        title="OBSERVATION",
    )

    FT1: Optional[List[_FT1]] = Field(
        default=None,
        title="FT1",
        description="Financial Transaction",
    )

    CTI: Optional[List[_CTI]] = Field(
        default=None,
        title="CTI",
        description="Clinical Trial Identification",
    )

    SPECIMEN: Optional[List[_ORU_R01_SPECIMEN]] = Field(
        default=None,
        title="SPECIMEN",
    )

    model_config = {"populate_by_name": True}

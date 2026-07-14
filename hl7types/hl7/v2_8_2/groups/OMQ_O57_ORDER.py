"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.2
Class: OMQ_O57.ORDER
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.BLG import BLG
from ..segments.CTD import CTD
from ..segments.CTI import CTI
from ..segments.DG1 import DG1
from ..segments.FT1 import FT1
from ..segments.OBX import OBX
from ..segments.ORC import ORC
from ..segments.PRT import PRT
from ..segments.TXA import TXA

from .OMQ_O57_OBSERVATION import OMQ_O57_OBSERVATION
from .OMQ_O57_PRIOR_RESULT import OMQ_O57_PRIOR_RESULT

_BLG = BLG
_CTD = CTD
_CTI = CTI
_DG1 = DG1
_FT1 = FT1
_OBX = OBX
_OMQ_O57_OBSERVATION = OMQ_O57_OBSERVATION
_OMQ_O57_PRIOR_RESULT = OMQ_O57_PRIOR_RESULT
_ORC = ORC
_PRT = PRT
_TXA = TXA


class OMQ_O57_ORDER(HL7Model):
    """HL7 v2 OMQ_O57.ORDER group.

    Attributes:
        ORC (ORC): Common Order, required
        PRT (Optional[List[PRT]]): Participation Information, optional
        OBX (OBX): Observation/Result, required
        TXA (TXA): Transcription Document Header, required
        CTD (Optional[CTD]): Contact Data, optional
        DG1 (Optional[List[DG1]]): Diagnosis, optional
        OBSERVATION (Optional[List[OMQ_O57_OBSERVATION]]): optional
        PRIOR_RESULT (Optional[List[OMQ_O57_PRIOR_RESULT]]): optional
        FT1 (Optional[List[FT1]]): Financial Transaction, optional
        CTI (Optional[List[CTI]]): Clinical Trial Identification, optional
        BLG (Optional[BLG]): Billing, optional
    """

    ORC: _ORC = Field(
        title="ORC",
        description="Common Order",
    )

    PRT: Optional[List[_PRT]] = Field(
        default=None,
        title="PRT",
        description="Participation Information",
    )

    OBX: _OBX = Field(
        title="OBX",
        description="Observation/Result",
    )

    TXA: _TXA = Field(
        title="TXA",
        description="Transcription Document Header",
    )

    CTD: Optional[_CTD] = Field(
        default=None,
        title="CTD",
        description="Contact Data",
    )

    DG1: Optional[List[_DG1]] = Field(
        default=None,
        title="DG1",
        description="Diagnosis",
    )

    OBSERVATION: Optional[List[_OMQ_O57_OBSERVATION]] = Field(
        default=None,
        title="OBSERVATION",
    )

    PRIOR_RESULT: Optional[List[_OMQ_O57_PRIOR_RESULT]] = Field(
        default=None,
        title="PRIOR_RESULT",
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

    BLG: Optional[_BLG] = Field(
        default=None,
        title="BLG",
        description="Billing",
    )

    model_config = {"populate_by_name": True}

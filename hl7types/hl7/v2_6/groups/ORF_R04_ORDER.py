"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.6
Class: ORF_R04.ORDER
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.CTD import CTD
from ..segments.CTI import CTI
from ..segments.NTE import NTE
from ..segments.OBR import OBR
from ..segments.ORC import ORC
from ..segments.ROL import ROL

from .ORF_R04_OBSERVATION import ORF_R04_OBSERVATION
from .ORF_R04_TIMING_QTY import ORF_R04_TIMING_QTY

_CTD = CTD
_CTI = CTI
_NTE = NTE
_OBR = OBR
_ORC = ORC
_ORF_R04_OBSERVATION = ORF_R04_OBSERVATION
_ORF_R04_TIMING_QTY = ORF_R04_TIMING_QTY
_ROL = ROL


class ORF_R04_ORDER(HL7Model):
    """HL7 v2 ORF_R04.ORDER group.

    Attributes:
        ORC (Optional[ORC]): Common Order, optional
        OBR (OBR): Observation Request, required
        NTE (Optional[List[NTE]]): Notes and Comments, optional
        ROL (Optional[List[ROL]]): Role, optional
        TIMING_QTY (Optional[List[ORF_R04_TIMING_QTY]]): optional
        CTD (Optional[CTD]): Contact Data, optional
        OBSERVATION (List[ORF_R04_OBSERVATION]): required
        CTI (Optional[List[CTI]]): Clinical Trial Identification, optional
    """

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

    ROL: Optional[List[_ROL]] = Field(
        default=None,
        title="ROL",
        description="Role",
    )

    TIMING_QTY: Optional[List[_ORF_R04_TIMING_QTY]] = Field(
        default=None,
        title="TIMING_QTY",
    )

    CTD: Optional[_CTD] = Field(
        default=None,
        title="CTD",
        description="Contact Data",
    )

    OBSERVATION: List[_ORF_R04_OBSERVATION] = Field(
        min_length=1,
        title="OBSERVATION",
    )

    CTI: Optional[List[_CTI]] = Field(
        default=None,
        title="CTI",
        description="Clinical Trial Identification",
    )

    model_config = {"populate_by_name": True}

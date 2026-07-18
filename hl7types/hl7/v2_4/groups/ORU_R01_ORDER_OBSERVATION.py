"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.4
Class: ORU_R01.ORDER_OBSERVATION
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import ConfigDict, Field
from hl7types.hl7 import HL7Model

from ..segments.CTD import CTD
from ..segments.CTI import CTI
from ..segments.FT1 import FT1
from ..segments.NTE import NTE
from ..segments.OBR import OBR
from ..segments.ORC import ORC

from .ORU_R01_OBSERVATION import ORU_R01_OBSERVATION

_CTD = CTD
_CTI = CTI
_FT1 = FT1
_NTE = NTE
_OBR = OBR
_ORC = ORC
_ORU_R01_OBSERVATION = ORU_R01_OBSERVATION


class ORU_R01_ORDER_OBSERVATION(HL7Model):
    """HL7 v2 ORU_R01.ORDER_OBSERVATION group.

    Attributes:
        ORC (Optional[ORC]): Common Order, optional
        OBR (OBR): Observation Request, required
        NTE (Optional[List[NTE]]): Notes and Comments, optional
        CTD (Optional[CTD]): Contact Data, optional
        OBSERVATION (List[ORU_R01_OBSERVATION]): required
        FT1 (Optional[List[FT1]]): Financial Transaction, optional
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

    CTD: Optional[_CTD] = Field(
        default=None,
        title="CTD",
        description="Contact Data",
    )

    OBSERVATION: List[_ORU_R01_OBSERVATION] = Field(
        min_length=1,
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

    model_config = ConfigDict(populate_by_name=True)

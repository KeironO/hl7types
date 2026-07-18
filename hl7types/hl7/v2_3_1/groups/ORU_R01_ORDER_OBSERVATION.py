"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3.1
Class: ORU_R01.ORDER_OBSERVATION
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import ConfigDict, Field
from hl7types.hl7 import HL7Model

from ..segments.CTI import CTI
from ..segments.NTE import NTE
from ..segments.OBR import OBR
from ..segments.ORC import ORC

from .ORU_R01_OBSERVATION import ORU_R01_OBSERVATION

_CTI = CTI
_NTE = NTE
_OBR = OBR
_ORC = ORC
_ORU_R01_OBSERVATION = ORU_R01_OBSERVATION


class ORU_R01_ORDER_OBSERVATION(HL7Model):
    """HL7 v2 ORU_R01.ORDER_OBSERVATION group.

    Attributes:
        ORC (Optional[ORC]): ORC - common order segment, optional
        OBR (OBR): OBR - observation request segment, required
        NTE (Optional[List[NTE]]): NTE - notes and comments segment, optional
        OBSERVATION (List[ORU_R01_OBSERVATION]): required
        CTI (Optional[List[CTI]]): CTI - clinical trial identification segment, optional
    """

    ORC: Optional[_ORC] = Field(
        default=None,
        title="ORC",
        description="ORC - common order segment",
    )

    OBR: _OBR = Field(
        title="OBR",
        description="OBR - observation request segment",
    )

    NTE: Optional[List[_NTE]] = Field(
        default=None,
        title="NTE",
        description="NTE - notes and comments segment",
    )

    OBSERVATION: List[_ORU_R01_OBSERVATION] = Field(
        min_length=1,
        title="OBSERVATION",
    )

    CTI: Optional[List[_CTI]] = Field(
        default=None,
        title="CTI",
        description="CTI - clinical trial identification segment",
    )

    model_config = ConfigDict(populate_by_name=True)

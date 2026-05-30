"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.6
Class: OPU_R25
Type: Message
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.MSH import MSH
from ..segments.NTE import NTE
from ..segments.OBX import OBX
from ..segments.PV1 import PV1
from ..segments.PV2 import PV2
from ..segments.ROL import ROL
from ..segments.SFT import SFT
from ..segments.UAC import UAC

from ..groups.OPU_R25_ACCESSION_DETAIL import OPU_R25_ACCESSION_DETAIL

_MSH = MSH
_NTE = NTE
_OBX = OBX
_OPU_R25_ACCESSION_DETAIL = OPU_R25_ACCESSION_DETAIL
_PV1 = PV1
_PV2 = PV2
_ROL = ROL
_SFT = SFT
_UAC = UAC


class OPU_R25(HL7Model):
    """HL7 v2 OPU_R25 message.

    Attributes:
        MSH (MSH): required
        SFT (Optional[List[SFT]]): optional
        UAC (Optional[UAC]): optional
        NTE (Optional[List[NTE]]): optional
        PV1 (PV1): required
        PV2 (Optional[PV2]): optional
        OBX (Optional[List[OBX]]): optional
        ROL (List[ROL]): required
        ACCESSION_DETAIL (List[OPU_R25_ACCESSION_DETAIL]): required
    """

    MSH: _MSH = Field(
        default=...,
        title="MSH",
        description="Required",
    )

    SFT: Optional[List[_SFT]] = Field(
        default=None,
        title="SFT",
        description="Optional, repeating",
    )

    UAC: Optional[_UAC] = Field(
        default=None,
        title="UAC",
        description="Optional",
    )

    NTE: Optional[List[_NTE]] = Field(
        default=None,
        title="NTE",
        description="Optional, repeating",
    )

    PV1: _PV1 = Field(
        default=...,
        title="PV1",
        description="Required",
    )

    PV2: Optional[_PV2] = Field(
        default=None,
        title="PV2",
        description="Optional",
    )

    OBX: Optional[List[_OBX]] = Field(
        default=None,
        title="OBX",
        description="Optional, repeating",
    )

    ROL: List[_ROL] = Field(
        default=...,
        title="ROL",
        description="Required, repeating",
    )

    ACCESSION_DETAIL: List[_OPU_R25_ACCESSION_DETAIL] = Field(
        default=...,
        title="ACCESSION_DETAIL",
        description="Required, repeating",
    )

    model_config = {"populate_by_name": True}

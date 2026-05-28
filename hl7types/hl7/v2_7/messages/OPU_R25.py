"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7
Class: OPU_R25
Type: Message
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..groups.OPU_R25_ACCESSION_DETAIL import OPU_R25_ACCESSION_DETAIL
from ..groups.OPU_R25_PATIENT_VISIT_OBSERVATION import OPU_R25_PATIENT_VISIT_OBSERVATION
from ..segments.MSH import MSH
from ..segments.NTE import NTE
from ..segments.PRT import PRT
from ..segments.PV1 import PV1
from ..segments.PV2 import PV2
from ..segments.SFT import SFT
from ..segments.UAC import UAC

_MSH = MSH
_NTE = NTE
_OPU_R25_ACCESSION_DETAIL = OPU_R25_ACCESSION_DETAIL
_OPU_R25_PATIENT_VISIT_OBSERVATION = OPU_R25_PATIENT_VISIT_OBSERVATION
_PRT = PRT
_PV1 = PV1
_PV2 = PV2
_SFT = SFT
_UAC = UAC


class OPU_R25(BaseModel):
    """HL7 v2 OPU_R25 message.

    Attributes:
        MSH (MSH): required
        SFT (Optional[List[SFT]]): optional
        UAC (Optional[UAC]): optional
        NTE (Optional[NTE]): optional
        PV1 (PV1): required
        PV2 (Optional[PV2]): optional
        PRT (Optional[List[PRT]]): optional
        PATIENT_VISIT_OBSERVATION (Optional[List[OPU_R25_PATIENT_VISIT_OBSERVATION]]): optional
        ACCESSION_DETAIL (List[OPU_R25_ACCESSION_DETAIL]): required
    """

    MSH: _MSH = Field(
        default=...,
        title="MSH",
        description="Required",
    )

    SFT: list[_SFT] | None = Field(
        default=None,
        title="SFT",
        description="Optional, repeating",
    )

    UAC: _UAC | None = Field(
        default=None,
        title="UAC",
        description="Optional",
    )

    NTE: _NTE | None = Field(
        default=None,
        title="NTE",
        description="Optional",
    )

    PV1: _PV1 = Field(
        default=...,
        title="PV1",
        description="Required",
    )

    PV2: _PV2 | None = Field(
        default=None,
        title="PV2",
        description="Optional",
    )

    PRT: list[_PRT] | None = Field(
        default=None,
        title="PRT",
        description="Optional, repeating",
    )

    PATIENT_VISIT_OBSERVATION: list[_OPU_R25_PATIENT_VISIT_OBSERVATION] | None = Field(
        default=None,
        title="PATIENT_VISIT_OBSERVATION",
        description="Optional, repeating",
    )

    ACCESSION_DETAIL: list[_OPU_R25_ACCESSION_DETAIL] = Field(
        default=...,
        title="ACCESSION_DETAIL",
        description="Required, repeating",
    )

    model_config = {"populate_by_name": True}

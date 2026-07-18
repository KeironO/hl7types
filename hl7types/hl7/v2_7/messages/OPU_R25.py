"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7
Class: OPU_R25
Type: Message
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import ConfigDict, Field
from hl7types.hl7 import HL7Model

from ..segments.MSH import MSH
from ..segments.NTE import NTE
from ..segments.PRT import PRT
from ..segments.PV1 import PV1
from ..segments.PV2 import PV2
from ..segments.SFT import SFT
from ..segments.UAC import UAC

from ..groups.OPU_R25_ACCESSION_DETAIL import OPU_R25_ACCESSION_DETAIL
from ..groups.OPU_R25_PATIENT_VISIT_OBSERVATION import OPU_R25_PATIENT_VISIT_OBSERVATION

_MSH = MSH
_NTE = NTE
_OPU_R25_ACCESSION_DETAIL = OPU_R25_ACCESSION_DETAIL
_OPU_R25_PATIENT_VISIT_OBSERVATION = OPU_R25_PATIENT_VISIT_OBSERVATION
_PRT = PRT
_PV1 = PV1
_PV2 = PV2
_SFT = SFT
_UAC = UAC


class OPU_R25(HL7Model):
    """OPU - Unsolicited Population/Location-Based Laboratory Observation Message (S7.3.11).

    Attributes:
        MSH (MSH): Message Header, required
        SFT (Optional[List[SFT]]): Software Segment, optional
        UAC (Optional[UAC]): User Authentication Credential Segment, optional
        NTE (Optional[NTE]): Notes and Comments, optional
        PV1 (PV1): Patient Visit, required
        PV2 (Optional[PV2]): Patient Visit - Additional Information, optional
        PRT (Optional[List[PRT]]): Participation Information, optional
        PATIENT_VISIT_OBSERVATION (Optional[List[OPU_R25_PATIENT_VISIT_OBSERVATION]]): optional
        ACCESSION_DETAIL (List[OPU_R25_ACCESSION_DETAIL]): required
    """

    MSH: _MSH = Field(
        title="MSH",
        description="Message Header",
    )

    SFT: Optional[List[_SFT]] = Field(
        default=None,
        title="SFT",
        description="Software Segment",
    )

    UAC: Optional[_UAC] = Field(
        default=None,
        title="UAC",
        description="User Authentication Credential Segment",
    )

    NTE: Optional[_NTE] = Field(
        default=None,
        title="NTE",
        description="Notes and Comments",
    )

    PV1: _PV1 = Field(
        title="PV1",
        description="Patient Visit",
    )

    PV2: Optional[_PV2] = Field(
        default=None,
        title="PV2",
        description="Patient Visit - Additional Information",
    )

    PRT: Optional[List[_PRT]] = Field(
        default=None,
        title="PRT",
        description="Participation Information",
    )

    PATIENT_VISIT_OBSERVATION: Optional[List[_OPU_R25_PATIENT_VISIT_OBSERVATION]] = Field(
        default=None,
        title="PATIENT_VISIT_OBSERVATION",
    )

    ACCESSION_DETAIL: List[_OPU_R25_ACCESSION_DETAIL] = Field(
        min_length=1,
        title="ACCESSION_DETAIL",
    )

    model_config = ConfigDict(populate_by_name=True)

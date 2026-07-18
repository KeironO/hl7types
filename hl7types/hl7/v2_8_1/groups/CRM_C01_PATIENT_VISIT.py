"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.1
Class: CRM_C01.PATIENT_VISIT
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import ConfigDict, Field
from hl7types.hl7 import HL7Model

from ..segments.PRT import PRT
from ..segments.PV1 import PV1

_PRT = PRT
_PV1 = PV1


class CRM_C01_PATIENT_VISIT(HL7Model):
    """HL7 v2 CRM_C01.PATIENT_VISIT group.

    Attributes:
        PV1 (PV1): Patient Visit, required
        PRT (Optional[List[PRT]]): Participation Information, optional
    """

    PV1: _PV1 = Field(
        title="PV1",
        description="Patient Visit",
    )

    PRT: Optional[List[_PRT]] = Field(
        default=None,
        title="PRT",
        description="Participation Information",
    )

    model_config = ConfigDict(populate_by_name=True)

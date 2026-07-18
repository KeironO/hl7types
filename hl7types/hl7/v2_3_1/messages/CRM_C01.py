"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3.1
Class: CRM_C01
Type: Message
"""
from __future__ import annotations

from typing import List
from pydantic import ConfigDict, Field
from hl7types.hl7 import HL7Model

from ..segments.MSH import MSH

from ..groups.CRM_C01_PATIENT import CRM_C01_PATIENT

_CRM_C01_PATIENT = CRM_C01_PATIENT
_MSH = MSH


class CRM_C01(HL7Model):
    """CRM - Register a patient on a clinical trial.

    Attributes:
        MSH (MSH): MSH - message header segment, required
        PATIENT (List[CRM_C01_PATIENT]): required
    """

    MSH: _MSH = Field(
        title="MSH",
        description="MSH - message header segment",
    )

    PATIENT: List[_CRM_C01_PATIENT] = Field(
        min_length=1,
        title="PATIENT",
    )

    model_config = ConfigDict(populate_by_name=True)

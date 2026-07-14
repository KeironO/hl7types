"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.4
Class: CRM_C01
Type: Message
"""
from __future__ import annotations

from typing import List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.MSH import MSH

from ..groups.CRM_C01_PATIENT import CRM_C01_PATIENT

_CRM_C01_PATIENT = CRM_C01_PATIENT
_MSH = MSH


class CRM_C01(HL7Model):
    """CRM - Register a patient on a clinical trial (S7).

    Attributes:
        MSH (MSH): Message Header, required
        PATIENT (List[CRM_C01_PATIENT]): required
    """

    MSH: _MSH = Field(
        title="MSH",
        description="Message Header",
    )

    PATIENT: List[_CRM_C01_PATIENT] = Field(
        min_length=1,
        title="PATIENT",
    )

    model_config = {"populate_by_name": True}

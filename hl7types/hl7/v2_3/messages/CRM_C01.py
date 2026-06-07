"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3
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
    """HL7 v2 CRM_C01 message.

    Attributes:
        MSH (MSH): required
        PATIENT (List[CRM_C01_PATIENT]): required
    """

    MSH: _MSH = Field(
        title="MSH",
        description="Required",
    )

    PATIENT: List[_CRM_C01_PATIENT] = Field(
        min_length=1,
        title="PATIENT",
        description="Required, repeating",
    )

    model_config = {"populate_by_name": True}

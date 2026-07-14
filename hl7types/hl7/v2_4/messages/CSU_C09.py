"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.4
Class: CSU_C09
Type: Message
"""
from __future__ import annotations

from typing import List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.MSH import MSH

from ..groups.CSU_C09_PATIENT import CSU_C09_PATIENT

_CSU_C09_PATIENT = CSU_C09_PATIENT
_MSH = MSH


class CSU_C09(HL7Model):
    """CSU - Automated time intervals for reporting, like monthly (S7).

    Attributes:
        MSH (MSH): Message Header, required
        PATIENT (List[CSU_C09_PATIENT]): required
    """

    MSH: _MSH = Field(
        title="MSH",
        description="Message Header",
    )

    PATIENT: List[_CSU_C09_PATIENT] = Field(
        min_length=1,
        title="PATIENT",
    )

    model_config = {"populate_by_name": True}

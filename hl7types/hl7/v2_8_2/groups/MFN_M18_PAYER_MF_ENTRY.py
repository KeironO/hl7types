"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.2
Class: MFN_M18.PAYER_MF_ENTRY
Type: Group
"""
from __future__ import annotations

from typing import List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.PM1 import PM1

from .MFN_M18_PAYER_MF_COVERAGE import MFN_M18_PAYER_MF_COVERAGE

_MFN_M18_PAYER_MF_COVERAGE = MFN_M18_PAYER_MF_COVERAGE
_PM1 = PM1


class MFN_M18_PAYER_MF_ENTRY(HL7Model):
    """HL7 v2 MFN_M18.PAYER_MF_ENTRY group.

    Attributes:
        PM1 (PM1): required
        PAYER_MF_COVERAGE (List[MFN_M18_PAYER_MF_COVERAGE]): required
    """

    PM1: _PM1 = Field(
        title="PM1",
        description="Required",
    )

    PAYER_MF_COVERAGE: List[_MFN_M18_PAYER_MF_COVERAGE] = Field(
        min_length=1,
        title="PAYER_MF_COVERAGE",
        description="Required, repeating",
    )

    model_config = {"populate_by_name": True}

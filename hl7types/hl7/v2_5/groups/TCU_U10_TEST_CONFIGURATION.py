"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5
Class: TCU_U10.TEST_CONFIGURATION
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import ConfigDict, Field
from hl7types.hl7 import HL7Model

from ..segments.SPM import SPM
from ..segments.TCC import TCC

_SPM = SPM
_TCC = TCC


class TCU_U10_TEST_CONFIGURATION(HL7Model):
    """HL7 v2 TCU_U10.TEST_CONFIGURATION group.

    Attributes:
        SPM (Optional[SPM]): Specimen, optional
        TCC (List[TCC]): Test Code Configuration, required
    """

    SPM: Optional[_SPM] = Field(
        default=None,
        title="SPM",
        description="Specimen",
    )

    TCC: List[_TCC] = Field(
        min_length=1,
        title="TCC",
        description="Test Code Configuration",
    )

    model_config = ConfigDict(populate_by_name=True)

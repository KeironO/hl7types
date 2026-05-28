"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.6
Class: TCU_U10.TEST_CONFIGURATION
Type: Group
"""
from _future__ import annotations

from typing import Optional, List
from pydantic import BaseModel, Field

from ..segments.SPM import SPM
from ..segments.TCC import TCC

_SPM = SPM
_TCC = TCC


class TCU_U10_TEST_CONFIGURATION(BaseModel):
    """HL7 v2 TCU_U10.TEST_CONFIGURATION group.

    Attributes:
        SPM (Optional[SPM]): optional
        TCC (List[TCC]): required
    """

    SPM: Optional[_SPM] = Field(
        default=None,
        title="SPM",
        description="Optional",
    )

    TCC: List[_TCC] = Field(
        default=...,
        title="TCC",
        description="Required, repeating",
    )

    model_config = {"populate_by_name": True}

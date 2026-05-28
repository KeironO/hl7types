"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7
Class: CSP
Type: Segment
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, BaseModel, Field

from ..datatypes.CWE import CWE


class CSP(BaseModel):
    """HL7 v2 CSP segment."""

    csp_1: CWE = Field(
        default=...,
        validation_alias=AliasChoices(
            "csp_1",
            "study_phase_identifier",
            "CSP.1",
        ),
        serialization_alias="CSP.1",
        title="Study Phase Identifier",
        description="Item #1022",
    )

    csp_2: str = Field(
        default=...,
        validation_alias=AliasChoices(
            "csp_2",
            "date_time_study_phase_began",
            "CSP.2",
        ),
        serialization_alias="CSP.2",
        title="Date/time Study Phase Began",
        description="Item #1052",
    )

    csp_3: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "csp_3",
            "date_time_study_phase_ended",
            "CSP.3",
        ),
        serialization_alias="CSP.3",
        title="Date/time Study Phase Ended",
        description="Item #1053",
    )

    csp_4: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "csp_4",
            "study_phase_evaluability",
            "CSP.4",
        ),
        serialization_alias="CSP.4",
        title="Study Phase Evaluability",
        description="Item #1054 | Table HL79999",
    )

    model_config = {"populate_by_name": True}

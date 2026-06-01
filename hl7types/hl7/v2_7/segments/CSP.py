"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7
Class: CSP
Type: Segment
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, Field
from hl7types.hl7 import HL7Model
from pydantic import field_validator

from ..datatypes.CWE import CWE


class CSP(HL7Model):
    """HL7 v2 CSP segment.

    Attributes
    ----------
    csp_1 : CWE
        CSP.1 (req) - Study Phase Identifier (CWE)

    csp_2 : str
        CSP.2 (req) - Date/time Study Phase Began (DTM)

    csp_3 : str | None
        CSP.3 (opt) - Date/time Study Phase Ended (DTM)

    csp_4 : CWE | None
        CSP.4 (opt) - Study Phase Evaluability (CWE)
    """

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

    @field_validator("csp_2", "csp_3", mode='before')
    @classmethod
    def _validate_dtm(cls, v: str) -> str:
        import re
        if not re.fullmatch(r'(\d{4}([01]\d(\d{2}([012]\d([0-5]\d([0-5]\d(\.\d(\d(\d(\d)?)?)?)?)?)?)?)?)?)?([+\-]\d{4})?', v or ''):
            raise ValueError(f"{v!r} is not empty or a valid HL7 datetime")
        return v

    model_config = {"populate_by_name": True}

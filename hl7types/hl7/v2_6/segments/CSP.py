"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.6
Class: CSP
Type: Segment
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, Field, field_validator
from hl7types.hl7 import HL7Model

from ..datatypes.CWE import CWE


class CSP(HL7Model):
    """Clinical Study Phase (S7.8.2).

    Attributes
    ----------
    csp_1 : CWE
        CSP.1 - Study Phase Identifier (CWE) R S8.11.3.2

    csp_2 : str
        CSP.2 - Date/time Study Phase Began (DTM) R S7.8.2.2

    csp_3 : str | None
        CSP.3 - Date/time Study Phase Ended (DTM) O S7.8.2.3

    csp_4 : CWE | None
        CSP.4 - Study Phase Evaluability (CWE) C S7.8.2.4 | 9999 - no table for CE
    """

    csp_1: CWE = Field(
        validation_alias=AliasChoices(
            "csp_1",
            "study_phase_identifier",
            "CSP.1",
        ),
        serialization_alias="CSP.1",
        title="Study Phase Identifier",
        description="R | Item #01022",
    )

    csp_2: str = Field(
        validation_alias=AliasChoices(
            "csp_2",
            "date_time_study_phase_began",
            "CSP.2",
        ),
        serialization_alias="CSP.2",
        title="Date/time Study Phase Began",
        description="R | Item #01052 | LEN:24",
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
        description="O | Item #01053 | LEN:24",
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
        description="C | Item #01054 | Table 9999 - no table for CE",
    )

    @field_validator("csp_2", "csp_3", mode='before')
    @classmethod
    def _validate_dtm(cls, v: str, info: ValidationInfo) -> str:
        import re
        if re.fullmatch(r'(\d{4}([01]\d(\d{2}([012]\d([0-5]\d([0-5]\d(\.\d(\d(\d(\d)?)?)?)?)?)?)?)?)?)?([+\-]\d{4})?', v or ''):
            return v
        ctx: dict[str, object] = info.context or {}
        from typing import cast, Callable
        return _apply_dt_fallback(v, parser=cast(Callable[[str], str] | None, ctx.get("dtm_parser")), datatype="DTM", field_path="TS.1")

    model_config = {"populate_by_name": True}

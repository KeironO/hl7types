"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3
Class: CSP
Type: Segment
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, ConfigDict, Field
from hl7types.hl7 import HL7Model

from ..datatypes.CE import CE
from ..datatypes.TS import TS


class CSP(HL7Model):
    """Clinical Study Phase (S7.7.2).

    Attributes
    ----------
    csp_1 : CE | None
        CSP.1 - Study Phase Identifier (CE) C S7.7.2

    csp_2 : TS
        CSP.2 - Date/time Study Phase Began (TS) R S7.7.2.2

    csp_3 : TS | None
        CSP.3 - Date/time Study Phase Ended (TS) O S7.7.2.3

    csp_4 : CE | None
        CSP.4 - Study Phase Evaluability (CE) O S7.7.2.4
    """

    csp_1: Optional[CE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "csp_1",
            "study_phase_identifier",
            "CSP.1",
        ),
        serialization_alias="CSP.1",
        title="Study Phase Identifier",
        description="C | Item #01051",
    )

    csp_2: TS = Field(
        validation_alias=AliasChoices(
            "csp_2",
            "date_time_study_phase_began",
            "CSP.2",
        ),
        serialization_alias="CSP.2",
        title="Date/time Study Phase Began",
        description="R | Item #01052",
    )

    csp_3: Optional[TS] = Field(
        default=None,
        validation_alias=AliasChoices(
            "csp_3",
            "date_time_study_phase_ended",
            "CSP.3",
        ),
        serialization_alias="CSP.3",
        title="Date/time Study Phase Ended",
        description="O | Item #01053",
    )

    csp_4: Optional[CE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "csp_4",
            "study_phase_evaluability",
            "CSP.4",
        ),
        serialization_alias="CSP.4",
        title="Study Phase Evaluability",
        description="O | Item #01054",
    )

    model_config = ConfigDict(populate_by_name=True)

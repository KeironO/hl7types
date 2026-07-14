"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.2
Class: MFA
Type: Segment
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import AliasChoices, Field
from hl7types.hl7 import HL7Model

from ..datatypes.CE import CE
from ..datatypes.TS import TS


class MFA(HL7Model):
    """MASTER FILE ACKNOWLEDGEMENT (S8.4.3).

    Attributes
    ----------
    mfa_1 : str
        MFA.1 (req) - Record-level event code (ID) S8.4.3.1 | 0180 - REcord Level Event Code

    mfa_2 : str | None
        MFA.2 (opt) - MFN control ID (ST) S8.4.3.2

    mfa_3 : TS | None
        MFA.3 (opt) - Event completion date / time (TS) S8.4.3.3

    mfa_4 : CE
        MFA.4 (req) - Error return code and/or text (CE) S8.4.3.4 | 0181 - MFN Recode-Level Error Return

    mfa_5 : list[CE]
        MFA.5 (req, rep) - Primary key value (CE) S8.4.2.4
    """

    mfa_1: str = Field(
        validation_alias=AliasChoices(
            "mfa_1",
            "record_level_event_code",
            "MFA.1",
        ),
        serialization_alias="MFA.1",
        title="Record-level event code",
        description="Item #664 | Table HL70180",
    )

    mfa_2: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "mfa_2",
            "mfn_control_id",
            "MFA.2",
        ),
        serialization_alias="MFA.2",
        title="MFN control ID",
        description="Item #665",
    )

    mfa_3: Optional[TS] = Field(
        default=None,
        validation_alias=AliasChoices(
            "mfa_3",
            "event_completion_date_time",
            "MFA.3",
        ),
        serialization_alias="MFA.3",
        title="Event completion date / time",
        description="Item #668",
    )

    mfa_4: CE = Field(
        validation_alias=AliasChoices(
            "mfa_4",
            "error_return_code_and_or_text",
            "MFA.4",
        ),
        serialization_alias="MFA.4",
        title="Error return code and/or text",
        description="Item #669 | Table HL70181",
    )

    mfa_5: List[CE] = Field(
        min_length=1,
        validation_alias=AliasChoices(
            "mfa_5",
            "primary_key_value",
            "MFA.5",
        ),
        serialization_alias="MFA.5",
        title="Primary key value",
        description="Item #667",
    )

    model_config = {"populate_by_name": True}

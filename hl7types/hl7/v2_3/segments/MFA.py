"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3
Class: MFA
Type: Segment
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import AliasChoices, ConfigDict, Field
from hl7types.hl7 import HL7Model

from ..datatypes.CE import CE
from ..datatypes.TS import TS


class MFA(HL7Model):
    """Master file acknowledgement segment (S8.4.3).

    Attributes
    ----------
    mfa_1 : str
        MFA.1 - Record-Level Event Code (ID) R S8.4.2 | 0180 - Record Level Event Code

    mfa_2 : str | None
        MFA.2 - MFN Control ID (ST) C S8.4.2

    mfa_3 : TS | None
        MFA.3 - Event Completion Date/Time (TS) NA S8.4.3.3

    mfa_4 : CE
        MFA.4 - Error Return Code and/or Text (CE) R S8.4.3.4 | 0181 - MFN Record Level Error Return

    mfa_5 : list[CE]
        MFA.5 - Primary Key Value (CE) R rep S8.4.2.4
    """

    mfa_1: str = Field(
        validation_alias=AliasChoices(
            "mfa_1",
            "record_level_event_code",
            "MFA.1",
        ),
        serialization_alias="MFA.1",
        title="Record-Level Event Code",
        description=(
            "R | Item #00664 | Table 0180 - Record Level Event Code | LEN:3"
        ),
    )

    mfa_2: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "mfa_2",
            "mfn_control_id",
            "MFA.2",
        ),
        serialization_alias="MFA.2",
        title="MFN Control ID",
        description="C | Item #00665 | LEN:20",
    )

    mfa_3: Optional[TS] = Field(
        default=None,
        validation_alias=AliasChoices(
            "mfa_3",
            "event_completion_date_time",
            "MFA.3",
        ),
        serialization_alias="MFA.3",
        title="Event Completion Date/Time",
        description="NA | Item #00668",
    )

    mfa_4: CE = Field(
        validation_alias=AliasChoices(
            "mfa_4",
            "error_return_code_and_or_text",
            "MFA.4",
        ),
        serialization_alias="MFA.4",
        title="Error Return Code and/or Text",
        description=(
            "R | Item #00669 | Table 0181 - MFN Record Level Error Return"
        ),
    )

    mfa_5: List[CE] = Field(
        min_length=1,
        validation_alias=AliasChoices(
            "mfa_5",
            "primary_key_value",
            "MFA.5",
        ),
        serialization_alias="MFA.5",
        title="Primary Key Value",
        description="R | Item #00667",
    )

    model_config = ConfigDict(populate_by_name=True)

"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3.1
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
    """MFA - master file acknowledgment segment (S8.4.3).

    Attributes
    ----------
    mfa_1 : str
        MFA.1 - Record-Level Event Code (ID) R S8.4.3.1 | 0180 - Record-level event code

    mfa_2 : str | None
        MFA.2 - MFN Control ID (ST) C S8.4.3.2

    mfa_3 : TS | None
        MFA.3 - Event Completion Date/Time (TS) O S8.4.3.3

    mfa_4 : CE
        MFA.4 - MFN Record Level Error Return (CE) R S8.4.3.4 | 0181 - MFN record-level error return

    mfa_5 : list[CE]
        MFA.5 - Primary Key Value – MFA (CE) R rep S8.4.3.5

    mfa_6 : list[str]
        MFA.6 - Primary Key Value Type - MFA (ID) R rep S8.4.3.6 | 0355 - Primary key value type
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
            "R | Item #00664 | Table 0180 - Record-level event code | LEN:3"
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
        description="O | Item #00668",
    )

    mfa_4: CE = Field(
        validation_alias=AliasChoices(
            "mfa_4",
            "mfn_record_level_error_return",
            "MFA.4",
        ),
        serialization_alias="MFA.4",
        title="MFN Record Level Error Return",
        description=(
            "R | Item #00669 | Table 0181 - MFN record-level error return"
        ),
    )

    mfa_5: List[CE] = Field(
        min_length=1,
        validation_alias=AliasChoices(
            "mfa_5",
            "primary_key_value_mfa",
            "MFA.5",
        ),
        serialization_alias="MFA.5",
        title="Primary Key Value – MFA",
        description="R | Item #01308",
    )

    mfa_6: List[str] = Field(
        min_length=1,
        validation_alias=AliasChoices(
            "mfa_6",
            "primary_key_value_type_mfa",
            "MFA.6",
        ),
        serialization_alias="MFA.6",
        title="Primary Key Value Type - MFA",
        description=(
            "R | Item #01320 | Table 0355 - Primary key value type | LEN:3"
        ),
    )

    model_config = ConfigDict(populate_by_name=True)

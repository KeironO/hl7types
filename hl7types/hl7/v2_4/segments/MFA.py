"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.4
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
    """HL7 v2 MFA segment.

    Attributes
    ----------
    mfa_1 : str
        MFA.1 (req) - Record-Level Event Code (ID)

    mfa_2 : str | None
        MFA.2 (opt) - MFN Control ID (ST)

    mfa_3 : TS | None
        MFA.3 (opt) - Event Completion Date/Time (TS)

    mfa_4 : CE
        MFA.4 (req) - MFN Record Level Error Return (CE)

    mfa_5 : list[CE] | None
        MFA.5 (req, rep) - Primary Key Value - MFA (CE) [optional: CE has no required components]

    mfa_6 : list[str]
        MFA.6 (req, rep) - Primary Key Value Type - MFA (ID)
    """

    mfa_1: str = Field(
        validation_alias=AliasChoices(
            "mfa_1",
            "record_level_event_code",
            "MFA.1",
        ),
        serialization_alias="MFA.1",
        title="Record-Level Event Code",
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
        title="MFN Control ID",
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
        title="Event Completion Date/Time",
        description="Item #668",
    )

    mfa_4: CE = Field(
        validation_alias=AliasChoices(
            "mfa_4",
            "mfn_record_level_error_return",
            "MFA.4",
        ),
        serialization_alias="MFA.4",
        title="MFN Record Level Error Return",
        description="Item #669 | Table HL70181",
    )

    mfa_5: Optional[List[CE]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "mfa_5",
            "primary_key_value_mfa",
            "MFA.5",
        ),
        serialization_alias="MFA.5",
        title="Primary Key Value - MFA",
        description="Item #1308 | Table HL79999",
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
        description="Item #1320 | Table HL70355",
    )

    model_config = {"populate_by_name": True}

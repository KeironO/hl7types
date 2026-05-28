"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.2
Class: MFA
Type: Segment
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import AliasChoices, BaseModel, Field

from ..datatypes.CE import CE
from ..datatypes.TS import TS


class MFA(BaseModel):
    """HL7 v2 MFA segment."""

    mfa_1: str = Field(
        default=...,
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
        default=...,
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
        default=...,
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

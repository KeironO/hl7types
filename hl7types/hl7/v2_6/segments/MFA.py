"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.6
Class: MFA
Type: Segment
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import AliasChoices, Field, field_validator
from hl7types.hl7 import HL7Model

from ..datatypes.CWE import CWE
from ..datatypes.varies import varies


class MFA(HL7Model):
    """Master File Acknowledgment (S8.5.3).

    Attributes
    ----------
    mfa_1 : str
        MFA.1 - Record-Level Event Code (ID) R S8.5.2.1 | 0180 - Record-level event code

    mfa_2 : str | None
        MFA.2 - MFN Control ID (ST) C S8.5.2.2

    mfa_3 : str | None
        MFA.3 - Event Completion Date/Time (DTM) O S8.5.3.3

    mfa_4 : CWE
        MFA.4 - MFN Record Level Error Return (CWE) R S8.5.3.4 | 0181 - MFN record-level error return

    mfa_5 : list[varies]
        MFA.5 - Primary Key Value - MFA (varies) R rep S8.5.3.5 | 9999 - no table for CE

    mfa_6 : list[str]
        MFA.6 - Primary Key Value Type - MFA (ID) R rep S8.5.3.6 | 0355 - Primary key value type
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

    mfa_3: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "mfa_3",
            "event_completion_date_time",
            "MFA.3",
        ),
        serialization_alias="MFA.3",
        title="Event Completion Date/Time",
        description="O | Item #00668 | LEN:24",
    )

    mfa_4: CWE = Field(
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

    mfa_5: List[varies] = Field(
        min_length=1,
        validation_alias=AliasChoices(
            "mfa_5",
            "primary_key_value_mfa",
            "MFA.5",
        ),
        serialization_alias="MFA.5",
        title="Primary Key Value - MFA",
        description="R | Item #01308 | Table 9999 - no table for CE",
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

    @field_validator("mfa_3", mode='before')
    @classmethod
    def _validate_dtm(cls, v: str, info: ValidationInfo) -> str:
        import re
        if re.fullmatch(r'(\d{4}([01]\d(\d{2}([012]\d([0-5]\d([0-5]\d(\.\d(\d(\d(\d)?)?)?)?)?)?)?)?)?)?([+\-]\d{4})?', v or ''):
            return v
        ctx: dict[str, object] = info.context or {}
        from typing import cast, Callable
        return _apply_dt_fallback(v, parser=cast(Callable[[str], str] | None, ctx.get("dtm_parser")), datatype="DTM", field_path="TS.1")

    model_config = {"populate_by_name": True}

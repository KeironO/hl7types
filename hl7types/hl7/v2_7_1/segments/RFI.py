"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7.1
Class: RFI
Type: Segment
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, Field, field_validator
from hl7types.hl7 import HL7Model


class RFI(HL7Model):
    """Request for Information (S16.4.1).

    Attributes
    ----------
    rfi_1 : str
        RFI.1 - Request Date (DTM) R S16.4.1.1

    rfi_2 : str
        RFI.2 - Response Due Date (DTM) R S16.4.1.2

    rfi_3 : str | None
        RFI.3 - Patient Consent (ID) O S16.4.1.3 | 0136 - Yes/no Indicator

    rfi_4 : str | None
        RFI.4 - Date Additional Information Was Submitted (DTM) O S16.4.1.4
    """

    rfi_1: str = Field(
        validation_alias=AliasChoices(
            "rfi_1",
            "request_date",
            "RFI.1",
        ),
        serialization_alias="RFI.1",
        title="Request Date",
        description="R | Item #01910",
    )

    rfi_2: str = Field(
        validation_alias=AliasChoices(
            "rfi_2",
            "response_due_date",
            "RFI.2",
        ),
        serialization_alias="RFI.2",
        title="Response Due Date",
        description="R | Item #01911",
    )

    rfi_3: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rfi_3",
            "patient_consent",
            "RFI.3",
        ),
        serialization_alias="RFI.3",
        title="Patient Consent",
        description="O | Item #01912 | Table 0136 - Yes/no Indicator | LEN:1",
    )

    rfi_4: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rfi_4",
            "date_additional_information_was_submitted",
            "RFI.4",
        ),
        serialization_alias="RFI.4",
        title="Date Additional Information Was Submitted",
        description="O | Item #01913",
    )

    @field_validator("rfi_1", "rfi_2", "rfi_4", mode='before')
    @classmethod
    def _validate_dtm(cls, v: str, info: ValidationInfo) -> str:
        import re
        if re.fullmatch(r'(\d{4}([01]\d(\d{2}([012]\d([0-5]\d([0-5]\d(\.\d(\d(\d(\d)?)?)?)?)?)?)?)?)?)?([+\-]\d{4})?', v or ''):
            return v
        ctx: dict[str, object] = info.context or {}
        from typing import cast, Callable
        return _apply_dt_fallback(v, parser=cast(Callable[[str], str] | None, ctx.get("dtm_parser")), datatype="DTM", field_path="TS.1")

    model_config = {"populate_by_name": True}

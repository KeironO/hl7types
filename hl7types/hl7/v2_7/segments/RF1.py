"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7
Class: RF1
Type: Segment
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import AliasChoices, Field, field_validator
from hl7types.hl7 import HL7Model

from ..datatypes.CWE import CWE
from ..datatypes.EI import EI


class RF1(HL7Model):
    """Referral Information (S11.8.1).

    Attributes
    ----------
    rf1_1 : CWE | None
        RF1.1 - Referral Status (CWE) O S11.8.1.1 | 0283 - Referral Status

    rf1_2 : CWE | None
        RF1.2 - Referral Priority (CWE) O S11.8.1.2 | 0280 - Referral Priority

    rf1_3 : CWE | None
        RF1.3 - Referral Type (CWE) O S11.8.1.3 | 0281 - Referral Type

    rf1_4 : list[CWE] | None
        RF1.4 - Referral Disposition (CWE) O rep S11.8.1.4 | 0282 - Referral Disposition

    rf1_5 : CWE | None
        RF1.5 - Referral Category (CWE) O S11.8.1.5 | 0284 - Referral Category

    rf1_6 : EI
        RF1.6 - Originating Referral Identifier (EI) R S11.8.1.6

    rf1_7 : str | None
        RF1.7 - Effective Date (DTM) O S11.8.1.7

    rf1_8 : str | None
        RF1.8 - Expiration Date (DTM) O S11.8.1.8

    rf1_9 : str | None
        RF1.9 - Process Date (DTM) O S11.8.1.9

    rf1_10 : list[CWE] | None
        RF1.10 - Referral Reason (CWE) O rep S11.8.1.10 | 0336 - Referral Reason

    rf1_11 : list[EI] | None
        RF1.11 - External Referral Identifier (EI) O rep S11.8.1.11

    rf1_12 : CWE | None
        RF1.12 - Referral Documentation Completion Status (CWE) O S11.8.1.12 | 0865 - Referral Documentation Completion Status
    """

    rf1_1: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rf1_1",
            "referral_status",
            "RF1.1",
        ),
        serialization_alias="RF1.1",
        title="Referral Status",
        description="O | Item #01137 | Table 0283 - Referral Status",
    )

    rf1_2: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rf1_2",
            "referral_priority",
            "RF1.2",
        ),
        serialization_alias="RF1.2",
        title="Referral Priority",
        description="O | Item #01138 | Table 0280 - Referral Priority",
    )

    rf1_3: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rf1_3",
            "referral_type",
            "RF1.3",
        ),
        serialization_alias="RF1.3",
        title="Referral Type",
        description="O | Item #01139 | Table 0281 - Referral Type",
    )

    rf1_4: Optional[List[CWE]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rf1_4",
            "referral_disposition",
            "RF1.4",
        ),
        serialization_alias="RF1.4",
        title="Referral Disposition",
        description="O | Item #01140 | Table 0282 - Referral Disposition",
    )

    rf1_5: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rf1_5",
            "referral_category",
            "RF1.5",
        ),
        serialization_alias="RF1.5",
        title="Referral Category",
        description="O | Item #01141 | Table 0284 - Referral Category",
    )

    rf1_6: EI = Field(
        validation_alias=AliasChoices(
            "rf1_6",
            "originating_referral_identifier",
            "RF1.6",
        ),
        serialization_alias="RF1.6",
        title="Originating Referral Identifier",
        description="R | Item #01142",
    )

    rf1_7: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rf1_7",
            "effective_date",
            "RF1.7",
        ),
        serialization_alias="RF1.7",
        title="Effective Date",
        description="O | Item #01143",
    )

    rf1_8: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rf1_8",
            "expiration_date",
            "RF1.8",
        ),
        serialization_alias="RF1.8",
        title="Expiration Date",
        description="O | Item #01144",
    )

    rf1_9: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rf1_9",
            "process_date",
            "RF1.9",
        ),
        serialization_alias="RF1.9",
        title="Process Date",
        description="O | Item #01145",
    )

    rf1_10: Optional[List[CWE]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rf1_10",
            "referral_reason",
            "RF1.10",
        ),
        serialization_alias="RF1.10",
        title="Referral Reason",
        description="O | Item #01228 | Table 0336 - Referral Reason",
    )

    rf1_11: Optional[List[EI]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rf1_11",
            "external_referral_identifier",
            "RF1.11",
        ),
        serialization_alias="RF1.11",
        title="External Referral Identifier",
        description="O | Item #01300",
    )

    rf1_12: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rf1_12",
            "referral_documentation_completion_status",
            "RF1.12",
        ),
        serialization_alias="RF1.12",
        title="Referral Documentation Completion Status",
        description=(
            "O | Item #02262 | Table 0865 - Referral Documentation Completion "
            "Status"
        ),
    )

    @field_validator("rf1_7", "rf1_8", "rf1_9", mode='before')
    @classmethod
    def _validate_dtm(cls, v: str, info: ValidationInfo) -> str:
        import re
        if re.fullmatch(r'(\d{4}([01]\d(\d{2}([012]\d([0-5]\d([0-5]\d(\.\d(\d(\d(\d)?)?)?)?)?)?)?)?)?)?([+\-]\d{4})?', v or ''):
            return v
        ctx: dict[str, object] = info.context or {}
        from typing import cast, Callable
        return _apply_dt_fallback(v, parser=cast(Callable[[str], str] | None, ctx.get("dtm_parser")), datatype="DTM", field_path="TS.1")

    model_config = {"populate_by_name": True}

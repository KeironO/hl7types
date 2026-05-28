"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.2
Class: UB2
Type: Segment
"""

from __future__ import annotations

from pydantic import AliasChoices, BaseModel, Field


class UB2(BaseModel):
    """HL7 v2 UB2 segment."""

    ub2_1: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "ub2_1",
            "set_id_ub92",
            "UB2.1",
        ),
        serialization_alias="UB2.1",
        title="Set ID - UB92",
        description="Item #553",
    )

    ub2_2: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "ub2_2",
            "co_insurance_days_9",
            "UB2.2",
        ),
        serialization_alias="UB2.2",
        title="Co-insurance days (9)",
        description="Item #554",
    )

    ub2_3: list[str] | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "ub2_3",
            "condition_code_24_30",
            "UB2.3",
        ),
        serialization_alias="UB2.3",
        title="Condition code (24-30)",
        description="Item #555 | Table HL70043",
    )

    ub2_4: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "ub2_4",
            "covered_days_7",
            "UB2.4",
        ),
        serialization_alias="UB2.4",
        title="Covered days (7)",
        description="Item #556",
    )

    ub2_5: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "ub2_5",
            "non_covered_days_8",
            "UB2.5",
        ),
        serialization_alias="UB2.5",
        title="Non-covered days (8)",
        description="Item #557",
    )

    ub2_6: list[str] | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "ub2_6",
            "value_amount_and_code_39_41",
            "UB2.6",
        ),
        serialization_alias="UB2.6",
        title="Value amount and code (39-41)",
        description="Item #558",
    )

    ub2_7: list[str] | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "ub2_7",
            "occurrence_code_and_date_32_35",
            "UB2.7",
        ),
        serialization_alias="UB2.7",
        title="Occurrence code and date (32-35)",
        description="Item #559",
    )

    ub2_8: list[str] | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "ub2_8",
            "occurrence_span_code_dates_36",
            "UB2.8",
        ),
        serialization_alias="UB2.8",
        title="Occurrence span code / dates (36)",
        description="Item #560",
    )

    ub2_9: list[str] | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "ub2_9",
            "ub92_locator_2_state",
            "UB2.9",
        ),
        serialization_alias="UB2.9",
        title="UB92 locator 2 (state)",
        description="Item #561",
    )

    ub2_10: list[str] | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "ub2_10",
            "ub92_locator_11_state",
            "UB2.10",
        ),
        serialization_alias="UB2.10",
        title="UB92 locator 11 (state)",
        description="Item #562",
    )

    ub2_11: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "ub2_11",
            "ub92_locator_31_national",
            "UB2.11",
        ),
        serialization_alias="UB2.11",
        title="UB92 locator 31 (national)",
        description="Item #563",
    )

    ub2_12: list[str] | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "ub2_12",
            "document_control_number_37",
            "UB2.12",
        ),
        serialization_alias="UB2.12",
        title="Document control number (37)",
        description="Item #564",
    )

    ub2_13: list[str] | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "ub2_13",
            "ub92_locator_49_national",
            "UB2.13",
        ),
        serialization_alias="UB2.13",
        title="UB92 locator 49 (national)",
        description="Item #565",
    )

    ub2_14: list[str] | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "ub2_14",
            "ub92_locator_56_state",
            "UB2.14",
        ),
        serialization_alias="UB2.14",
        title="UB92 locator 56 (state)",
        description="Item #566",
    )

    ub2_15: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "ub2_15",
            "ub92_locator_57_national",
            "UB2.15",
        ),
        serialization_alias="UB2.15",
        title="UB92 locator 57 (national)",
        description="Item #567",
    )

    ub2_16: list[str] | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "ub2_16",
            "ub92_locator_78_state",
            "UB2.16",
        ),
        serialization_alias="UB2.16",
        title="UB92 Locator 78 (state)",
        description="Item #568",
    )

    model_config = {"populate_by_name": True}

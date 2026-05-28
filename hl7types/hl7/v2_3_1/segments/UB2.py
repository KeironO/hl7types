"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3.1
Class: UB2
Type: Segment
"""

from __future__ import annotations

from pydantic import AliasChoices, BaseModel, Field

from ..datatypes.OCD import OCD
from ..datatypes.OSP import OSP
from ..datatypes.UVC import UVC


class UB2(BaseModel):
    """HL7 v2 UB2 segment."""

    ub2_1: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "ub2_1",
            "set_id_ub2",
            "UB2.1",
        ),
        serialization_alias="UB2.1",
        title="Set ID - UB2",
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
        title="Co-Insurance Days (9)",
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
        title="Condition Code (24-30)",
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
        title="Covered Days (7)",
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
        title="Non-Covered Days (8)",
        description="Item #557",
    )

    ub2_6: list[UVC] | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "ub2_6",
            "value_amount_code",
            "UB2.6",
        ),
        serialization_alias="UB2.6",
        title="Value Amount & Code",
        description="Item #558 | Table HL70153",
    )

    ub2_7: list[OCD] | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "ub2_7",
            "occurrence_code_date_32_35",
            "UB2.7",
        ),
        serialization_alias="UB2.7",
        title="Occurrence Code & Date (32-35)",
        description="Item #559 | Table HL70350",
    )

    ub2_8: list[OSP] | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "ub2_8",
            "occurrence_span_code_dates_36",
            "UB2.8",
        ),
        serialization_alias="UB2.8",
        title="Occurrence Span Code/Dates (36)",
        description="Item #560 | Table HL70351",
    )

    ub2_9: list[str] | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "ub2_9",
            "ub92_locator_2_state",
            "UB2.9",
        ),
        serialization_alias="UB2.9",
        title="UB92 Locator 2 (State)",
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
        title="UB92 Locator 11 (State)",
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
        title="UB92 Locator 31 (National)",
        description="Item #563",
    )

    ub2_12: list[str] | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "ub2_12",
            "document_control_number",
            "UB2.12",
        ),
        serialization_alias="UB2.12",
        title="Document Control Number",
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
        title="UB92 Locator 49 (National)",
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
        title="UB92 Locator 56 (State)",
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
        title="UB92 Locator 57 (National)",
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
        title="UB92 Locator 78 (State)",
        description="Item #568",
    )

    ub2_17: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "ub2_17",
            "special_visit_count",
            "UB2.17",
        ),
        serialization_alias="UB2.17",
        title="Special Visit Count",
        description="Item #815",
    )

    model_config = {"populate_by_name": True}

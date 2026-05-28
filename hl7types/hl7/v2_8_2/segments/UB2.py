"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.2
Class: UB2
Type: Segment
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import AliasChoices, BaseModel, Field

from ..datatypes.CWE import CWE
from ..datatypes.OCD import OCD
from ..datatypes.OSP import OSP
from ..datatypes.UVC import UVC


class UB2(BaseModel):
    """HL7 v2 UB2 segment."""

    ub2_1: Optional[str] = Field(
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

    ub2_2: Optional[str] = Field(
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

    ub2_3: Optional[List[CWE]] = Field(
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

    ub2_4: Optional[str] = Field(
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

    ub2_5: Optional[str] = Field(
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

    ub2_6: Optional[List[UVC]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ub2_6",
            "value_amount_code_39_41",
            "UB2.6",
        ),
        serialization_alias="UB2.6",
        title="Value Amount & Code (39-41)",
        description="Item #558",
    )

    ub2_7: Optional[List[OCD]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ub2_7",
            "occurrence_code_date_32_35",
            "UB2.7",
        ),
        serialization_alias="UB2.7",
        title="Occurrence Code & Date (32-35)",
        description="Item #559",
    )

    ub2_8: Optional[List[OSP]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ub2_8",
            "occurrence_span_code_dates_36",
            "UB2.8",
        ),
        serialization_alias="UB2.8",
        title="Occurrence Span Code/Dates (36)",
        description="Item #560",
    )

    ub2_9: Optional[List[str]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ub2_9",
            "uniform_billing_locator_2_state",
            "UB2.9",
        ),
        serialization_alias="UB2.9",
        title="Uniform Billing Locator 2 (state)",
        description="Item #561",
    )

    ub2_10: Optional[List[str]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ub2_10",
            "uniform_billing_locator_11_state",
            "UB2.10",
        ),
        serialization_alias="UB2.10",
        title="Uniform Billing Locator 11 (state)",
        description="Item #562",
    )

    ub2_11: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ub2_11",
            "uniform_billing_locator_31_national",
            "UB2.11",
        ),
        serialization_alias="UB2.11",
        title="Uniform Billing Locator 31 (national)",
        description="Item #563",
    )

    ub2_12: Optional[List[str]] = Field(
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

    ub2_13: Optional[List[str]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ub2_13",
            "uniform_billing_locator_49_national",
            "UB2.13",
        ),
        serialization_alias="UB2.13",
        title="Uniform Billing Locator 49 (national)",
        description="Item #565",
    )

    ub2_14: Optional[List[str]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ub2_14",
            "uniform_billing_locator_56_state",
            "UB2.14",
        ),
        serialization_alias="UB2.14",
        title="Uniform Billing Locator 56 (state)",
        description="Item #566",
    )

    ub2_15: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ub2_15",
            "uniform_billing_locator_57_sational",
            "UB2.15",
        ),
        serialization_alias="UB2.15",
        title="Uniform Billing Locator 57 (sational)",
        description="Item #567",
    )

    ub2_16: Optional[List[str]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ub2_16",
            "uniform_billing_locator_78_state",
            "UB2.16",
        ),
        serialization_alias="UB2.16",
        title="Uniform Billing Locator 78 (state)",
        description="Item #568",
    )

    ub2_17: Optional[str] = Field(
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

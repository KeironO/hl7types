"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.2
Class: FT1
Type: Segment
"""

from __future__ import annotations

from pydantic import AliasChoices, BaseModel, Field

from ..datatypes.CE import CE


class FT1(BaseModel):
    """HL7 v2 FT1 segment."""

    ft1_1: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "ft1_1",
            "set_id_financial_transaction",
            "FT1.1",
        ),
        serialization_alias="FT1.1",
        title="Set ID - financial transaction",
        description="Item #355",
    )

    ft1_2: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "ft1_2",
            "transaction_id",
            "FT1.2",
        ),
        serialization_alias="FT1.2",
        title="Transaction ID",
        description="Item #356",
    )

    ft1_3: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "ft1_3",
            "transaction_batch_id",
            "FT1.3",
        ),
        serialization_alias="FT1.3",
        title="Transaction batch ID",
        description="Item #357",
    )

    ft1_4: str = Field(
        default=...,
        validation_alias=AliasChoices(
            "ft1_4",
            "transaction_date",
            "FT1.4",
        ),
        serialization_alias="FT1.4",
        title="Transaction date",
        description="Item #358",
    )

    ft1_5: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "ft1_5",
            "transaction_posting_date",
            "FT1.5",
        ),
        serialization_alias="FT1.5",
        title="Transaction posting date",
        description="Item #359",
    )

    ft1_6: str = Field(
        default=...,
        validation_alias=AliasChoices(
            "ft1_6",
            "transaction_type",
            "FT1.6",
        ),
        serialization_alias="FT1.6",
        title="Transaction type",
        description="Item #360 | Table HL70017",
    )

    ft1_7: CE = Field(
        default=...,
        validation_alias=AliasChoices(
            "ft1_7",
            "transaction_code",
            "FT1.7",
        ),
        serialization_alias="FT1.7",
        title="Transaction code",
        description="Item #361 | Table HL70132",
    )

    ft1_8: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "ft1_8",
            "transaction_description",
            "FT1.8",
        ),
        serialization_alias="FT1.8",
        title="Transaction description",
        description="Item #362",
    )

    ft1_9: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "ft1_9",
            "transaction_description_alternate",
            "FT1.9",
        ),
        serialization_alias="FT1.9",
        title="Transaction description - alternate",
        description="Item #363",
    )

    ft1_10: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "ft1_10",
            "transaction_quantity",
            "FT1.10",
        ),
        serialization_alias="FT1.10",
        title="Transaction quantity",
        description="Item #364",
    )

    ft1_11: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "ft1_11",
            "transaction_amount_extended",
            "FT1.11",
        ),
        serialization_alias="FT1.11",
        title="Transaction amount - extended",
        description="Item #365",
    )

    ft1_12: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "ft1_12",
            "transaction_amount_unit",
            "FT1.12",
        ),
        serialization_alias="FT1.12",
        title="Transaction amount - unit",
        description="Item #366",
    )

    ft1_13: CE | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "ft1_13",
            "department_code",
            "FT1.13",
        ),
        serialization_alias="FT1.13",
        title="Department code",
        description="Item #367 | Table HL70049",
    )

    ft1_14: str = Field(
        default=...,
        validation_alias=AliasChoices(
            "ft1_14",
            "insurance_plan_id",
            "FT1.14",
        ),
        serialization_alias="FT1.14",
        title="Insurance plan ID",
        description="Item #368 | Table HL70072",
    )

    ft1_15: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "ft1_15",
            "insurance_amount",
            "FT1.15",
        ),
        serialization_alias="FT1.15",
        title="Insurance amount",
        description="Item #369",
    )

    ft1_16: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "ft1_16",
            "assigned_patient_location",
            "FT1.16",
        ),
        serialization_alias="FT1.16",
        title="Assigned Patient Location",
        description="Item #133 | Table HL70079",
    )

    ft1_17: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "ft1_17",
            "fee_schedule",
            "FT1.17",
        ),
        serialization_alias="FT1.17",
        title="Fee schedule",
        description="Item #370 | Table HL70024",
    )

    ft1_18: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "ft1_18",
            "patient_type",
            "FT1.18",
        ),
        serialization_alias="FT1.18",
        title="Patient type",
        description="Item #148 | Table HL70018",
    )

    ft1_19: list[CE] | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "ft1_19",
            "diagnosis_code",
            "FT1.19",
        ),
        serialization_alias="FT1.19",
        title="Diagnosis code",
        description="Item #371 | Table HL70051",
    )

    ft1_20: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "ft1_20",
            "performed_by_code",
            "FT1.20",
        ),
        serialization_alias="FT1.20",
        title="Performed by code",
        description="Item #372 | Table HL70084",
    )

    ft1_21: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "ft1_21",
            "ordered_by_code",
            "FT1.21",
        ),
        serialization_alias="FT1.21",
        title="Ordered by code",
        description="Item #373",
    )

    ft1_22: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "ft1_22",
            "unit_cost",
            "FT1.22",
        ),
        serialization_alias="FT1.22",
        title="Unit cost",
        description="Item #374",
    )

    ft1_23: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "ft1_23",
            "filler_order_number",
            "FT1.23",
        ),
        serialization_alias="FT1.23",
        title="Filler Order Number",
        description="Item #217",
    )

    model_config = {"populate_by_name": True}

"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.1
Class: FT1
Type: Segment
"""

from __future__ import annotations

from pydantic import AliasChoices, BaseModel, Field


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
        title="SET ID - FINANCIAL TRANSACTION",
        description="Item #507",
    )

    ft1_2: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "ft1_2",
            "transaction_id",
            "FT1.2",
        ),
        serialization_alias="FT1.2",
        title="TRANSACTION ID",
        description="Item #366",
    )

    ft1_3: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "ft1_3",
            "transaction_batch_id",
            "FT1.3",
        ),
        serialization_alias="FT1.3",
        title="TRANSACTION BATCH ID",
        description="Item #503",
    )

    ft1_4: str = Field(
        default=...,
        validation_alias=AliasChoices(
            "ft1_4",
            "transaction_date",
            "FT1.4",
        ),
        serialization_alias="FT1.4",
        title="TRANSACTION DATE",
        description="Item #351",
    )

    ft1_5: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "ft1_5",
            "transaction_posting_date",
            "FT1.5",
        ),
        serialization_alias="FT1.5",
        title="TRANSACTION POSTING DATE",
        description="Item #352",
    )

    ft1_6: str = Field(
        default=...,
        validation_alias=AliasChoices(
            "ft1_6",
            "transaction_type",
            "FT1.6",
        ),
        serialization_alias="FT1.6",
        title="TRANSACTION TYPE",
        description="Item #353 | Table HL70017",
    )

    ft1_7: str = Field(
        default=...,
        validation_alias=AliasChoices(
            "ft1_7",
            "transaction_code",
            "FT1.7",
        ),
        serialization_alias="FT1.7",
        title="TRANSACTION CODE",
        description="Item #354 | Table HL70096",
    )

    ft1_8: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "ft1_8",
            "transaction_description",
            "FT1.8",
        ),
        serialization_alias="FT1.8",
        title="TRANSACTION DESCRIPTION",
        description="Item #356",
    )

    ft1_9: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "ft1_9",
            "transaction_description_alt",
            "FT1.9",
        ),
        serialization_alias="FT1.9",
        title="TRANSACTION DESCRIPTION - ALT",
        description="Item #706",
    )

    ft1_10: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "ft1_10",
            "transaction_amount_extended",
            "FT1.10",
        ),
        serialization_alias="FT1.10",
        title="TRANSACTION AMOUNT - EXTENDED",
        description="Item #358",
    )

    ft1_11: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "ft1_11",
            "transaction_quantity",
            "FT1.11",
        ),
        serialization_alias="FT1.11",
        title="TRANSACTION QUANTITY",
        description="Item #357",
    )

    ft1_12: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "ft1_12",
            "transaction_amount_unit",
            "FT1.12",
        ),
        serialization_alias="FT1.12",
        title="TRANSACTION AMOUNT - UNIT",
        description="Item #782",
    )

    ft1_13: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "ft1_13",
            "department_code",
            "FT1.13",
        ),
        serialization_alias="FT1.13",
        title="DEPARTMENT CODE",
        description="Item #355 | Table HL70049",
    )

    ft1_14: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "ft1_14",
            "insurance_plan_id",
            "FT1.14",
        ),
        serialization_alias="FT1.14",
        title="INSURANCE PLAN ID",
        description="Item #359 | Table HL70072",
    )

    ft1_15: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "ft1_15",
            "insurance_amount",
            "FT1.15",
        ),
        serialization_alias="FT1.15",
        title="INSURANCE AMOUNT",
        description="Item #360",
    )

    ft1_16: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "ft1_16",
            "patient_location",
            "FT1.16",
        ),
        serialization_alias="FT1.16",
        title="PATIENT LOCATION",
        description="Item #361 | Table HL70079",
    )

    ft1_17: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "ft1_17",
            "fee_schedule",
            "FT1.17",
        ),
        serialization_alias="FT1.17",
        title="FEE SCHEDULE",
        description="Item #362 | Table HL70024",
    )

    ft1_18: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "ft1_18",
            "patient_type",
            "FT1.18",
        ),
        serialization_alias="FT1.18",
        title="PATIENT TYPE",
        description="Item #363 | Table HL70018",
    )

    ft1_19: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "ft1_19",
            "diagnosis_code",
            "FT1.19",
        ),
        serialization_alias="FT1.19",
        title="DIAGNOSIS CODE",
        description="Item #364 | Table HL70051",
    )

    ft1_20: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "ft1_20",
            "performed_by_code",
            "FT1.20",
        ),
        serialization_alias="FT1.20",
        title="PERFORMED BY CODE",
        description="Item #377 | Table HL70084",
    )

    ft1_21: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "ft1_21",
            "ordered_by_code",
            "FT1.21",
        ),
        serialization_alias="FT1.21",
        title="ORDERED BY CODE",
        description="Item #783",
    )

    ft1_22: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "ft1_22",
            "unit_cost",
            "FT1.22",
        ),
        serialization_alias="FT1.22",
        title="UNIT COST",
        description="Item #784",
    )

    model_config = {"populate_by_name": True}

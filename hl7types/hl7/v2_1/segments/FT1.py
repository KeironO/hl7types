"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.1
Class: FT1
Type: Segment
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, Field, field_validator
from hl7types.hl7 import HL7Model


class FT1(HL7Model):
    """HL7 v2 FT1 segment.

    Attributes
    ----------
    ft1_1 : str | None
        FT1.1 (opt) - SET ID - FINANCIAL TRANSACTION (SI)

    ft1_2 : str | None
        FT1.2 (opt) - TRANSACTION ID (ST)

    ft1_3 : str | None
        FT1.3 (opt) - TRANSACTION BATCH ID (ST)

    ft1_4 : str
        FT1.4 (req) - TRANSACTION DATE (DT)

    ft1_5 : str | None
        FT1.5 (opt) - TRANSACTION POSTING DATE (DT)

    ft1_6 : str
        FT1.6 (req) - TRANSACTION TYPE (ID)

    ft1_7 : str
        FT1.7 (req) - TRANSACTION CODE (ID)

    ft1_8 : str | None
        FT1.8 (opt) - TRANSACTION DESCRIPTION (ST)

    ft1_9 : str | None
        FT1.9 (opt) - TRANSACTION DESCRIPTION - ALT (ST)

    ft1_10 : str | None
        FT1.10 (opt) - TRANSACTION AMOUNT - EXTENDED (NM)

    ft1_11 : str | None
        FT1.11 (opt) - TRANSACTION QUANTITY (NM)

    ft1_12 : str | None
        FT1.12 (opt) - TRANSACTION AMOUNT - UNIT (NM)

    ft1_13 : str | None
        FT1.13 (opt) - DEPARTMENT CODE (ST)

    ft1_14 : str | None
        FT1.14 (opt) - INSURANCE PLAN ID (ID)

    ft1_15 : str | None
        FT1.15 (opt) - INSURANCE AMOUNT (NM)

    ft1_16 : str | None
        FT1.16 (opt) - PATIENT LOCATION (ST)

    ft1_17 : str | None
        FT1.17 (opt) - FEE SCHEDULE (ID)

    ft1_18 : str | None
        FT1.18 (opt) - PATIENT TYPE (ID)

    ft1_19 : str | None
        FT1.19 (opt) - DIAGNOSIS CODE (ID)

    ft1_20 : str | None
        FT1.20 (opt) - PERFORMED BY CODE (CN)

    ft1_21 : str | None
        FT1.21 (opt) - ORDERED BY CODE (CN)

    ft1_22 : str | None
        FT1.22 (opt) - UNIT COST (NM)
    """

    ft1_1: Optional[str] = Field(
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

    ft1_2: Optional[str] = Field(
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

    ft1_3: Optional[str] = Field(
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
        validation_alias=AliasChoices(
            "ft1_4",
            "transaction_date",
            "FT1.4",
        ),
        serialization_alias="FT1.4",
        title="TRANSACTION DATE",
        description="Item #351",
    )

    ft1_5: Optional[str] = Field(
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
        validation_alias=AliasChoices(
            "ft1_7",
            "transaction_code",
            "FT1.7",
        ),
        serialization_alias="FT1.7",
        title="TRANSACTION CODE",
        description="Item #354 | Table HL70096",
    )

    ft1_8: Optional[str] = Field(
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

    ft1_9: Optional[str] = Field(
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

    ft1_10: Optional[str] = Field(
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

    ft1_11: Optional[str] = Field(
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

    ft1_12: Optional[str] = Field(
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

    ft1_13: Optional[str] = Field(
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

    ft1_14: Optional[str] = Field(
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

    ft1_15: Optional[str] = Field(
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

    ft1_16: Optional[str] = Field(
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

    ft1_17: Optional[str] = Field(
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

    ft1_18: Optional[str] = Field(
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

    ft1_19: Optional[str] = Field(
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

    ft1_20: Optional[str] = Field(
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

    ft1_21: Optional[str] = Field(
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

    ft1_22: Optional[str] = Field(
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

    @field_validator("ft1_1", mode='before')
    @classmethod
    def _validate_si(cls, v: str) -> str:
        import re
        if not re.fullmatch(r'\d*', v or ''):
            raise ValueError(f"{v!r} is not empty or a non-negative integer")
        return v

    @field_validator("ft1_4", "ft1_5", mode='before')
    @classmethod
    def _validate_dt(cls, v: str) -> str:
        import re
        if not re.fullmatch(r'(\d{4}([01]\d(\d{2})?)?)?', v or ''):
            raise ValueError(f"{v!r} is not empty or a valid HL7 date (YYYY[MM[DD]])")
        return v

    @field_validator("ft1_10", "ft1_11", "ft1_12", "ft1_15", "ft1_22", mode='before')
    @classmethod
    def _validate_nm(cls, v: str) -> str:
        import re
        if not re.fullmatch(r'(\+|\-)?\d*\.?\d*', v or ''):
            raise ValueError(f"{v!r} is not empty or numeric")
        return v

    model_config = {"populate_by_name": True}

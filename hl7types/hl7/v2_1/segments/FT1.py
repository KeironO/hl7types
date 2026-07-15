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
    """FINANCIAL TRANSACTION (S6.3.3).

    Attributes
    ----------
    ft1_1 : str | None
        FT1.1 - SET ID - FINANCIAL TRANSACTION (SI) O S6-5

    ft1_2 : str | None
        FT1.2 - TRANSACTION ID (ST) O

    ft1_3 : str | None
        FT1.3 - TRANSACTION BATCH ID (ST) O

    ft1_4 : str
        FT1.4 - TRANSACTION DATE (DT) R

    ft1_5 : str | None
        FT1.5 - TRANSACTION POSTING DATE (DT) O

    ft1_6 : str
        FT1.6 - TRANSACTION TYPE (ID) R | 0017 - TRANSACTION TYPE

    ft1_7 : str
        FT1.7 - TRANSACTION CODE (ID) R | 0096 - FINANCIAL TRANSACTION CODE

    ft1_8 : str | None
        FT1.8 - TRANSACTION DESCRIPTION (ST) O

    ft1_9 : str | None
        FT1.9 - TRANSACTION DESCRIPTION - ALT (ST) O

    ft1_10 : str | None
        FT1.10 - TRANSACTION AMOUNT - EXTENDED (NM) O

    ft1_11 : str | None
        FT1.11 - TRANSACTION QUANTITY (NM) O

    ft1_12 : str | None
        FT1.12 - TRANSACTION AMOUNT - UNIT (NM) O

    ft1_13 : str | None
        FT1.13 - DEPARTMENT CODE (ST) O | 0049 - DEPARTMENT CODE

    ft1_14 : str | None
        FT1.14 - INSURANCE PLAN ID (ID) O | 0072 - INS. PLAN ID

    ft1_15 : str | None
        FT1.15 - INSURANCE AMOUNT (NM) O

    ft1_16 : str | None
        FT1.16 - PATIENT LOCATION (ST) O | 0079 - LOCATION

    ft1_17 : str | None
        FT1.17 - FEE SCHEDULE (ID) O | 0024 - FEE SCHEDULE

    ft1_18 : str | None
        FT1.18 - PATIENT TYPE (ID) O | 0018 - PATIENT TYPE

    ft1_19 : str | None
        FT1.19 - DIAGNOSIS CODE (ID) O | 0051 - DIAGNOSIS CODE

    ft1_20 : str | None
        FT1.20 - PERFORMED BY CODE (CN) O | 0084 - PERFORMED BY

    ft1_21 : str | None
        FT1.21 - ORDERED BY CODE (CN) O

    ft1_22 : str | None
        FT1.22 - UNIT COST (NM) O
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
        description="O | Item #00507 | LEN:4",
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
        description="O | Item #00366 | LEN:12",
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
        description="O | Item #00503 | LEN:5",
    )

    ft1_4: str = Field(
        validation_alias=AliasChoices(
            "ft1_4",
            "transaction_date",
            "FT1.4",
        ),
        serialization_alias="FT1.4",
        title="TRANSACTION DATE",
        description="R | Item #00351 | LEN:8",
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
        description="O | Item #00352 | LEN:8",
    )

    ft1_6: str = Field(
        validation_alias=AliasChoices(
            "ft1_6",
            "transaction_type",
            "FT1.6",
        ),
        serialization_alias="FT1.6",
        title="TRANSACTION TYPE",
        description="R | Item #00353 | Table 0017 - TRANSACTION TYPE | LEN:8",
    )

    ft1_7: str = Field(
        validation_alias=AliasChoices(
            "ft1_7",
            "transaction_code",
            "FT1.7",
        ),
        serialization_alias="FT1.7",
        title="TRANSACTION CODE",
        description=(
            "R | Item #00354 | Table 0096 - FINANCIAL TRANSACTION CODE | LEN:20"
        ),
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
        description="O | Item #00356 | LEN:40",
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
        description="O | Item #00706 | LEN:40",
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
        description="O | Item #00358 | LEN:12",
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
        description="O | Item #00357 | LEN:4",
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
        description="O | Item #00782 | LEN:12",
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
        description="O | Item #00355 | Table 0049 - DEPARTMENT CODE | LEN:16",
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
        description="O | Item #00359 | Table 0072 - INS. PLAN ID | LEN:8",
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
        description="O | Item #00360 | LEN:12",
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
        description="O | Item #00361 | Table 0079 - LOCATION | LEN:12",
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
        description="O | Item #00362 | Table 0024 - FEE SCHEDULE | LEN:1",
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
        description="O | Item #00363 | Table 0018 - PATIENT TYPE | LEN:2",
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
        description="O | Item #00364 | Table 0051 - DIAGNOSIS CODE | LEN:8",
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
        description="O | Item #00377 | Table 0084 - PERFORMED BY | LEN:60",
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
        description="O | Item #00783 | LEN:60",
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
        description="O | Item #00784 | LEN:12",
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

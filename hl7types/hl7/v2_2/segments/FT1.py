"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.2
Class: FT1
Type: Segment
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import AliasChoices, Field, field_validator
from hl7types.hl7 import HL7Model

from ..datatypes.CE import CE


class FT1(HL7Model):
    """FINANCIAL TRANSACTION (S6.4.1).

    Attributes
    ----------
    ft1_1 : str | None
        FT1.1 (opt) - Set ID - financial transaction (SI) S6.4.1.1

    ft1_2 : str | None
        FT1.2 (opt) - Transaction ID (ST) S6.4.1.2

    ft1_3 : str | None
        FT1.3 (opt) - Transaction batch ID (ST) S6.4.1.3

    ft1_4 : str
        FT1.4 (req) - Transaction date (DT) S6.4.1.4

    ft1_5 : str | None
        FT1.5 (opt) - Transaction posting date (DT) S6.4.1.5

    ft1_6 : str
        FT1.6 (req) - Transaction type (ID) S6.4.1.6 | 0017 - TRANSACTION TYPE

    ft1_7 : CE
        FT1.7 (req) - Transaction code (CE) S6.4.1.7 | 0132 - TRANSACTION CODE

    ft1_8 : str | None
        FT1.8 (opt) - Transaction description (ST) S6.4.1.8

    ft1_9 : str | None
        FT1.9 (opt) - Transaction description - alternate (ST) S6.4.1.9

    ft1_10 : str | None
        FT1.10 (opt) - Transaction quantity (NM) S6.4.1.10

    ft1_11 : str | None
        FT1.11 (opt) - Transaction amount - extended (NM) S6.4.1.11

    ft1_12 : str | None
        FT1.12 (opt) - Transaction amount - unit (NM) S6.4.1.12

    ft1_13 : CE | None
        FT1.13 (opt) - Department code (CE) S6.4.1.13 | 0049 - DEPARTMENT CODE

    ft1_14 : str
        FT1.14 (req) - Insurance plan ID (ID) S6.4.1.14 | 0072 - INS. PLAN ID

    ft1_15 : str | None
        FT1.15 (opt) - Insurance amount (NM) S6.4.1.15

    ft1_16 : str | None
        FT1.16 (opt) - Assigned Patient Location (CM) S3.3.3.3 | 0079 - LOCATION

    ft1_17 : str | None
        FT1.17 (opt) - Fee schedule (ID) S6.4.1.17 | 0024 - FEE SCHEDULE

    ft1_18 : str | None
        FT1.18 (opt) - Patient type (ID) S3.3.3.18 | 0018 - PATIENT TYPE

    ft1_19 : list[CE] | None
        FT1.19 (opt, rep) - Diagnosis code (CE) S6.4.1.19 | 0051 - DIAGNOSIS CODE

    ft1_20 : str | None
        FT1.20 (opt) - Performed by code (CN) S6.4.1.20 | 0084 - PERFORMED BY

    ft1_21 : str | None
        FT1.21 (opt) - Ordered by code (CN) S6.4.1.21

    ft1_22 : str | None
        FT1.22 (opt) - Unit cost (NM) S6.4.1.22

    ft1_23 : str | None
        FT1.23 (opt) - Filler Order Number (CM) S6.4.1.23
    """

    ft1_1: Optional[str] = Field(
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

    ft1_2: Optional[str] = Field(
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

    ft1_3: Optional[str] = Field(
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
        validation_alias=AliasChoices(
            "ft1_4",
            "transaction_date",
            "FT1.4",
        ),
        serialization_alias="FT1.4",
        title="Transaction date",
        description="Item #358",
    )

    ft1_5: Optional[str] = Field(
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
        validation_alias=AliasChoices(
            "ft1_7",
            "transaction_code",
            "FT1.7",
        ),
        serialization_alias="FT1.7",
        title="Transaction code",
        description="Item #361 | Table HL70132",
    )

    ft1_8: Optional[str] = Field(
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

    ft1_9: Optional[str] = Field(
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

    ft1_10: Optional[str] = Field(
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

    ft1_11: Optional[str] = Field(
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

    ft1_12: Optional[str] = Field(
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

    ft1_13: Optional[CE] = Field(
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
        validation_alias=AliasChoices(
            "ft1_14",
            "insurance_plan_id",
            "FT1.14",
        ),
        serialization_alias="FT1.14",
        title="Insurance plan ID",
        description="Item #368 | Table HL70072",
    )

    ft1_15: Optional[str] = Field(
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

    ft1_16: Optional[str] = Field(
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

    ft1_17: Optional[str] = Field(
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

    ft1_18: Optional[str] = Field(
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

    ft1_19: Optional[List[CE]] = Field(
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

    ft1_20: Optional[str] = Field(
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

    ft1_21: Optional[str] = Field(
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

    ft1_22: Optional[str] = Field(
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

    ft1_23: Optional[str] = Field(
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

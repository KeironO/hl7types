"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.4
Class: FT1
Type: Segment
"""
from __future__ import annotations

import re

from typing import Optional, List
from pydantic import AliasChoices, ConfigDict, Field, field_validator
from hl7types.hl7 import HL7Model

from ..datatypes.CE import CE
from ..datatypes.CP import CP
from ..datatypes.EI import EI
from ..datatypes.PL import PL
from ..datatypes.TS import TS
from ..datatypes.XCN import XCN

_RE_SI = re.compile(r'\d*')
_RE_NM = re.compile(r'(\+|\-)?\d*\.?\d*')


class FT1(HL7Model):
    """Financial Transaction (S6.5.1).

    Attributes
    ----------
    ft1_1 : str | None
        FT1.1 - Set ID - FT1 (SI) O S6.5.1.1

    ft1_2 : str | None
        FT1.2 - Transaction ID (ST) O S6.5.1.2

    ft1_3 : str | None
        FT1.3 - Transaction Batch ID (ST) O S6.5.1.3

    ft1_4 : TS
        FT1.4 - Transaction Date (TS) R S6.5.1.4

    ft1_5 : TS | None
        FT1.5 - Transaction Posting Date (TS) O S6.5.1.5

    ft1_6 : str
        FT1.6 - Transaction Type (IS) R S6.5.1.6 | 0017 - Transaction type

    ft1_7 : CE
        FT1.7 - Transaction Code (CE) R S6.5.1.7 | 0132 - Transaction code

    ft1_8 : str | None
        FT1.8 - Transaction Description (ST) O S6.5.1.8

    ft1_9 : str | None
        FT1.9 - Transaction Description - Alt (ST) O S6.5.1.9

    ft1_10 : str | None
        FT1.10 - Transaction Quantity (NM) O S6.5.1.10

    ft1_11 : CP | None
        FT1.11 - Transaction Amount - Extended (CP) O S6.5.1.11

    ft1_12 : CP | None
        FT1.12 - Transaction Amount - Unit (CP) O S6.5.1.12

    ft1_13 : CE | None
        FT1.13 - Department Code (CE) O S6.5.1.13 | 0049 - Department code

    ft1_14 : CE | None
        FT1.14 - Insurance Plan ID (CE) O S6.5.6.2 | 0072 - Insurance plan ID

    ft1_15 : CP | None
        FT1.15 - Insurance Amount (CP) O S6.5.1.15

    ft1_16 : PL | None
        FT1.16 - Assigned Patient Location (PL) O S6.5.1.16

    ft1_17 : str | None
        FT1.17 - Fee Schedule (IS) O S6.5.1.17 | 0024 - Fee schedule

    ft1_18 : str | None
        FT1.18 - Patient Type (IS) O S6.5.1.18 | 0018 - Patient type

    ft1_19 : list[CE] | None
        FT1.19 - Diagnosis Code - FT1 (CE) O rep S6.5.1.19 | 0051 - Diagnosis code

    ft1_20 : list[XCN] | None
        FT1.20 - Performed By Code (XCN) O rep S6.5.1.20 | 0084 - Performed by

    ft1_21 : list[XCN] | None
        FT1.21 - Ordered By Code (XCN) O rep S6.5.1.21

    ft1_22 : CP | None
        FT1.22 - Unit Cost (CP) O S6.5.1.22

    ft1_23 : EI | None
        FT1.23 - Filler Order Number (EI) O S10.6.2.27

    ft1_24 : list[XCN] | None
        FT1.24 - Entered By Code (XCN) O rep S6.5.1.24

    ft1_25 : CE | None
        FT1.25 - Procedure Code (CE) O S8.10.2.7 | 0088 - Procedure Code

    ft1_26 : list[CE] | None
        FT1.26 - Procedure Code Modifier (CE) O rep S7.4.1.45 | 0340 - Procedure Code modifier
    """

    ft1_1: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ft1_1",
            "set_id_ft1",
            "FT1.1",
        ),
        serialization_alias="FT1.1",
        title="Set ID - FT1",
        description="O | Item #00355 | LEN:4",
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
        description="O | Item #00356 | LEN:12",
    )

    ft1_3: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ft1_3",
            "transaction_batch_id",
            "FT1.3",
        ),
        serialization_alias="FT1.3",
        title="Transaction Batch ID",
        description="O | Item #00357 | LEN:10",
    )

    ft1_4: TS = Field(
        validation_alias=AliasChoices(
            "ft1_4",
            "transaction_date",
            "FT1.4",
        ),
        serialization_alias="FT1.4",
        title="Transaction Date",
        description="R | Item #00358",
    )

    ft1_5: Optional[TS] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ft1_5",
            "transaction_posting_date",
            "FT1.5",
        ),
        serialization_alias="FT1.5",
        title="Transaction Posting Date",
        description="O | Item #00359",
    )

    ft1_6: str = Field(
        validation_alias=AliasChoices(
            "ft1_6",
            "transaction_type",
            "FT1.6",
        ),
        serialization_alias="FT1.6",
        title="Transaction Type",
        description="R | Item #00360 | Table 0017 - Transaction type | LEN:8",
    )

    ft1_7: CE = Field(
        validation_alias=AliasChoices(
            "ft1_7",
            "transaction_code",
            "FT1.7",
        ),
        serialization_alias="FT1.7",
        title="Transaction Code",
        description="R | Item #00361 | Table 0132 - Transaction code",
    )

    ft1_8: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ft1_8",
            "transaction_description",
            "FT1.8",
        ),
        serialization_alias="FT1.8",
        title="Transaction Description",
        description="O | Item #00362 | LEN:40",
    )

    ft1_9: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ft1_9",
            "transaction_description_alt",
            "FT1.9",
        ),
        serialization_alias="FT1.9",
        title="Transaction Description - Alt",
        description="O | Item #00363 | LEN:40",
    )

    ft1_10: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ft1_10",
            "transaction_quantity",
            "FT1.10",
        ),
        serialization_alias="FT1.10",
        title="Transaction Quantity",
        description="O | Item #00364 | LEN:6",
    )

    ft1_11: Optional[CP] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ft1_11",
            "transaction_amount_extended",
            "FT1.11",
        ),
        serialization_alias="FT1.11",
        title="Transaction Amount - Extended",
        description="O | Item #00365",
    )

    ft1_12: Optional[CP] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ft1_12",
            "transaction_amount_unit",
            "FT1.12",
        ),
        serialization_alias="FT1.12",
        title="Transaction Amount - Unit",
        description="O | Item #00366",
    )

    ft1_13: Optional[CE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ft1_13",
            "department_code",
            "FT1.13",
        ),
        serialization_alias="FT1.13",
        title="Department Code",
        description="O | Item #00367 | Table 0049 - Department code",
    )

    ft1_14: Optional[CE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ft1_14",
            "insurance_plan_id",
            "FT1.14",
        ),
        serialization_alias="FT1.14",
        title="Insurance Plan ID",
        description="O | Item #00368 | Table 0072 - Insurance plan ID",
    )

    ft1_15: Optional[CP] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ft1_15",
            "insurance_amount",
            "FT1.15",
        ),
        serialization_alias="FT1.15",
        title="Insurance Amount",
        description="O | Item #00369",
    )

    ft1_16: Optional[PL] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ft1_16",
            "assigned_patient_location",
            "FT1.16",
        ),
        serialization_alias="FT1.16",
        title="Assigned Patient Location",
        description="O | Item #00133",
    )

    ft1_17: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ft1_17",
            "fee_schedule",
            "FT1.17",
        ),
        serialization_alias="FT1.17",
        title="Fee Schedule",
        description="O | Item #00370 | Table 0024 - Fee schedule | LEN:1",
    )

    ft1_18: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ft1_18",
            "patient_type",
            "FT1.18",
        ),
        serialization_alias="FT1.18",
        title="Patient Type",
        description="O | Item #00148 | Table 0018 - Patient type | LEN:2",
    )

    ft1_19: Optional[List[CE]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ft1_19",
            "diagnosis_code_ft1",
            "FT1.19",
        ),
        serialization_alias="FT1.19",
        title="Diagnosis Code - FT1",
        description="O | Item #00371 | Table 0051 - Diagnosis code",
    )

    ft1_20: Optional[List[XCN]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ft1_20",
            "performed_by_code",
            "FT1.20",
        ),
        serialization_alias="FT1.20",
        title="Performed By Code",
        description="O | Item #00372 | Table 0084 - Performed by",
    )

    ft1_21: Optional[List[XCN]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ft1_21",
            "ordered_by_code",
            "FT1.21",
        ),
        serialization_alias="FT1.21",
        title="Ordered By Code",
        description="O | Item #00373",
    )

    ft1_22: Optional[CP] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ft1_22",
            "unit_cost",
            "FT1.22",
        ),
        serialization_alias="FT1.22",
        title="Unit Cost",
        description="O | Item #00374",
    )

    ft1_23: Optional[EI] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ft1_23",
            "filler_order_number",
            "FT1.23",
        ),
        serialization_alias="FT1.23",
        title="Filler Order Number",
        description="O | Item #00217",
    )

    ft1_24: Optional[List[XCN]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ft1_24",
            "entered_by_code",
            "FT1.24",
        ),
        serialization_alias="FT1.24",
        title="Entered By Code",
        description="O | Item #00765",
    )

    ft1_25: Optional[CE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ft1_25",
            "procedure_code",
            "FT1.25",
        ),
        serialization_alias="FT1.25",
        title="Procedure Code",
        description="O | Item #00393 | Table 0088 - Procedure Code",
    )

    ft1_26: Optional[List[CE]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ft1_26",
            "procedure_code_modifier",
            "FT1.26",
        ),
        serialization_alias="FT1.26",
        title="Procedure Code Modifier",
        description="O | Item #01316 | Table 0340 - Procedure Code modifier",
    )

    @field_validator("ft1_1", mode='before')
    @classmethod
    def _validate_si(cls, v: str) -> str:
        if not _RE_SI.fullmatch(v or ''):
            raise ValueError(f"{v!r} is not empty or a non-negative integer")
        return v

    @field_validator("ft1_10", mode='before')
    @classmethod
    def _validate_nm(cls, v: str) -> str:
        if not _RE_NM.fullmatch(v or ''):
            raise ValueError(f"{v!r} is not empty or numeric")
        return v

    model_config = ConfigDict(populate_by_name=True)

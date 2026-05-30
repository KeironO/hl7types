"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3.1
Class: FT1
Type: Segment
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import AliasChoices, Field
from hl7types.hl7 import HL7Model

from ..datatypes.CE import CE
from ..datatypes.CP import CP
from ..datatypes.EI import EI
from ..datatypes.PL import PL
from ..datatypes.TS import TS
from ..datatypes.XCN import XCN


class FT1(HL7Model):
    """HL7 v2 FT1 segment.

    Attributes
    ----------
    ft1_1 : str | None
        FT1.1 (opt) - Set ID - FT1 (SI)

    ft1_2 : str | None
        FT1.2 (opt) - Transaction ID (ST)

    ft1_3 : str | None
        FT1.3 (opt) - Transaction Batch ID (ST)

    ft1_4 : TS
        FT1.4 (req) - Transaction Date (TS)

    ft1_5 : TS | None
        FT1.5 (opt) - Transaction Posting Date (TS)

    ft1_6 : str
        FT1.6 (req) - Transaction Type (IS)

    ft1_7 : CE
        FT1.7 (req) - Transaction Code (CE)

    ft1_8 : str | None
        FT1.8 (opt) - Transaction Description (ST)

    ft1_9 : str | None
        FT1.9 (opt) - Transaction Description - Alt (ST)

    ft1_10 : str | None
        FT1.10 (opt) - Transaction Quantity (NM)

    ft1_11 : CP | None
        FT1.11 (opt) - Transaction Amount - Extended (CP)

    ft1_12 : CP | None
        FT1.12 (opt) - Transaction Amount - Unit (CP)

    ft1_13 : CE | None
        FT1.13 (opt) - Department Code (CE)

    ft1_14 : CE | None
        FT1.14 (opt) - Insurance Plan ID (CE)

    ft1_15 : CP | None
        FT1.15 (opt) - Insurance Amount (CP)

    ft1_16 : PL | None
        FT1.16 (opt) - Assigned Patient Location (PL)

    ft1_17 : str | None
        FT1.17 (opt) - Fee Schedule (IS)

    ft1_18 : str | None
        FT1.18 (opt) - Patient Type (IS)

    ft1_19 : list[CE] | None
        FT1.19 (opt, rep) - Diagnosis Code - FT1 (CE)

    ft1_20 : list[XCN] | None
        FT1.20 (opt, rep) - Performed By Code (XCN)

    ft1_21 : list[XCN] | None
        FT1.21 (opt, rep) - Ordered By Code (XCN)

    ft1_22 : CP | None
        FT1.22 (opt) - Unit Cost (CP)

    ft1_23 : EI | None
        FT1.23 (opt) - Filler Order Number (EI)

    ft1_24 : list[XCN] | None
        FT1.24 (opt, rep) - Entered By Code (XCN)

    ft1_25 : CE | None
        FT1.25 (opt) - Procedure Code (CE)

    ft1_26 : list[CE] | None
        FT1.26 (opt, rep) - Procedure Code Modifier (CE)
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
        title="Transaction Batch ID",
        description="Item #357",
    )

    ft1_4: TS = Field(
        default=...,
        validation_alias=AliasChoices(
            "ft1_4",
            "transaction_date",
            "FT1.4",
        ),
        serialization_alias="FT1.4",
        title="Transaction Date",
        description="Item #358",
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
        title="Transaction Type",
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
        title="Transaction Code",
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
        title="Transaction Description",
        description="Item #362",
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
        title="Transaction Quantity",
        description="Item #364",
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
        description="Item #365",
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
        title="Department Code",
        description="Item #367 | Table HL70049",
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
        description="Item #368 | Table HL70072",
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
        description="Item #369",
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
        description="Item #133",
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
        title="Patient Type",
        description="Item #148 | Table HL70018",
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
        description="Item #371 | Table HL70051",
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
        description="Item #372 | Table HL70084",
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
        description="Item #373",
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
        description="Item #374",
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
        description="Item #217",
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
        description="Item #765",
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
        description="Item #393 | Table HL70088",
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
        description="Item #1316 | Table HL70340",
    )

    model_config = {"populate_by_name": True}

"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8
Class: FT1
Type: Segment
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import AliasChoices, BaseModel, Field

from ..datatypes.CNE import CNE
from ..datatypes.CP import CP
from ..datatypes.CQ import CQ
from ..datatypes.CWE import CWE
from ..datatypes.CX import CX
from ..datatypes.DR import DR
from ..datatypes.EI import EI
from ..datatypes.PL import PL
from ..datatypes.XCN import XCN
from ..datatypes.XON import XON


class FT1(BaseModel):
    """HL7 v2 FT1 segment."""

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

    ft1_4: DR = Field(
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

    ft1_5: Optional[str] = Field(
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

    ft1_6: CWE = Field(
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

    ft1_7: CWE = Field(
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
        title="Transaction amount - unit",
        description="Item #366",
    )

    ft1_13: Optional[CWE] = Field(
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

    ft1_14: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ft1_14",
            "health_plan_id",
            "FT1.14",
        ),
        serialization_alias="FT1.14",
        title="Health Plan ID",
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

    ft1_17: Optional[CWE] = Field(
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

    ft1_18: Optional[CWE] = Field(
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

    ft1_19: Optional[List[CWE]] = Field(
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

    ft1_25: Optional[CNE] = Field(
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

    ft1_26: Optional[List[CNE]] = Field(
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

    ft1_27: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ft1_27",
            "advanced_beneficiary_notice_code",
            "FT1.27",
        ),
        serialization_alias="FT1.27",
        title="Advanced Beneficiary Notice Code",
        description="Item #1310 | Table HL70339",
    )

    ft1_28: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ft1_28",
            "medically_necessary_duplicate_procedure_reason",
            "FT1.28",
        ),
        serialization_alias="FT1.28",
        title="Medically Necessary Duplicate Procedure Reason",
        description="Item #1646 | Table HL70476",
    )

    ft1_29: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ft1_29",
            "ndc_code",
            "FT1.29",
        ),
        serialization_alias="FT1.29",
        title="NDC Code",
        description="Item #1845 | Table HL70549",
    )

    ft1_30: Optional[CX] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ft1_30",
            "payment_reference_id",
            "FT1.30",
        ),
        serialization_alias="FT1.30",
        title="Payment Reference ID",
        description="Item #1846",
    )

    ft1_31: Optional[List[str]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ft1_31",
            "transaction_reference_key",
            "FT1.31",
        ),
        serialization_alias="FT1.31",
        title="Transaction Reference Key",
        description="Item #1847",
    )

    ft1_32: Optional[List[XON]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ft1_32",
            "performing_facility",
            "FT1.32",
        ),
        serialization_alias="FT1.32",
        title="Performing Facility",
        description="Item #2361",
    )

    ft1_33: Optional[XON] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ft1_33",
            "ordering_facility",
            "FT1.33",
        ),
        serialization_alias="FT1.33",
        title="Ordering Facility",
        description="Item #2362",
    )

    ft1_34: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ft1_34",
            "item_number",
            "FT1.34",
        ),
        serialization_alias="FT1.34",
        title="Item Number",
        description="Item #2363",
    )

    ft1_35: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ft1_35",
            "model_number",
            "FT1.35",
        ),
        serialization_alias="FT1.35",
        title="Model Number",
        description="Item #2364",
    )

    ft1_36: Optional[List[CWE]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ft1_36",
            "special_processing_code",
            "FT1.36",
        ),
        serialization_alias="FT1.36",
        title="Special Processing Code",
        description="Item #2365",
    )

    ft1_37: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ft1_37",
            "clinic_code",
            "FT1.37",
        ),
        serialization_alias="FT1.37",
        title="Clinic Code",
        description="Item #2366",
    )

    ft1_38: Optional[CX] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ft1_38",
            "referral_number",
            "FT1.38",
        ),
        serialization_alias="FT1.38",
        title="Referral Number",
        description="Item #2367",
    )

    ft1_39: Optional[CX] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ft1_39",
            "authorization_number",
            "FT1.39",
        ),
        serialization_alias="FT1.39",
        title="Authorization Number",
        description="Item #2368",
    )

    ft1_40: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ft1_40",
            "service_provider_taxonomy_code",
            "FT1.40",
        ),
        serialization_alias="FT1.40",
        title="Service Provider Taxonomy Code",
        description="Item #2369",
    )

    ft1_41: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ft1_41",
            "revenue_code",
            "FT1.41",
        ),
        serialization_alias="FT1.41",
        title="Revenue Code",
        description="Item #1600 | Table HL70456",
    )

    ft1_42: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ft1_42",
            "prescription_number",
            "FT1.42",
        ),
        serialization_alias="FT1.42",
        title="Prescription Number",
        description="Item #325",
    )

    ft1_43: Optional[CQ] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ft1_43",
            "ndc_qty_and_uom",
            "FT1.43",
        ),
        serialization_alias="FT1.43",
        title="NDC Qty and UOM",
        description="Item #2370",
    )

    model_config = {"populate_by_name": True}

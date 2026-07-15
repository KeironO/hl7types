"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8
Class: FT1
Type: Segment
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import AliasChoices, Field, field_validator
from hl7types.hl7 import HL7Model

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

    ft1_4 : DR
        FT1.4 - Transaction Date (DR) R S6.5.1.4

    ft1_5 : str | None
        FT1.5 - Transaction Posting Date (DTM) O S6.5.1.5

    ft1_6 : CWE
        FT1.6 - Transaction Type (CWE) R S6.5.1.6 | 0017 - Transaction Type

    ft1_7 : CWE
        FT1.7 - Transaction Code (CWE) R S17.4.2.12 | 0132 - Transaction Code

    ft1_10 : str | None
        FT1.10 - Transaction Quantity (NM) O S6.5.1.10

    ft1_11 : CP | None
        FT1.11 - Transaction Amount - Extended (CP) O S6.5.1.11

    ft1_12 : CP | None
        FT1.12 - Transaction amount - unit (CP) O S17.4.2.13

    ft1_13 : CWE | None
        FT1.13 - Department Code (CWE) O S6.5.1.13 | 0049 - Department Code

    ft1_14 : CWE | None
        FT1.14 - Health Plan ID (CWE) O S6.5.1.14 | 0072 - Insurance Plan ID

    ft1_15 : CP | None
        FT1.15 - Insurance Amount (CP) O S6.5.1.15

    ft1_16 : PL | None
        FT1.16 - Assigned Patient Location (PL) O S3.4.3.3

    ft1_17 : CWE | None
        FT1.17 - Fee Schedule (CWE) O S6.5.1.17 | 0024 - Fee Schedule

    ft1_18 : CWE | None
        FT1.18 - Patient Type (CWE) O S3.4.3.18 | 0018 - Patient Type

    ft1_19 : list[CWE] | None
        FT1.19 - Diagnosis Code - FT1 (CWE) O rep S6.5.1.19 | 0051 - Diagnosis Code

    ft1_20 : list[XCN] | None
        FT1.20 - Performed By Code (XCN) O rep S6.5.1.20 | 0084 - Performed by

    ft1_21 : list[XCN] | None
        FT1.21 - Ordered By Code (XCN) O rep S6.5.1.21

    ft1_22 : CP | None
        FT1.22 - Unit Cost (CP) O S6.5.1.22

    ft1_23 : EI | None
        FT1.23 - Filler Order Number (EI) O S10.6.1.25

    ft1_24 : list[XCN] | None
        FT1.24 - Entered By Code (XCN) O rep S6.5.1.24

    ft1_25 : CNE | None
        FT1.25 - Procedure Code (CNE) O S17.4.1.14 | 0088 - Procedure Code

    ft1_26 : list[CNE] | None
        FT1.26 - Procedure Code Modifier (CNE) O rep S17.4.1.15 | 0340 - Procedure Code Modifier

    ft1_27 : CWE | None
        FT1.27 - Advanced Beneficiary Notice Code (CWE) O S4.5.1.20 | 0339 - Advanced Beneficiary Notice Code

    ft1_28 : CWE | None
        FT1.28 - Medically Necessary Duplicate Procedure Reason (CWE) O S4.5.3.48 | 0476 - Medically Necessary Duplicate Procedure Reason

    ft1_29 : CWE | None
        FT1.29 - NDC Code (CWE) O S6.5.1.29 | 0549 - NDC Codes

    ft1_30 : CX | None
        FT1.30 - Payment Reference ID (CX) O S6.5.1.30

    ft1_31 : list[str] | None
        FT1.31 - Transaction Reference Key (SI) O rep S6.5.1.31

    ft1_32 : list[XON] | None
        FT1.32 - Performing Facility (XON) O rep S6.5.1.32

    ft1_33 : XON | None
        FT1.33 - Ordering Facility (XON) O S6.5.1.33

    ft1_34 : CWE | None
        FT1.34 - Item Number (CWE) O S6.5.1.34

    ft1_35 : str | None
        FT1.35 - Model Number (ST) O S6.5.1.35

    ft1_36 : list[CWE] | None
        FT1.36 - Special Processing Code (CWE) O rep S6.5.1.36

    ft1_37 : CWE | None
        FT1.37 - Clinic Code (CWE) O S6.5.1.37

    ft1_38 : CX | None
        FT1.38 - Referral Number (CX) O S6.5.1.38

    ft1_39 : CX | None
        FT1.39 - Authorization Number (CX) O S6.5.1.39

    ft1_40 : CWE | None
        FT1.40 - Service Provider Taxonomy Code (CWE) O S6.5.1.40

    ft1_41 : CWE | None
        FT1.41 - Revenue Code (CWE) O S6.5.1.41 | 0456 - Revenue code

    ft1_42 : str | None
        FT1.42 - Prescription Number (ST) O S4.A.4.15

    ft1_43 : CQ | None
        FT1.43 - NDC Qty and UOM (CQ) O S6.5.1.43
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

    ft1_4: DR = Field(
        validation_alias=AliasChoices(
            "ft1_4",
            "transaction_date",
            "FT1.4",
        ),
        serialization_alias="FT1.4",
        title="Transaction Date",
        description="R | Item #00358",
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
        description="O | Item #00359",
    )

    ft1_6: CWE = Field(
        validation_alias=AliasChoices(
            "ft1_6",
            "transaction_type",
            "FT1.6",
        ),
        serialization_alias="FT1.6",
        title="Transaction Type",
        description="R | Item #00360 | Table 0017 - Transaction Type",
    )

    ft1_7: CWE = Field(
        validation_alias=AliasChoices(
            "ft1_7",
            "transaction_code",
            "FT1.7",
        ),
        serialization_alias="FT1.7",
        title="Transaction Code",
        description="R | Item #00361 | Table 0132 - Transaction Code",
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
        description="O | Item #00364",
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
        title="Transaction amount - unit",
        description="O | Item #00366",
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
        description="O | Item #00367 | Table 0049 - Department Code",
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
        description="O | Item #00368 | Table 0072 - Insurance Plan ID",
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

    ft1_17: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ft1_17",
            "fee_schedule",
            "FT1.17",
        ),
        serialization_alias="FT1.17",
        title="Fee Schedule",
        description="O | Item #00370 | Table 0024 - Fee Schedule",
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
        description="O | Item #00148 | Table 0018 - Patient Type",
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
        description="O | Item #00371 | Table 0051 - Diagnosis Code",
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

    ft1_25: Optional[CNE] = Field(
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

    ft1_26: Optional[List[CNE]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ft1_26",
            "procedure_code_modifier",
            "FT1.26",
        ),
        serialization_alias="FT1.26",
        title="Procedure Code Modifier",
        description="O | Item #01316 | Table 0340 - Procedure Code Modifier",
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
        description=(
            "O | Item #01310 | Table 0339 - Advanced Beneficiary Notice Code"
        ),
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
        description=(
            "O | Item #01646 | Table 0476 - Medically Necessary Duplicate "
            "Procedure Reason"
        ),
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
        description="O | Item #01845 | Table 0549 - NDC Codes",
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
        description="O | Item #01846",
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
        description="O | Item #01847 | LEN:4",
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
        description="O | Item #02361",
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
        description="O | Item #02362",
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
        description="O | Item #02363",
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
        description="O | Item #02364",
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
        description="O | Item #02365",
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
        description="O | Item #02366",
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
        description="O | Item #02367",
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
        description="O | Item #02368",
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
        description="O | Item #02369",
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
        description="O | Item #01600 | Table 0456 - Revenue code",
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
        description="O | Item #00325",
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
        description="O | Item #02370",
    )

    @field_validator("ft1_1", "ft1_31", mode='before')
    @classmethod
    def _validate_si(cls, v: str) -> str:
        import re
        if not re.fullmatch(r'\d*', v or ''):
            raise ValueError(f"{v!r} is not empty or a non-negative integer")
        return v

    @field_validator("ft1_5", mode='before')
    @classmethod
    def _validate_dtm(cls, v: str, info: ValidationInfo) -> str:
        import re
        if re.fullmatch(r'(\d{4}([01]\d(\d{2}([012]\d([0-5]\d([0-5]\d(\.\d(\d(\d(\d)?)?)?)?)?)?)?)?)?)?([+\-]\d{4})?', v or ''):
            return v
        ctx: dict[str, object] = info.context or {}
        from typing import cast, Callable
        return _apply_dt_fallback(v, parser=cast(Callable[[str], str] | None, ctx.get("dtm_parser")), datatype="DTM", field_path="TS.1")

    @field_validator("ft1_10", mode='before')
    @classmethod
    def _validate_nm(cls, v: str) -> str:
        import re
        if not re.fullmatch(r'(\+|\-)?\d*\.?\d*', v or ''):
            raise ValueError(f"{v!r} is not empty or numeric")
        return v

    model_config = {"populate_by_name": True}

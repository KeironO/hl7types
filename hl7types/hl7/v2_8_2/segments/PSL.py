"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.2
Class: PSL
Type: Segment
"""
from __future__ import annotations

import re

from typing import Optional, List
from pydantic import AliasChoices, ConfigDict, Field, ValidationInfo, field_validator
from hl7types.hl7 import HL7Model
from hl7types.hl7._validators import _apply_dt_fallback

from ..datatypes.CP import CP
from ..datatypes.CQ import CQ
from ..datatypes.CWE import CWE
from ..datatypes.CX import CX
from ..datatypes.DR import DR
from ..datatypes.EI import EI
from ..datatypes.XCN import XCN

_RE_SI = re.compile(r'\d*')
_RE_DTM = re.compile(r'(\d{4}([01]\d(\d{2}([012]\d([0-5]\d([0-5]\d(\.\d(\d(\d(\d)?)?)?)?)?)?)?)?)?)?([+\-]\d{4})?')
_RE_NM = re.compile(r'(\+|\-)?\d*\.?\d*')


class PSL(HL7Model):
    """Product/Service Line Item (S16.4.6).

    Attributes
    ----------
    psl_1 : EI
        PSL.1 - Provider Product/Service Line Item Number (EI) R S16.4.6.1

    psl_2 : EI | None
        PSL.2 - Payer Product/Service Line Item Number (EI) O S16.4.6.2

    psl_3 : str
        PSL.3 - Product/Service Line Item Sequence Number (SI) R S16.4.6.3

    psl_4 : EI | None
        PSL.4 - Provider Tracking ID (EI) O S16.4.6.4

    psl_5 : EI | None
        PSL.5 - Payer Tracking ID (EI) O S16.4.6.5

    psl_6 : CWE
        PSL.6 - Product/Service Line Item Status (CWE) R S16.4.6.6 | 0559 - Product/Service Status

    psl_7 : CWE
        PSL.7 - Product/Service Code (CWE) R S16.4.6.7 | 0879 - Product/Service Code

    psl_8 : list[CWE] | None
        PSL.8 - Product/Service Code Modifier (CWE) O rep S16.4.6.8 | 0880 - Product/Service Code Modifier

    psl_9 : str | None
        PSL.9 - Product/Service Code Description (ST) O S16.4.6.9

    psl_10 : str | None
        PSL.10 - Product/Service Effective Date (DTM) C S16.4.6.10

    psl_11 : str | None
        PSL.11 - Product/Service Expiration Date (DTM) O S16.4.6.11

    psl_12 : CQ | None
        PSL.12 - Product/Service Quantity (CQ) C S16.4.6.12 | 0560 - Quantity Units

    psl_13 : CP | None
        PSL.13 - Product/Service Unit Cost (CP) C S16.4.6.13

    psl_14 : str | None
        PSL.14 - Number of Items per Unit (NM) C S16.4.6.14

    psl_15 : CP | None
        PSL.15 - Product/Service Gross Amount (CP) C S16.4.6.15

    psl_16 : CP | None
        PSL.16 - Product/Service Billed Amount (CP) C S16.4.6.16

    psl_17 : list[CWE] | None
        PSL.17 - Product/Service Clarification Code Type (CWE) O rep S16.4.6.17 | 0561 - Product/Services Clarification Codes

    psl_18 : list[str] | None
        PSL.18 - Product/Service Clarification Code Value (ST) O rep S16.4.6.18

    psl_19 : list[EI] | None
        PSL.19 - Health Document Reference Identifier (EI) O rep S16.4.6.19

    psl_20 : list[CWE] | None
        PSL.20 - Processing Consideration Code (CWE) O rep S16.4.6.20 | 0562 - Processing Consideration Codes

    psl_21 : str
        PSL.21 - Restricted Disclosure Indicator (ID) R S16.4.6.21 | 0532 - Expanded Yes/no Indicator

    psl_22 : CWE | None
        PSL.22 - Related Product/Service Code Indicator (CWE) O S16.4.6.22 | 0879 - Product/Service Code

    psl_23 : CP | None
        PSL.23 - Product/Service Amount for Physician (CP) O S16.4.6.23

    psl_24 : str | None
        PSL.24 - Product/Service Cost Factor (NM) O S16.4.6.24

    psl_25 : CX | None
        PSL.25 - Cost Center (CX) O S16.4.2.20

    psl_26 : DR | None
        PSL.26 - Billing Period (DR) O S16.4.6.26

    psl_27 : str | None
        PSL.27 - Days without Billing (NM) O S16.4.6.27

    psl_28 : str | None
        PSL.28 - Session-No (NM) O S16.4.6.28

    psl_29 : XCN | None
        PSL.29 - Executing Physician ID (XCN) O S16.4.6.29

    psl_30 : XCN | None
        PSL.30 - Responsible Physician ID (XCN) O S16.4.6.30

    psl_31 : CWE | None
        PSL.31 - Role Executing Physician (CWE) O S16.4.6.31 | 0881 - Role Executing Physician

    psl_32 : CWE | None
        PSL.32 - Medical Role Executing Physician (CWE) O S16.4.6.32 | 0882 - Medical Role Executing Physician

    psl_33 : CWE | None
        PSL.33 - Side of body (CWE) O S16.4.6.33 | 0894 - Side of body

    psl_34 : str | None
        PSL.34 - Number of TP's PP (NM) O S16.4.6.34

    psl_35 : CP | None
        PSL.35 - TP-Value PP (CP) O S16.4.6.35

    psl_36 : str | None
        PSL.36 - Internal Scaling Factor PP (NM) O S16.4.6.36

    psl_37 : str | None
        PSL.37 - External Scaling Factor PP (NM) O S16.4.6.37

    psl_38 : CP | None
        PSL.38 - Amount PP (CP) O S16.4.6.38

    psl_39 : str | None
        PSL.39 - Number of TP's Technical Part (NM) O S16.4.6.39

    psl_40 : CP | None
        PSL.40 - TP-Value Technical Part (CP) O S16.4.6.40

    psl_41 : str | None
        PSL.41 - Internal Scaling Factor Technical Part (NM) O S16.4.6.41

    psl_42 : str | None
        PSL.42 - External Scaling Factor Technical Part (NM) O S16.4.6.42

    psl_43 : CP | None
        PSL.43 - Amount Technical Part (CP) O S16.4.6.43

    psl_44 : CP | None
        PSL.44 - Total Amount Professional Part + Technical Part (CP) O S16.4.6.44

    psl_45 : str | None
        PSL.45 - VAT-Rate (NM) O S16.4.6.45

    psl_46 : str | None
        PSL.46 - Main-Service (ID) O S16.4.6.46

    psl_47 : str | None
        PSL.47 - Validation (ID) O S16.4.6.47 | 0136 - Yes/no Indicator

    psl_48 : str | None
        PSL.48 - Comment (ST) O S16.4.6.48
    """

    psl_1: EI = Field(
        validation_alias=AliasChoices(
            "psl_1",
            "provider_product_service_line_item_number",
            "PSL.1",
        ),
        serialization_alias="PSL.1",
        title="Provider Product/Service Line Item Number",
        description="R | Item #01955",
    )

    psl_2: Optional[EI] = Field(
        default=None,
        validation_alias=AliasChoices(
            "psl_2",
            "payer_product_service_line_item_number",
            "PSL.2",
        ),
        serialization_alias="PSL.2",
        title="Payer Product/Service Line Item Number",
        description="O | Item #01956",
    )

    psl_3: str = Field(
        validation_alias=AliasChoices(
            "psl_3",
            "product_service_line_item_sequence_number",
            "PSL.3",
        ),
        serialization_alias="PSL.3",
        title="Product/Service Line Item Sequence Number",
        description="R | Item #01957 | LEN:4",
    )

    psl_4: Optional[EI] = Field(
        default=None,
        validation_alias=AliasChoices(
            "psl_4",
            "provider_tracking_id",
            "PSL.4",
        ),
        serialization_alias="PSL.4",
        title="Provider Tracking ID",
        description="O | Item #01958",
    )

    psl_5: Optional[EI] = Field(
        default=None,
        validation_alias=AliasChoices(
            "psl_5",
            "payer_tracking_id",
            "PSL.5",
        ),
        serialization_alias="PSL.5",
        title="Payer Tracking ID",
        description="O | Item #01959",
    )

    psl_6: CWE = Field(
        validation_alias=AliasChoices(
            "psl_6",
            "product_service_line_item_status",
            "PSL.6",
        ),
        serialization_alias="PSL.6",
        title="Product/Service Line Item Status",
        description="R | Item #01960 | Table 0559 - Product/Service Status",
    )

    psl_7: CWE = Field(
        validation_alias=AliasChoices(
            "psl_7",
            "product_service_code",
            "PSL.7",
        ),
        serialization_alias="PSL.7",
        title="Product/Service Code",
        description="R | Item #01961 | Table 0879 - Product/Service Code",
    )

    psl_8: Optional[List[CWE]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "psl_8",
            "product_service_code_modifier",
            "PSL.8",
        ),
        serialization_alias="PSL.8",
        title="Product/Service Code Modifier",
        description=(
            "O | Item #01962 | Table 0880 - Product/Service Code Modifier"
        ),
    )

    psl_9: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "psl_9",
            "product_service_code_description",
            "PSL.9",
        ),
        serialization_alias="PSL.9",
        title="Product/Service Code Description",
        description="O | Item #01963",
    )

    psl_10: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "psl_10",
            "product_service_effective_date",
            "PSL.10",
        ),
        serialization_alias="PSL.10",
        title="Product/Service Effective Date",
        description="C | Item #01964",
    )

    psl_11: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "psl_11",
            "product_service_expiration_date",
            "PSL.11",
        ),
        serialization_alias="PSL.11",
        title="Product/Service Expiration Date",
        description="O | Item #01965",
    )

    psl_12: Optional[CQ] = Field(
        default=None,
        validation_alias=AliasChoices(
            "psl_12",
            "product_service_quantity",
            "PSL.12",
        ),
        serialization_alias="PSL.12",
        title="Product/Service Quantity",
        description="C | Item #01966 | Table 0560 - Quantity Units",
    )

    psl_13: Optional[CP] = Field(
        default=None,
        validation_alias=AliasChoices(
            "psl_13",
            "product_service_unit_cost",
            "PSL.13",
        ),
        serialization_alias="PSL.13",
        title="Product/Service Unit Cost",
        description="C | Item #01967",
    )

    psl_14: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "psl_14",
            "number_of_items_per_unit",
            "PSL.14",
        ),
        serialization_alias="PSL.14",
        title="Number of Items per Unit",
        description="C | Item #01968",
    )

    psl_15: Optional[CP] = Field(
        default=None,
        validation_alias=AliasChoices(
            "psl_15",
            "product_service_gross_amount",
            "PSL.15",
        ),
        serialization_alias="PSL.15",
        title="Product/Service Gross Amount",
        description="C | Item #01969",
    )

    psl_16: Optional[CP] = Field(
        default=None,
        validation_alias=AliasChoices(
            "psl_16",
            "product_service_billed_amount",
            "PSL.16",
        ),
        serialization_alias="PSL.16",
        title="Product/Service Billed Amount",
        description="C | Item #01970",
    )

    psl_17: Optional[List[CWE]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "psl_17",
            "product_service_clarification_code_type",
            "PSL.17",
        ),
        serialization_alias="PSL.17",
        title="Product/Service Clarification Code Type",
        description=(
            "O | Item #01971 | Table 0561 - Product/Services Clarification Codes"
        ),
    )

    psl_18: Optional[List[str]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "psl_18",
            "product_service_clarification_code_value",
            "PSL.18",
        ),
        serialization_alias="PSL.18",
        title="Product/Service Clarification Code Value",
        description="O | Item #01972",
    )

    psl_19: Optional[List[EI]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "psl_19",
            "health_document_reference_identifier",
            "PSL.19",
        ),
        serialization_alias="PSL.19",
        title="Health Document Reference Identifier",
        description="O | Item #01973",
    )

    psl_20: Optional[List[CWE]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "psl_20",
            "processing_consideration_code",
            "PSL.20",
        ),
        serialization_alias="PSL.20",
        title="Processing Consideration Code",
        description=(
            "O | Item #01974 | Table 0562 - Processing Consideration Codes"
        ),
    )

    psl_21: str = Field(
        validation_alias=AliasChoices(
            "psl_21",
            "restricted_disclosure_indicator",
            "PSL.21",
        ),
        serialization_alias="PSL.21",
        title="Restricted Disclosure Indicator",
        description=(
            "R | Item #01975 | Table 0532 - Expanded Yes/no Indicator | LEN:4"
        ),
    )

    psl_22: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "psl_22",
            "related_product_service_code_indicator",
            "PSL.22",
        ),
        serialization_alias="PSL.22",
        title="Related Product/Service Code Indicator",
        description="O | Item #01976 | Table 0879 - Product/Service Code",
    )

    psl_23: Optional[CP] = Field(
        default=None,
        validation_alias=AliasChoices(
            "psl_23",
            "product_service_amount_for_physician",
            "PSL.23",
        ),
        serialization_alias="PSL.23",
        title="Product/Service Amount for Physician",
        description="O | Item #01977",
    )

    psl_24: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "psl_24",
            "product_service_cost_factor",
            "PSL.24",
        ),
        serialization_alias="PSL.24",
        title="Product/Service Cost Factor",
        description="O | Item #01978",
    )

    psl_25: Optional[CX] = Field(
        default=None,
        validation_alias=AliasChoices(
            "psl_25",
            "cost_center",
            "PSL.25",
        ),
        serialization_alias="PSL.25",
        title="Cost Center",
        description="O | Item #01933",
    )

    psl_26: Optional[DR] = Field(
        default=None,
        validation_alias=AliasChoices(
            "psl_26",
            "billing_period",
            "PSL.26",
        ),
        serialization_alias="PSL.26",
        title="Billing Period",
        description="O | Item #01980",
    )

    psl_27: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "psl_27",
            "days_without_billing",
            "PSL.27",
        ),
        serialization_alias="PSL.27",
        title="Days without Billing",
        description="O | Item #01981",
    )

    psl_28: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "psl_28",
            "session_no",
            "PSL.28",
        ),
        serialization_alias="PSL.28",
        title="Session-No",
        description="O | Item #01982 | LEN:4",
    )

    psl_29: Optional[XCN] = Field(
        default=None,
        validation_alias=AliasChoices(
            "psl_29",
            "executing_physician_id",
            "PSL.29",
        ),
        serialization_alias="PSL.29",
        title="Executing Physician ID",
        description="O | Item #01983",
    )

    psl_30: Optional[XCN] = Field(
        default=None,
        validation_alias=AliasChoices(
            "psl_30",
            "responsible_physician_id",
            "PSL.30",
        ),
        serialization_alias="PSL.30",
        title="Responsible Physician ID",
        description="O | Item #01984",
    )

    psl_31: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "psl_31",
            "role_executing_physician",
            "PSL.31",
        ),
        serialization_alias="PSL.31",
        title="Role Executing Physician",
        description="O | Item #01985 | Table 0881 - Role Executing Physician",
    )

    psl_32: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "psl_32",
            "medical_role_executing_physician",
            "PSL.32",
        ),
        serialization_alias="PSL.32",
        title="Medical Role Executing Physician",
        description=(
            "O | Item #01986 | Table 0882 - Medical Role Executing Physician"
        ),
    )

    psl_33: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "psl_33",
            "side_of_body",
            "PSL.33",
        ),
        serialization_alias="PSL.33",
        title="Side of body",
        description="O | Item #01987 | Table 0894 - Side of body",
    )

    psl_34: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "psl_34",
            "number_of_tp_s_pp",
            "PSL.34",
        ),
        serialization_alias="PSL.34",
        title="Number of TP's PP",
        description="O | Item #01988",
    )

    psl_35: Optional[CP] = Field(
        default=None,
        validation_alias=AliasChoices(
            "psl_35",
            "tp_value_pp",
            "PSL.35",
        ),
        serialization_alias="PSL.35",
        title="TP-Value PP",
        description="O | Item #01989",
    )

    psl_36: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "psl_36",
            "internal_scaling_factor_pp",
            "PSL.36",
        ),
        serialization_alias="PSL.36",
        title="Internal Scaling Factor PP",
        description="O | Item #01990",
    )

    psl_37: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "psl_37",
            "external_scaling_factor_pp",
            "PSL.37",
        ),
        serialization_alias="PSL.37",
        title="External Scaling Factor PP",
        description="O | Item #01991",
    )

    psl_38: Optional[CP] = Field(
        default=None,
        validation_alias=AliasChoices(
            "psl_38",
            "amount_pp",
            "PSL.38",
        ),
        serialization_alias="PSL.38",
        title="Amount PP",
        description="O | Item #01992",
    )

    psl_39: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "psl_39",
            "number_of_tp_s_technical_part",
            "PSL.39",
        ),
        serialization_alias="PSL.39",
        title="Number of TP's Technical Part",
        description="O | Item #01993",
    )

    psl_40: Optional[CP] = Field(
        default=None,
        validation_alias=AliasChoices(
            "psl_40",
            "tp_value_technical_part",
            "PSL.40",
        ),
        serialization_alias="PSL.40",
        title="TP-Value Technical Part",
        description="O | Item #01994",
    )

    psl_41: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "psl_41",
            "internal_scaling_factor_technical_part",
            "PSL.41",
        ),
        serialization_alias="PSL.41",
        title="Internal Scaling Factor Technical Part",
        description="O | Item #01995",
    )

    psl_42: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "psl_42",
            "external_scaling_factor_technical_part",
            "PSL.42",
        ),
        serialization_alias="PSL.42",
        title="External Scaling Factor Technical Part",
        description="O | Item #01996",
    )

    psl_43: Optional[CP] = Field(
        default=None,
        validation_alias=AliasChoices(
            "psl_43",
            "amount_technical_part",
            "PSL.43",
        ),
        serialization_alias="PSL.43",
        title="Amount Technical Part",
        description="O | Item #01997",
    )

    psl_44: Optional[CP] = Field(
        default=None,
        validation_alias=AliasChoices(
            "psl_44",
            "total_amount_professional_part_technical_part",
            "PSL.44",
        ),
        serialization_alias="PSL.44",
        title="Total Amount Professional Part + Technical Part",
        description="O | Item #01998",
    )

    psl_45: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "psl_45",
            "vat_rate",
            "PSL.45",
        ),
        serialization_alias="PSL.45",
        title="VAT-Rate",
        description="O | Item #01999",
    )

    psl_46: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "psl_46",
            "main_service",
            "PSL.46",
        ),
        serialization_alias="PSL.46",
        title="Main-Service",
        description="O | Item #02000 | LEN:20",
    )

    psl_47: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "psl_47",
            "validation",
            "PSL.47",
        ),
        serialization_alias="PSL.47",
        title="Validation",
        description="O | Item #02001 | Table 0136 - Yes/no Indicator | LEN:1",
    )

    psl_48: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "psl_48",
            "comment",
            "PSL.48",
        ),
        serialization_alias="PSL.48",
        title="Comment",
        description="O | Item #02002",
    )

    @field_validator("psl_3", mode='before')
    @classmethod
    def _validate_si(cls, v: str) -> str:
        if not _RE_SI.fullmatch(v or ''):
            raise ValueError(f"{v!r} is not empty or a non-negative integer")
        return v

    @field_validator("psl_10", "psl_11", mode='before')
    @classmethod
    def _validate_dtm(cls, v: str, info: ValidationInfo) -> str:
        if _RE_DTM.fullmatch(v or ''):
            return v
        ctx: dict[str, object] = info.context or {}
        from typing import cast, Callable
        return _apply_dt_fallback(v, parser=cast(Callable[[str], str] | None, ctx.get("dtm_parser")), datatype="DTM", field_path="TS.1")

    @field_validator("psl_14", "psl_24", "psl_27", "psl_28", "psl_34", "psl_36", "psl_37", "psl_39", "psl_41", "psl_42", "psl_45", mode='before')
    @classmethod
    def _validate_nm(cls, v: str) -> str:
        if not _RE_NM.fullmatch(v or ''):
            raise ValueError(f"{v!r} is not empty or numeric")
        return v

    model_config = ConfigDict(populate_by_name=True)

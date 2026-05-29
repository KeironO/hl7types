"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.6
Class: PSL
Type: Segment
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import AliasChoices, BaseModel, Field

from ..datatypes.CP import CP
from ..datatypes.CQ import CQ
from ..datatypes.CWE import CWE
from ..datatypes.CX import CX
from ..datatypes.DR import DR
from ..datatypes.EI import EI
from ..datatypes.XCN import XCN


class PSL(BaseModel):
    """HL7 v2 PSL segment.

    Attributes
    ----------
    psl_1 : EI
        PSL.1 (req) - Provider Product/Service Line Item Number (EI)

    psl_2 : EI | None
        PSL.2 (opt) - Payer Product/Service Line Item Number (EI)

    psl_3 : str
        PSL.3 (req) - Product/Service Line Item Sequence Number (SI)

    psl_4 : EI | None
        PSL.4 (opt) - Provider Tracking ID (EI)

    psl_5 : EI | None
        PSL.5 (opt) - Payer Tracking ID (EI)

    psl_6 : CWE
        PSL.6 (req) - Product/Service Line Item Status (CWE)

    psl_7 : CWE
        PSL.7 (req) - Product/Service Code (CWE)

    psl_8 : list[CWE] | None
        PSL.8 (opt, rep) - Product/Service Code Modifier (CWE)

    psl_9 : str | None
        PSL.9 (opt) - Product/Service Code Description (ST)

    psl_10 : str | None
        PSL.10 (opt) - Product/Service Effective Date (DTM)

    psl_11 : str | None
        PSL.11 (opt) - Product/Service Expiration Date (DTM)

    psl_12 : CQ | None
        PSL.12 (opt) - Product/Service Quantity (CQ)

    psl_13 : CP | None
        PSL.13 (opt) - Product/Service Unit Cost (CP)

    psl_14 : str | None
        PSL.14 (opt) - Number of Items per Unit (NM)

    psl_15 : CP | None
        PSL.15 (opt) - Product/Service Gross Amount (CP)

    psl_16 : CP | None
        PSL.16 (opt) - Product/Service Billed Amount (CP)

    psl_17 : list[str] | None
        PSL.17 (opt, rep) - Product/Service Clarification Code Type (IS)

    psl_18 : list[str] | None
        PSL.18 (opt, rep) - Product/Service Clarification Code Value (ST)

    psl_19 : list[EI] | None
        PSL.19 (opt, rep) - Health Document Reference Identifier (EI)

    psl_20 : list[str] | None
        PSL.20 (opt, rep) - Processing Consideration Code (IS)

    psl_21 : str
        PSL.21 (req) - Restricted Disclosure Indicator (ID)

    psl_22 : CWE | None
        PSL.22 (opt) - Related Product/Service Code Indicator (CWE)

    psl_23 : CP | None
        PSL.23 (opt) - Product/Service Amount for Physician (CP)

    psl_24 : str | None
        PSL.24 (opt) - Product/Service Cost Factor (NM)

    psl_25 : CX | None
        PSL.25 (opt) - Cost Center (CX)

    psl_26 : DR | None
        PSL.26 (opt) - Billing Period (DR)

    psl_27 : str | None
        PSL.27 (opt) - Days without Billing (NM)

    psl_28 : str | None
        PSL.28 (opt) - Session-No (NM)

    psl_29 : XCN | None
        PSL.29 (opt) - Executing Physician ID (XCN)

    psl_30 : XCN | None
        PSL.30 (opt) - Responsible Physician ID (XCN)

    psl_31 : CWE | None
        PSL.31 (opt) - Role Executing Physician (CWE)

    psl_32 : CWE | None
        PSL.32 (opt) - Medical Role Executing Physician (CWE)

    psl_33 : CWE | None
        PSL.33 (opt) - Side of body (CWE)

    psl_34 : str | None
        PSL.34 (opt) - Number of TP's PP (NM)

    psl_35 : CP | None
        PSL.35 (opt) - TP-Value PP (CP)

    psl_36 : str | None
        PSL.36 (opt) - Internal Scaling Factor PP (NM)

    psl_37 : str | None
        PSL.37 (opt) - External Scaling Factor PP (NM)

    psl_38 : CP | None
        PSL.38 (opt) - Amount PP (CP)

    psl_39 : str | None
        PSL.39 (opt) - Number of TP's Technical Part (NM)

    psl_40 : CP | None
        PSL.40 (opt) - TP-Value Technical Part (CP)

    psl_41 : str | None
        PSL.41 (opt) - Internal Scaling Factor Technical Part (NM)

    psl_42 : str | None
        PSL.42 (opt) - External Scaling Factor Technical Part (NM)

    psl_43 : CP | None
        PSL.43 (opt) - Amount Technical Part (CP)

    psl_44 : CP | None
        PSL.44 (opt) - Total Amount Professional Part + Technical Part (CP)

    psl_45 : str | None
        PSL.45 (opt) - VAT-Rate (NM)

    psl_46 : str | None
        PSL.46 (opt) - Main-Service (ID)

    psl_47 : str | None
        PSL.47 (opt) - Validation (ID)

    psl_48 : str | None
        PSL.48 (opt) - Comment (ST)
    """

    psl_1: EI = Field(
        default=...,
        validation_alias=AliasChoices(
            "psl_1",
            "provider_product_service_line_item_number",
            "PSL.1",
        ),
        serialization_alias="PSL.1",
        title="Provider Product/Service Line Item Number",
        description="Item #1955",
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
        description="Item #1956",
    )

    psl_3: str = Field(
        default=...,
        validation_alias=AliasChoices(
            "psl_3",
            "product_service_line_item_sequence_number",
            "PSL.3",
        ),
        serialization_alias="PSL.3",
        title="Product/Service Line Item Sequence Number",
        description="Item #1957",
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
        description="Item #1958",
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
        description="Item #1959",
    )

    psl_6: CWE = Field(
        default=...,
        validation_alias=AliasChoices(
            "psl_6",
            "product_service_line_item_status",
            "PSL.6",
        ),
        serialization_alias="PSL.6",
        title="Product/Service Line Item Status",
        description="Item #1960 | Table HL70559",
    )

    psl_7: CWE = Field(
        default=...,
        validation_alias=AliasChoices(
            "psl_7",
            "product_service_code",
            "PSL.7",
        ),
        serialization_alias="PSL.7",
        title="Product/Service Code",
        description="Item #1961 | Table HL70879",
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
        description="Item #1962 | Table HL70880",
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
        description="Item #1963",
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
        description="Item #1964",
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
        description="Item #1965",
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
        description="Item #1966 | Table HL70560",
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
        description="Item #1967",
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
        description="Item #1968",
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
        description="Item #1969",
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
        description="Item #1970",
    )

    psl_17: Optional[List[str]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "psl_17",
            "product_service_clarification_code_type",
            "PSL.17",
        ),
        serialization_alias="PSL.17",
        title="Product/Service Clarification Code Type",
        description="Item #1971 | Table HL70561",
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
        description="Item #1972",
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
        description="Item #1973",
    )

    psl_20: Optional[List[str]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "psl_20",
            "processing_consideration_code",
            "PSL.20",
        ),
        serialization_alias="PSL.20",
        title="Processing Consideration Code",
        description="Item #1974 | Table HL70562",
    )

    psl_21: str = Field(
        default=...,
        validation_alias=AliasChoices(
            "psl_21",
            "restricted_disclosure_indicator",
            "PSL.21",
        ),
        serialization_alias="PSL.21",
        title="Restricted Disclosure Indicator",
        description="Item #1975 | Table HL70532",
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
        description="Item #1976 | Table HL70879",
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
        description="Item #1977",
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
        description="Item #1978",
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
        description="Item #1933",
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
        description="Item #1980",
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
        description="Item #1981",
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
        description="Item #1982",
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
        description="Item #1983",
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
        description="Item #1984",
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
        description="Item #1985 | Table HL70881",
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
        description="Item #1986 | Table HL70882",
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
        description="Item #1987 | Table HL70894",
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
        description="Item #1988",
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
        description="Item #1989",
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
        description="Item #1990",
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
        description="Item #1991",
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
        description="Item #1992",
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
        description="Item #1993",
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
        description="Item #1994",
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
        description="Item #1995",
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
        description="Item #1996",
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
        description="Item #1997",
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
        description="Item #1998",
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
        description="Item #1999",
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
        description="Item #2000",
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
        description="Item #2001 | Table HL70136",
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
        description="Item #2002",
    )

    model_config = {"populate_by_name": True}

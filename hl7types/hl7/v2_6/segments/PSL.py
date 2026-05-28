"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.6
Class: PSL
Type: Segment
"""

from __future__ import annotations

from pydantic import AliasChoices, BaseModel, Field

from ..datatypes.CP import CP
from ..datatypes.CQ import CQ
from ..datatypes.CWE import CWE
from ..datatypes.CX import CX
from ..datatypes.DR import DR
from ..datatypes.EI import EI
from ..datatypes.XCN import XCN


class PSL(BaseModel):
    """HL7 v2 PSL segment."""

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

    psl_2: EI | None = Field(
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

    psl_4: EI | None = Field(
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

    psl_5: EI | None = Field(
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

    psl_8: list[CWE] | None = Field(
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

    psl_9: str | None = Field(
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

    psl_10: str | None = Field(
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

    psl_11: str | None = Field(
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

    psl_12: CQ | None = Field(
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

    psl_13: CP | None = Field(
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

    psl_14: str | None = Field(
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

    psl_15: CP | None = Field(
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

    psl_16: CP | None = Field(
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

    psl_17: list[str] | None = Field(
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

    psl_18: list[str] | None = Field(
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

    psl_19: list[EI] | None = Field(
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

    psl_20: list[str] | None = Field(
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

    psl_22: CWE | None = Field(
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

    psl_23: CP | None = Field(
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

    psl_24: str | None = Field(
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

    psl_25: CX | None = Field(
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

    psl_26: DR | None = Field(
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

    psl_27: str | None = Field(
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

    psl_28: str | None = Field(
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

    psl_29: XCN | None = Field(
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

    psl_30: XCN | None = Field(
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

    psl_31: CWE | None = Field(
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

    psl_32: CWE | None = Field(
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

    psl_33: CWE | None = Field(
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

    psl_34: str | None = Field(
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

    psl_35: CP | None = Field(
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

    psl_36: str | None = Field(
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

    psl_37: str | None = Field(
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

    psl_38: CP | None = Field(
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

    psl_39: str | None = Field(
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

    psl_40: CP | None = Field(
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

    psl_41: str | None = Field(
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

    psl_42: str | None = Field(
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

    psl_43: CP | None = Field(
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

    psl_44: CP | None = Field(
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

    psl_45: str | None = Field(
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

    psl_46: str | None = Field(
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

    psl_47: str | None = Field(
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

    psl_48: str | None = Field(
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
